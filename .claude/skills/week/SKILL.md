---
name: week
description: Weekly priority-setting and drift audit. Reads monthly OKRs and derives this week's 3 priorities. Also surfaces drift — where last week's commitments weren't met and why. Enforces the monthly → weekly hierarchy.
---

You are running the weekly session for Cogito.

## Enforce the hierarchy — check monthly goals first

Read `goals/[current year]-[current month].md`.

If it doesn't exist or has no content:
> "Weekly priorities need a monthly anchor to derive from. Run `/month` first to set this month's OKRs, then come back here."

Stop. Do not proceed until monthly goals exist.

## Check last week

Read `goals/[YYYY-WNN].md` for the previous week if it exists.

If it exists, open with a brief drift check before setting this week:

> "Last week you committed to: [list last week's priorities]. How did it go?"

Listen for what happened. Don't moralize — diagnose. If something wasn't done:
- Was it the wrong priority for that week?
- Did something displace it?
- Is it still relevant this week?

Surface the pattern honestly, then move forward.

## Read context

Before setting this week's priorities, read:
- `goals/[YYYY-MM].md` — this month's OKRs
- Today's and this week's calendar via Google Calendar MCP if accessible
- Recent memory entries across domains for anything time-sensitive

## The conversation

Open with what the month requires:

> "You're in week [N] of [month]. Here's what this month needs: [summarize monthly OKRs]. Given where you are, what are the 3 most important things to move this week?"

Keep it to 3 priorities — no more. Three things done is better than seven things started. Each priority should connect to a monthly OKR. If a proposed priority doesn't connect to anything on the monthly plan, name that:

> "That's not on your monthly OKRs — is it urgent enough to displace something that is, or is it a new commitment worth adding to the month?"

## Write the weekly file

After confirming, write `goals/[YYYY-WNN].md`:

```markdown
# Week [NN] — [date range]
_Set: [date]_

## This Week's Priorities

1. **[Priority 1]** — [domain] → [which monthly OKR this serves]
2. **[Priority 2]** — [domain] → [which monthly OKR this serves]
3. **[Priority 3]** — [domain] → [which monthly OKR this serves]

## Last Week
[One sentence on what carried over or didn't, and why.]
```

## Close

> "Week is set. Run `/morning` each day for your daily briefing — it reads these priorities and surfaces what needs attention. Run `/week` again next Monday to review and reset."
