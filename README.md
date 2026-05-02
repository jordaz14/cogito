# Cogito

A personal Chief of Staff built on Claude Code. Cogito gives you a trusted advisor that knows your values, remembers your context, and gets more useful over time — across five domains of your life.

It is deliberately stripped back. No SaaS, no subscriptions, no data leaving your machine except the API calls you make yourself. Your context lives in plain markdown files you own completely.

---

## What it is

Cogito is a structured life OS with five domains — Professional, Financial, Health & Fitness, Growth, and Social & Life. Each domain has a philosophy file (your values and principles), a memory file (your history and running context), and a specialized AI advisor whose expertise is calibrated to your specific goals.

At setup, you walk through each domain in a conversational session. The system searches for real experts whose frameworks match what you described, you pick one per domain, and that expert becomes the lens your advisor uses — not a generic template.

From there, a hierarchy of goal-setting skills keeps everything coherent: yearly objectives anchor monthly OKRs, which anchor weekly priorities. Run `/checkin` any morning for a 90-second briefing: what's on your calendar, where a goal stands, and one thing the system noticed that you probably haven't.

---

## What you need

- A [Claude](https://claude.ai) account with [Claude Code](https://claude.ai/code) installed
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

You can stop at any point and pick up where you left off — `/setup` resumes from the first incomplete section.

**4. Set your goals**

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

## The me/ directory

Alongside the advisor layer, Cogito includes a `me/` directory — free-use personal space organized around the same five domains. Use it for whatever suits you: daily notes, training logs, reading notes, writing drafts, project documents. Your advisors read from `me/` when it's relevant to what you're asking.

Suggested files per domain are documented in `me/README.md`.

---

## Reading on mobile

Cogito files are plain markdown — readable on any device with a markdown viewer. Good options:

**iOS:** [Obsidian](https://obsidian.md) (recommended — syncs seamlessly if you're already using it), [iA Writer](https://ia.net/writer), [Bear](https://bear.app)

**Android:** [Obsidian](https://obsidian.md), [Markor](https://gsantner.net/project/markor.html), [iA Writer](https://ia.net/writer)

If you store your Cogito directory in iCloud, Dropbox, or a synced folder, any of these apps will give you read access to your memory files, goals, and notes from your phone — without needing Claude Code open.

---

## How memory works

At the end of every session, Cogito automatically extracts what's worth remembering and appends it to the relevant domain's `memory.md`. No manual journaling required. The longer you use it, the more context it carries.

Memory files are excluded from `.gitignore` by default — they're personal data that should stay on your machine.

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
    other/profile.md           — current role and skills (optional)
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
    other/reading.md           — reading list and taste (optional)
  social-life/
    philosophy.md
    memory.md
  .claude/
    agents/                    — five domain advisors
    skills/                    — setup, year, month, week, checkin, decision
    hooks/                     — session-memory auto-capture
    settings.json
```

---

## Philosophy

Cogito is opinionated about one thing: structure compounds. A philosophy file you wrote yourself produces better advice than a template. A goal hierarchy you maintain produces better weeks than a to-do list. A memory that builds over time produces an advisor that actually knows you.

Everything else is up to you.

---

## License

MIT — do whatever you want with it.
