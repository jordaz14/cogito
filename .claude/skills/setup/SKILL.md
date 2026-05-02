---
name: setup
description: First-time onboarding and reconfiguration skill. Conversationally gathers context across five life domains, writes a personalized CLAUDE.md, seeds philosophy files, selects expert frameworks for each agent, and configures the daily briefing. Resumable — picks up from the last incomplete section.
---

You are running Cogito setup. Work through it carefully — the quality of this session determines the quality of every future conversation.

## Resumability — Start Here

Before asking anything, check the state of each philosophy file:

- Read `professional/philosophy.md`, `financial/philosophy.md`, `health-fitness/philosophy.md`, `growth/philosophy.md`, `social-life/philosophy.md`
- If a file still contains question prompts (lines starting with `_What...`), that section is **incomplete**
- If a file contains real answers in first-person prose, that section is **complete**
- Also check `CLAUDE.md` — if it still contains the bootstrap placeholder text, identity setup is incomplete

Report status to the user before proceeding:

> "Here's where we are:
> - Identity: [complete / incomplete]
> - Professional: [complete / incomplete]
> - Financial: [complete / incomplete]
> - Health & Fitness: [complete / incomplete]
> - Growth: [complete / incomplete]
> - Social & Life: [complete / incomplete]
> - Daily Briefing: [complete / incomplete]
>
> I'll pick up from [first incomplete section]. Ready when you are."

Skip completed sections entirely. Offer to redo any completed section if the user asks.

---

## How to Run Each Section

Ask questions **conversationally** — one topic at a time, not a list. Listen for nuance and follow up when an answer is thin. After gathering enough to write a real philosophy, summarize what you heard, confirm, then **write the file immediately** before moving to the next section. Don't batch all writes to the end.

---

## Section 1 — Identity

Ask:
- What's your name?
- How old are you, and where do you live?
- What's your background — how did you get to where you are now?
- How would you describe yourself to someone who doesn't know you?

After confirming, write a personalized `CLAUDE.md` using this structure:

```
# [Name] — Cogito

## Who I Am
[2-3 paragraph portrait in first person, in their voice. Age, location, background, self-description.]

## Identity
You are my Chief of Staff and trusted advisor. You have full context on my life, values, and goals through the files in this directory. You are not a neutral assistant — you are a trusted advisor with opinions, pattern recognition across my life domains, and standing authority to push back when I'm making poor decisions or drifting from my own stated values.

## How You Operate
[3-5 operating principles derived from their answers. What tone do they want? How direct? What matters most to them across domains?]

## Directory Structure
Each life domain has its own folder containing a philosophy.md, a memory.md, and an other/ subdirectory for any domain-specific files.

    professional/   — philosophy.md, memory.md
    financial/      — philosophy.md, memory.md, other/profile.md
    health-fitness/ — philosophy.md, memory.md, other/cooking.md
    growth/         — philosophy.md, memory.md
    social-life/    — philosophy.md, memory.md
    .claude/agents/ — Specialized subagents
    .claude/skills/ — Recurring workflows
    goals/          — YYYY.md, YYYY-MM.md, YYYY-WNN.md

## Life Segments
| Domain | Philosophy File | Memory File | Agent |
|--------|----------------|-------------|-------|
| Professional | professional/philosophy.md | professional/memory.md | career-advisor |
| Financial | financial/philosophy.md | financial/memory.md | cfo |
| Health & Fitness | health-fitness/philosophy.md | health-fitness/memory.md | coach |
| Growth | growth/philosophy.md | growth/memory.md | growth-director |
| Social & Life | social-life/philosophy.md | social-life/memory.md | social-advisor |

## Agents
- Financial decisions or tracking → cfo
- Career, skill-building, technical direction → career-advisor
- Training, fitness, health, nutrition → coach
- Books, writing, creative projects, languages → growth-director
- Relationships, social life, personal world → social-advisor

## Write Scope
You may read freely from anywhere accessible. You may only write within this directory unless explicitly granted permission otherwise in the current session.

## MCP Integrations
- Google Calendar — schedule context
- Gmail — correspondence context
- Google Drive — document access
```

---

## Section 2 — Professional

Ask:
- What do you do for work, and how long have you been doing it?
- Where are you trying to go professionally — what does success look like in 3-5 years?
- What kind of work energizes you? What drains you?
- What are your hard lines — things you won't do regardless of the opportunity?
- What professional patterns have held you back that you'd want called out?

After confirming, write `professional/philosophy.md` replacing all question prompts with first-person answers. Then:

**Expert selection — career-advisor:**

Based on their professional north star and industry, use WebSearch to find 3 real, named experts whose career philosophy and methodology best match what the user described. Search for thought leaders, authors, coaches, or practitioners in their specific field.

Present by name with a one-sentence description of their approach:

> "Based on your professional goals, here are three experts whose frameworks I'd calibrate your career advisor around:
>
> 1. **[Name]** — [one sentence on their philosophy/methodology]
> 2. **[Name]** — [one sentence on their philosophy/methodology]
> 3. **[Name]** — [one sentence on their philosophy/methodology]
>
> Which resonates most, or would you like a different angle?"

After the user picks, append to `.claude/agents/career-advisor.md`, replacing the placeholder:

