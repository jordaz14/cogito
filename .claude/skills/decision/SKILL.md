---
name: decision
description: Structured decision framework for significant choices. Works through framing, philosophy check, options inventory, principles test, trade-off analysis, pre-mortem, and recommendation. Use when the user is weighing an important decision.
argument-hint: [decision topic]
---

You are running a structured decision session for: $ARGUMENTS

Work through each step in order. Do not skip any step. For significant decisions, depth matters more than speed.

---

**Step 1: Frame the decision**
What exactly needs to be decided? What's the decision horizon (by when)? Who else is affected?
Restate the decision in one crisp sentence to confirm alignment before proceeding.

**Step 2: Read relevant philosophy**
Identify which life domains this decision touches. Read the corresponding philosophy file(s):
- Professional → `professional/philosophy.md`
- Financial → `financial/philosophy.md`
- Health & Fitness → `health-fitness/philosophy.md`
- Growth → `growth/philosophy.md`
- Social & Life → `social-life/philosophy.md`

Summarize: which non-negotiables are relevant? Which principles apply?

**Step 3: Options inventory**
What are all the realistic options, including "do nothing" and "decide later"? List them without judgment first.

**Step 4: Principles test**
For each option: does it align with or violate any non-negotiables from Step 2? Eliminate any option that violates a non-negotiable. These are not trade-offs.

**Step 5: Trade-off analysis**
For the remaining options: what are you actually trading between them? Name the real trade-offs explicitly. Use the trade-off heuristics from the relevant philosophy file.

**Step 6: Pre-mortem**
Pick the option you're currently leaning toward. If you choose it and it fails, what's the most likely reason? What would you wish you had done differently?

**Step 7: Recommendation**
Given everything above: what do you recommend, and why? Be direct. If the answer is unclear, say what additional information would break the tie.

---

After the session, invoke `/remember` to log the outcome to the relevant domain's `memory.md`. Use the `[DECISION]` prefix to mark it:

```
**[YYYY-MM-DD] — [Domain] [DECISION]**
[What was decided, the key reasoning, and any non-negotiables that applied. 2-3 sentences max.]
```

This makes decisions discoverable in future sessions without needing a separate folder.
