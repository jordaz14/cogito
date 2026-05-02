#!/usr/bin/env python3
import json, sys, re, subprocess, shutil
from pathlib import Path
from datetime import date

STATE_FILE = Path.home() / ".claude" / "session-memory-state.json"
NEW_MESSAGES_THRESHOLD = 10

CLAUDE_BIN_CANDIDATES = [
    shutil.which("claude"),
    str(Path.home() / ".local" / "bin" / "claude"),
    "/usr/local/bin/claude",
    "/opt/homebrew/bin/claude",
]


def find_claude_bin():
    for candidate in CLAUDE_BIN_CANDIDATES:
        if candidate and Path(candidate).exists():
            return candidate
    return None


def extract_conversation(transcript_path):
    messages = []
    with open(transcript_path) as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
            except json.JSONDecodeError:
                continue
            role = entry.get("message", {}).get("role")
            if role not in ("user", "assistant"):
                continue
            content = entry.get("message", {}).get("content", [])
            if isinstance(content, str):
                if content.strip():
                    messages.append(f"{role.upper()}: {content.strip()}")
                continue
            for block in content:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "text" and block.get("text", "").strip():
                    messages.append(f"{role.upper()}: {block['text'].strip()}")
    return messages


def main():
    claude_bin = find_claude_bin()
    if not claude_bin:
        sys.exit(0)

    hook_input = json.load(sys.stdin)
    transcript_path = hook_input.get("transcript_path")
    if not transcript_path or not Path(transcript_path).exists():
        sys.exit(0)

    messages = extract_conversation(transcript_path)
    if len(messages) < 5:
        sys.exit(0)

    session_id = hook_input.get("session_id", transcript_path)
    state = {}
    if STATE_FILE.exists():
        try:
            state = json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    raw_state = state.get(session_id, {})
    if isinstance(raw_state, int):
        raw_state = {"count": raw_state, "written": []}
    last_count = raw_state.get("count", 0)
    written_domains = set(raw_state.get("written", []))
    if len(messages) - last_count < NEW_MESSAGES_THRESHOLD:
        sys.exit(0)

    conversation = "\n\n".join(messages[-60:])

    prompt = f"""You are a memory keeper for a personal life OS with 5 domains.

Review this conversation and identify anything worth preserving as a memory entry — facts, decisions, progress updates, preferences, or context that would be useful in a future session. Be conservative: skip conversational mechanics, hypotheticals, and things already obvious from files.

For each domain, return a single concise memory entry (1-3 sentences, past tense) OR null if nothing notable happened in that domain.

Domains:
- professional: career moves, skill progress, job search, work decisions
- financial: account changes, spending decisions, investment actions, financial milestones
- health-fitness: training progress, injuries, fitness decisions, health updates
- growth: books read, writing progress, creative projects, language practice, hobbies
- social-life: relationship events, social activities, hosting, travel, family

Return ONLY valid JSON — no explanation, no markdown fences:
{{"professional": "entry text" or null, "financial": "entry text" or null, "health-fitness": "entry text" or null, "growth": "entry text" or null, "social-life": "entry text" or null}}

Conversation:
{conversation}"""

    try:
        result = subprocess.run(
            [claude_bin, "-p", prompt],
            capture_output=True, text=True, timeout=60
        )
        raw = result.stdout.strip()
        raw = re.sub(r'^```(?:json)?\n?', '', raw)
        raw = re.sub(r'\n?```$', '', raw)
        memories = json.loads(raw)
    except Exception as e:
        log = Path.home() / ".claude" / "session-memory.log"
        log.write_text(f"{date.today()} ERROR: {e}\n")
        sys.exit(0)

    agent_dir = Path(__file__).parent.parent.parent
    today = date.today().isoformat()

    domain_map = {
        "professional":   agent_dir / "professional"   / "memory.md",
        "financial":      agent_dir / "financial"      / "memory.md",
        "health-fitness": agent_dir / "health-fitness" / "memory.md",
        "growth":         agent_dir / "growth"         / "memory.md",
        "social-life":    agent_dir / "social-life"    / "memory.md",
    }

    for domain, entry in memories.items():
        if not entry or domain not in domain_map or domain in written_domains:
            continue
        mem_file = domain_map[domain]
        if not mem_file.exists():
            continue
        content = mem_file.read_text()
        content = content.replace("_No entries yet._", "").rstrip()
        content += f"\n\n**{today} — Auto-captured**\n{entry.strip()}\n"
        mem_file.write_text(content)
        written_domains.add(domain)

    state[session_id] = {"count": len(messages), "written": list(written_domains)}
    STATE_FILE.write_text(json.dumps(state))


if __name__ == "__main__":
    main()