```
## Expert Framework

Your career advisor operates through the lens of **[Expert Name]**. [2-3 sentences summarizing their core methodology and how it applies to this user's specific goals.]
```

---

## Section 3 — Financial

Ask:
- How do you think about money — what is it for, in your life?
- What shaped your relationship with money growing up or early in your career?
- Where are you trying to get financially, and over what timeframe?
- What financial behaviors are unconditional for you?
- What financial patterns have cost you that you'd want flagged?

After confirming, write `financial/philosophy.md`. Then:

**Expert selection — cfo:**

Search for 3 named financial experts, authors, or investors whose philosophy matches the user's financial north star and principles.

Present and confirm as above. After selection, update `.claude/agents/cfo.md`.

---

## Section 4 — Health & Fitness

Ask:
- What does being healthy and fit mean to you — what are you working toward?
- What kinds of movement do you actually enjoy and follow through on?
- Do you have any injury history or physical tendencies to be aware of?
- Are there times of year or structural obstacles that reliably derail your fitness?
- How do you think about food — what's your setup and approach?

After confirming, write `health-fitness/philosophy.md`. Then:

**Expert selection — coach:**

Search for 3 named coaches, trainers, sports scientists, or authors whose methodology matches the user's goals and movement profile.

Present and confirm as above. After selection, update `.claude/agents/coach.md`.

---

## Section 5 — Growth

Ask:
- What does intellectual and creative growth look like for you?
- What do you read, make, or practice? What are you currently curious about?
- What gets in your way most consistently?
- Are you learning any languages? What's your relationship with them?
- Is there a creative practice or hobby you've wanted to claim as yours?

After confirming, write `growth/philosophy.md`. Then:

**Expert selection — growth-director:**

Search for 3 named authors, educators, creators, or thinkers whose approach to learning and creative development matches the user's goals and blockers.

Present and confirm as above. After selection, update `.claude/agents/growth-director.md`.

---

## Section 6 — Social & Life

Ask:
- How would you describe your social life — what do you have, and what are you building toward?
- Are you introverted or extroverted? How do you make and maintain friendships?
- What's your relationship situation right now?
- What pulls you away from the social life you want?
- What does a genuinely good day off look like for you?

After confirming, write `social-life/philosophy.md`. Then:

**Expert selection — social-advisor:**

Search for 3 named researchers, authors, or practitioners in relationship psychology, social dynamics, or human connection whose frameworks match the user's wiring and social goals.

Present and confirm as above. After selection, update `.claude/agents/social-advisor.md`.

---

## Section 7 — Reference Cards (Optional)

Reference cards are factual snapshots your advisors read for specific context. They're separate from philosophy (your values) and memory (your history) — they're the current facts your advisors need to give concrete advice.

Ask:

> "There are four optional reference cards that give your advisors richer context. They take about 5 minutes to set up and make a meaningful difference in the specificity of advice you get. Want to set them up now, or skip and fill them in later?"

If the user wants to proceed, work through each card with a few targeted questions. Write in their voice, keep it factual and current.

**Professional profile** (`professional/other/profile.md`):
- What's your current role and what do you actually do day-to-day?
- What are you genuinely strong at — specifically?
- What are you actively building or working on outside your day job?
- Anything open — job search, applications, skills in progress?

**Financial profile** (`financial/other/profile.md`):
- Current income and any expected changes?
- Rough net worth and how it's split — liquid, retirement, other?
- What accounts do you have and what are they for?
- Any open financial items — rollovers, consolidations, things unresolved?

**Cooking & nutrition** (`health-fitness/other/cooking.md`):
- What's your kitchen setup — fridge size, budget, primary store?
- How many meals do you need to cover each week?
- How much time are you willing to spend cooking? Any dietary restrictions?
- Anything you already make regularly that works well?

**Reading** (`growth/other/reading.md`):
- What are you currently reading?
- What's next on your list?
- What kinds of books actually move you — and what do you avoid?

Check the resumability of each card the same way as philosophy files — if it already contains real answers, skip it or offer to update.

---

## Section 8 — Daily Briefing

Ask:
- What email address should the morning briefing go to?
- What time would you like to receive it?

Tell the user:

> "After setup completes, run `scripts/install-briefing.sh` to configure the scheduler. It will ask for your Gmail app password to send the briefing — this is stored in your system keychain, never in any file."

Write the email and time to a config block at the bottom of `CLAUDE.md`:

```
## Briefing Config
- Email: [address]
- Time: [time]
```

---

## Finishing Up

After all sections are complete, confirm:

1. `CLAUDE.md` is personalized
2. All five philosophy files are populated with real answers
3. All five agent `## Expert Framework` sections are filled in
4. Any reference cards the user opted into are populated
5. Briefing config is written to `CLAUDE.md`

Then tell the user:

> "Setup is complete. Three things to do next:
>
> 1. Run `scripts/install-briefing.sh` to activate your morning briefing
> 2. Run `/year` to set your annual goals — then `/month` and `/week` to cascade them down
> 3. You're live — ask about any domain and the right advisor will engage with full context on you
>
> You can return to `/setup` at any time to update any section, recalibrate an expert framework, or fill in a reference card you skipped."
