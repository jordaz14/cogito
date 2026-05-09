---
name: year
description: Yearly goal-setting session. Reads philosophy files to understand the user's long-term outlook, then helps set 3-5 annual objectives with measurable key results. Parent of all monthly and weekly goals.
---
## Data Directory

Before any file operations, resolve the Cogito data directory:

1. **In Claude Code**: use the current working directory — all relative paths resolve from there automatically.
2. **In Cowork or any context without an implicit project directory**:
   - Check if a workspace folder is already connected.
   - If not, call `mcp__cowork__request_cowork_directory` to prompt the user to select their Cogito data folder.
   - Treat all relative file paths in this skill (`professional/philosophy.md`, `CLAUDE.md`, `goals/`, etc.) as relative to that folder.

Do not read from or write to the plugin installation directory. All user data lives in their chosen data directory.

---
You are running the yearly goal-setting session for Cogito.

## Check for existing yearly goals

First, check if `goals/[current year].md` already exists and has content.

If it does:
> "You already have yearly goals set for [year]. Here's what you committed to: [summarize]. Want to review and adjust, or start fresh?"

If it doesn't, proceed with setup.

## Read philosophy files first

Before asking anything, read all five philosophy files:
- `professional/philosophy.md`
- `financial/philosophy.md`
- `health-fitness/philosophy.md`
- `growth/philosophy.md`
- `social-life/philosophy.md`

Also read `goals/[current year].md` if it exists for any prior context.

Use these to ground the conversation — you already know what the user values, what they're building toward, and what their non-negotiables are. Don't ask them to repeat their philosophy. Ask them to extend it into concrete commitments for the year.

## The conversation

Open with a brief orientation:

> "Yearly goals are the anchor for everything else. Monthly OKRs and weekly priorities derive from these — so getting this right matters. We're setting 3-5 objectives across your five domains. Each objective needs a measurable key result so we know at year-end whether you hit it.
>
> Let's go domain by domain. I'll propose a direction based on your philosophy — push back or redirect wherever it doesn't fit."

For each domain, propose a draft objective based on what you read in the philosophy file. Then ask:
- Does this capture what actually matters to you this year?
- What would it look like to clearly succeed at this by December?
- Is there anything more important in this domain that isn't captured here?

Push for specificity. "Get better at X" is not an objective. "Ship X by Q3" or "reach X metric by year-end" is.

Aim for 3-5 objectives total across all domains — not one per domain by default. Some domains may have none this year. That's fine. Focus beats coverage.

## Write the yearly goals file

After confirming all objectives, write `goals/[YYYY].md`:

```markdown
# [YYYY] — Yearly Goals
_Set: [date]_

## Objectives

### [Objective 1 — domain]
**Key Result:** [specific, measurable outcome]

### [Objective 2 — domain]
**Key Result:** [specific, measurable outcome]

[...]

## What This Year Is About
[2-3 sentences in the user's voice on the theme or intention behind these goals — not a list, a framing.]
```

## Close

> "Yearly goals are set. Run `/month` to translate these into this month's OKRs — monthly goals can't be set without the yearly anchor. Run `/year` again anytime to revisit these."
