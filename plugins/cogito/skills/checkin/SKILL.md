---
name: checkin
description: Daily briefing. Reads calendar, current goals, and memory files to produce a concise 3-section snapshot — Today, Goal Spotlight, and One Signal. Designed to be read in 90 seconds.
---

You are generating the user's daily briefing. This should take 90 seconds to read. Do not make it longer.

## Read these files first

- `goals/[current year].md` — yearly objectives
- `goals/[YYYY-MM].md` — this month's OKRs
- `goals/[YYYY-WNN].md` — this week's priorities
- All five `*/memory.md` files — recent context across domains
- Google Calendar — today's events and any urgent items this week

If no goal files exist, note it at the top:
> "No goals are configured yet. Run `/year` → `/month` → `/week` to set them up."

Then proceed with what's available.

## The three sections

### 1. Today

- List today's calendar events (time + title, nothing more)
- Flag one email or open item that needs action today if anything stands out — otherwise omit this line
- Keep this section to 5 lines maximum

### 2. Goal Spotlight

- Pick one monthly OKR to surface — rotate across domains day to day, don't spotlight the same one repeatedly
- State current status in one sentence: on track, behind, not started, or complete
- State one specific action that would move it today

### 3. One Signal

This is the most valuable section. Surface something the user probably hasn't thought about — a pattern, a drift, a conflict, or a connection across domains. One thing only. Examples:

- A goal that hasn't appeared in memory entries for 2+ weeks
- A calendar event that conflicts with a stated non-negotiable or priority
- A pattern across memory entries worth naming (e.g., fitness absent while work has been heavy)
- A monthly OKR with no weekly priority connected to it
- An open item from memory sitting unresolved

Be specific. A signal with no specifics is not a signal.

## Format

```
## Briefing — [Weekday, Month Day]

**Today**
[calendar events]
[one action item if relevant]

**Goal Spotlight — [domain]**
[monthly OKR name]: [status in one sentence]
→ [one specific action for today]

**One Signal**
[one specific observation — pattern, drift, conflict, or connection]
```

## Tone

Direct and brief. This is a briefing, not a report. No preamble, no summary at the end.
