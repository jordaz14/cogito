# Cogito

A personal Chief of Staff built on Claude Code. Cogito gives you a trusted advisor that knows your values, remembers your context, and gets more useful over time — across five domains of your life.

It is deliberately stripped back. No SaaS, no subscriptions, no data leaving your machine except the API calls you make yourself. Your context lives in plain markdown files you own completely.

---

## What it is

Cogito is a structured life OS with five domains — Professional, Financial, Health & Fitness, Growth, and Social & Life. Each domain has a philosophy file (your values and principles), a memory file (your history and running context), and a specialized AI advisor whose expertise is calibrated to your specific goals.

At setup, you walk through each domain in a conversational session. The system searches for real experts whose frameworks match what you described, you pick one per domain, and that expert becomes the lens your advisor uses — not a generic template.

From there, a hierarchy of goal-setting skills keeps everything coherent: yearly objectives anchor monthly OKRs, which anchor weekly priorities. A daily briefing lands in your inbox each morning: what's on your calendar, where a goal stands, and one thing the system noticed that you probably haven't.

---

## What you need

- A [Claude](https://claude.ai) account with [Claude Code](https://claude.ai/code) installed
- An [Anthropic API key](https://console.anthropic.com) (for the daily briefing)
- Python 3.10+ (for the briefing script)
- A Gmail account with an [app password](https://support.google.com/accounts/answer/185833) configured (for sending the briefing)
- macOS, Windows, or Linux

---

## Setup

**1. Get the repo**

```bash
git clone https://github.com/julianordaz/cogito.git
cd cogito
```

Or use the GitHub template button to create a private copy under your own account.

**2. Open it in Claude Code**

```bash
claude .
```

Or open the folder in the Claude Code desktop app.

**3. Run setup**

```
/setup
```

This is a 15–20 minute conversational session. It will:

- Ask you about your life across five domains
- Write a personalized `CLAUDE.md` with your full context
- Seed each domain's philosophy file in your voice
- Search for and calibrate an expert framework for each advisor
- Ask where to send your daily briefing

You can stop at any point and pick up where you left off — `/setup` resumes from the first incomplete section.

**4. Install the daily briefing**

```bash
bash scripts/install-briefing.sh
```

Follow the prompts. Your API key and Gmail credentials are stored in your system keychain — never in any file.

**5. Set your goals**

```
/year
```

Then `/month`, then `/week`. Each is blocked until its parent exists.

---

## Skills

| Skill | What it does |
|-------|-------------|
| `/setup` | First-time onboarding. Resumable. |
| `/year` | Set annual objectives with key results |
| `/month` | Set monthly OKRs derived from yearly goals |
| `/week` | Set weekly priorities (3 max) derived from monthly OKRs |
| `/checkin` | Daily briefing — Today, Goal Spotlight, One Signal |
| `/decision` | Structured decision framework for significant choices |

---

## Daily briefing

The briefing arrives at your configured time every morning. Three sections, 90 seconds to read:

**Today** — calendar events and one action item if relevant

**Goal Spotlight** — one monthly OKR, its status, one action for today

**One Signal** — something the system noticed: a goal that's drifted, a conflict, a pattern across domains

The briefing requires your machine to be on or in sleep mode — it runs locally via launchd (Mac), Task Scheduler (Windows), or cron (Linux). See [Scheduling on Windows and Linux](#scheduling-on-windows-and-linux) below.

---

## How memory works

At the end of every session, Cogito automatically extracts what's worth remembering and appends it to the relevant domain's `memory.md`. No manual journaling required. The longer you use it, the more context it carries.

Memory files are excluded from `.gitignore` by default — they're personal data that should stay on your machine.

---

## Scheduling on Windows and Linux

**Windows — Task Scheduler**

1. Open Task Scheduler → Create Basic Task
2. Set trigger: Daily at your preferred time
3. Action: Start a program
   - Program: `python`
   - Arguments: `C:\path\to\cogito\scripts\daily-briefing.py`
4. Store credentials using Windows Credential Manager instead of Keychain — you'll need to modify `daily-briefing.py` to use `keyring` instead of the `security` CLI

**Linux — cron**

```bash
crontab -e
```

Add:
```
30 7 * * * /usr/bin/python3 /path/to/cogito/scripts/daily-briefing.py
```

Store credentials using `secret-tool` (GNOME Keyring) or `keyring` Python library, and update `daily-briefing.py` accordingly.

---

## File structure

```
cogito/
  CLAUDE.md                    — your personalized context (gitignored)
  goals/                       — goal files (gitignored)
    2026.md                    — yearly objectives
    2026-05.md                 — monthly OKRs
    2026-W18.md                — weekly priorities
  professional/
    philosophy.md              — your professional values and principles
    memory.md                  — running context (gitignored)
  financial/
    philosophy.md
    memory.md
    other/profile.md           — account details (optional)
  health-fitness/
    philosophy.md
    memory.md
    other/cooking.md           — meal prep context (optional)
  growth/
    philosophy.md
    memory.md
  social-life/
    philosophy.md
    memory.md
  .claude/
    agents/                    — five domain advisors
    skills/                    — setup, year, month, week, checkin, decision
    hooks/                     — session-memory auto-capture
    settings.json
  scripts/
    daily-briefing.py
    install-briefing.sh
```

---

## Philosophy

Cogito is opinionated about one thing: structure compounds. A philosophy file you wrote yourself produces better advice than a template. A goal hierarchy you maintain produces better weeks than a to-do list. A memory that builds over time produces an advisor that actually knows you.

Everything else is up to you.

---

## License

MIT — do whatever you want with it.
