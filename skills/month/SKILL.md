---
name: month
description: Monthly OKR-setting session. Reads yearly goals and translates them into this month's objectives and key results. Enforces the yearly → monthly hierarchy.
---

You are running the monthly goal-setting session for Cogito.

## Enforce the hierarchy — check yearly goals first

Read `goals/[current year].md`.

If it doesn't exist or has no content:
> "Monthly goals can't be set without a yearly anchor — otherwise there's nothing to derive them from. Run `/year` first to set your annual objectives, then come back here."

Stop. Do not proceed until yearly goals exist.

## Check for existing monthly goals

Check if `goals/[YYYY-MM].md` already exists and has content.

If it does:
> "You already have goals set for [month]. Here's what you committed to: [summarize]. Want to review and adjust, or start fresh?"

## Read context

Before the conversation, read:
- `goals/[current year].md` — the yearly anchor
- All five `*/memory.md` files — recent context across domains
- Current month's calendar if accessible via Google Calendar MCP

Use this to come in informed. You know what the user committed to for the year and what's been happening recently. Don't ask them to re-explain.

## The conversation

Open with a grounding summary:

> "Here's what you're working toward this year: [brief summary of yearly objectives]. This month's OKRs should move the needle on at least 2-3 of these. Let's figure out what's realistic given where you are right now."

For each yearly objective, ask:
- What's the most important thing to move on this specifically in [month]?
- What would meaningful progress look like by the end of the month?
- Is anything blocking this that needs to be addressed first?

Also surface anything from memory that's relevant — an open item, a stalled goal, something that deserves attention this month even if it's not a yearly objective.

Push for 3-5 monthly OKRs total. Each needs:
- A clear objective (what you're doing)
- A measurable key result (how you'll know you did it)
- A domain label

## Write the monthly goals file

After confirming, write `goals/[YYYY-MM].md`:

```markdown
# [Month YYYY] — Monthly OKRs
_Set: [date]_

## OKRs

### [Objective 1] — [domain]
**Key Result:** [specific, measurable outcome by month-end]

### [Objective 2] — [domain]
**Key Result:** [specific, measurable outcome by month-end]

[...]

## Yearly Goals Progress
[Brief status on each yearly objective — on track, behind, not started, complete.]
```

## Close

> "Month is set. Run `/week` at the start of each week to translate these into weekly priorities. Run `/month` again anytime to adjust — goals aren't contracts, but changes should be deliberate."
