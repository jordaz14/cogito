# Cogito

A personal Chief of Staff built on Claude Code. Cogito gives you a trusted advisor that knows your values, remembers your context, and gets more useful over time — across five domains of your life.

No SaaS, no subscriptions, no data leaving your machine except the API calls you make yourself. Your context lives in plain markdown files you own completely.

---

## What it is

Cogito is a structured life OS with five domains — Professional, Financial, Health & Fitness, Growth, and Social & Life. Each domain has:

- A **philosophy file** — your values, principles, and non-negotiables
- A **memory file** — running context captured automatically after each session
- A **specialized advisor** — calibrated to your specific goals, not a generic template

At setup, you walk through each domain in a conversational session. The system searches for real experts whose frameworks match what you described, you pick one per domain, and that expert becomes the lens your advisor uses.

A hierarchy of goal-setting skills keeps everything coherent: yearly objectives anchor monthly OKRs, which anchor weekly priorities. Run `/cogito:checkin` any morning for a 90-second briefing: what's on your calendar, where a goal stands, and one thing the system noticed that you probably haven't.

---

## Requirements

- A [Claude](https://claude.ai) account with [Claude Code](https://claude.ai/code) installed

---

## Install

```bash
claude plugin install cogito@github
```

Or test locally from this repo:

```bash
claude --plugin-dir /path/to/cogito-plugin
```

---

## Getting started

**1. Create a project directory**

Cogito writes your personal data (philosophy files, memory, goals) into whichever directory you open Claude Code from. Create a dedicated directory:

```bash
mkdir ~/cogito && cd ~/cogito
claude
```

**2. Run setup**

```
/cogito:setup
```

A 15–20 minute conversational session that:
- Asks about your life across five domains
- Writes a personalized `CLAUDE.md` with your full context
- Seeds each domain's philosophy file in your voice
- Searches for and calibrates an expert framework for each advisor

Resumable — `/cogito:setup` picks up from the first incomplete section.

**3. Set your goals**

```
/cogito:year
```

Then `/cogito:month`, then `/cogito:week`. Each is blocked until its parent exists.

---

## Skills

| Skill | What it does |
|-------|-------------|
| `/cogito:setup` | First-time onboarding. Resumable. |
| `/cogito:checkin` | Daily briefing — Today, Goal Spotlight, One Signal |
| `/cogito:year` | Set annual objectives with key results |
| `/cogito:month` | Set monthly OKRs derived from yearly goals |
| `/cogito:week` | Set weekly priorities (3 max) derived from monthly OKRs |
| `/cogito:decision` | Structured decision framework for significant choices |
| `/cogito:remember` | Manually log a memory entry to a domain |

---

## Advisors

Each domain has a dedicated subagent Claude Code activates automatically:

| Domain | Agent | Triggers on |
|--------|-------|-------------|
| Professional | `career-advisor` | Career questions, job opportunities, skill-building |
| Financial | `cfo` | Money, investments, budgets, financial decisions |
| Health & Fitness | `coach` | Training, nutrition, recovery, fitness goals |
| Growth | `growth-director` | Books, writing, creative projects, learning |
| Social & Life | `social-advisor` | Relationships, social life, personal world |

---

## How memory works

At the end of every session, Cogito automatically reviews what was discussed and appends anything worth remembering to the relevant domain's `memory.md`. No manual journaling required. The longer you use it, the more context it carries.

You can also log memories manually with `/cogito:remember`.

---

## Your project structure

After setup, your Cogito project directory will look like this:

```
~/cogito/                        — your project directory (not this repo)
  CLAUDE.md                      — personalized context (gitignored)
  goals/
    2026.md                      — yearly objectives
    2026-05.md                   — monthly OKRs
    2026-W18.md                  — weekly priorities
  professional/
    philosophy.md                — your values and principles
    memory.md                    — running context (auto-captured)
    other/profile.md             — current role and skills (optional)
  financial/
    philosophy.md
    memory.md
    other/profile.md             — account details (optional)
  health-fitness/
    philosophy.md
    memory.md
    other/cooking.md             — meal prep context (optional)
  growth/
    philosophy.md
    memory.md
    other/reading.md             — reading list and taste (optional)
  social-life/
    philosophy.md
    memory.md
```

None of this lives in the plugin repo — it's all written into your own directory by `/cogito:setup`.

---

## Philosophy

Structure compounds. A philosophy file you wrote yourself produces better advice than a template. A goal hierarchy you maintain produces better weeks than a to-do list. A memory that builds over time produces an advisor that actually knows you.

Everything else is up to you.

---

## License

MIT
