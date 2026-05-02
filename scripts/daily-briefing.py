#!/usr/bin/env python3
"""
Cogito daily briefing — reads local goal and memory files,
calls the Anthropic API, and sends the briefing via email.
"""
import smtplib
import subprocess
import sys
from datetime import date, datetime
from email.mime.text import MIMEText
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip3 install anthropic")
    sys.exit(1)


COGITO_DIR = Path(__file__).parent.parent
DOMAINS = ["professional", "financial", "health-fitness", "growth", "social-life"]


def keychain_get(service: str, account: str) -> str | None:
    result = subprocess.run(
        ["security", "find-generic-password", "-s", service, "-a", account, "-w"],
        capture_output=True, text=True
    )
    return result.stdout.strip() if result.returncode == 0 else None


def read_file(path: Path) -> str:
    if path.exists():
        return path.read_text().strip()
    return ""


def build_context() -> str:
    today = date.today()
    year = today.strftime("%Y")
    month = today.strftime("%Y-%m")
    week = f"{year}-W{today.isocalendar()[1]:02d}"

    sections = [f"Today is {today.strftime('%A, %B %d, %Y')}.\n"]

    year_goals = read_file(COGITO_DIR / "goals" / f"{year}.md")
    month_goals = read_file(COGITO_DIR / "goals" / f"{month}.md")
    week_goals = read_file(COGITO_DIR / "goals" / f"{week}.md")

    if year_goals:
        sections.append(f"## Yearly Goals\n{year_goals}")
    if month_goals:
        sections.append(f"## This Month's OKRs\n{month_goals}")
    if week_goals:
        sections.append(f"## This Week's Priorities\n{week_goals}")

    for domain in DOMAINS:
        memory = read_file(COGITO_DIR / domain / "memory.md")
        if memory and "_No entries yet._" not in memory:
            sections.append(f"## {domain.title()} Memory\n{memory}")

    return "\n\n".join(sections)


def generate_briefing(context: str, api_key: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are generating a daily morning briefing for a personal life OS called Cogito.

Produce a briefing in exactly three sections. The entire briefing should take 90 seconds to read.

**Today** — List today's date and any goal or open item needing action today. 5 lines max.

**Goal Spotlight** — Pick one monthly OKR. State its current status in one sentence. Give one specific action for today.

**One Signal** — Surface one specific thing the user probably hasn't thought about: a pattern, a drift, a conflict, or a cross-domain connection. Be specific. No generalities.

Format:
## Briefing — [Weekday, Month Day]

**Today**
...

**Goal Spotlight — [domain]**
...

**One Signal**
...

No preamble. No summary. Direct and brief.

---

Context:
{context}"""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


def send_email(briefing: str, to_address: str, gmail_user: str, gmail_password: str):
    subject = f"Cogito — {date.today().strftime('%A, %b %d')}"
    msg = MIMEText(briefing, "plain")
    msg["Subject"] = subject
    msg["From"] = gmail_user
    msg["To"] = to_address

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_address, msg.as_string())


def main():
    api_key = keychain_get("cogito", "anthropic_api_key")
    if not api_key:
        print("ERROR: Anthropic API key not found in Keychain. Run install-briefing.sh to configure.")
        sys.exit(1)

    gmail_user = keychain_get("cogito", "gmail_user")
    gmail_password = keychain_get("cogito", "gmail_app_password")
    to_address = keychain_get("cogito", "briefing_email")

    if not all([gmail_user, gmail_password, to_address]):
        print("ERROR: Email credentials not found in Keychain. Run install-briefing.sh to configure.")
        sys.exit(1)

    context = build_context()
    briefing = generate_briefing(context, api_key)
    send_email(briefing, to_address, gmail_user, gmail_password)
    print(f"Briefing sent to {to_address}")


if __name__ == "__main__":
    main()
