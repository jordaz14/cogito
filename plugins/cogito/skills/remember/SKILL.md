---
name: remember
description: Append a memory to the relevant domain's memory.md. Invoke proactively when a conversation surfaces something worth carrying into future sessions — progress updates, decisions made, expressed preferences, context that would otherwise be lost on cold start.
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
You are writing a new entry to a domain memory file.

## When to invoke this skill

- The user reaches a meaningful milestone (finished a course, ran a race, launched something, closed an open item)
- A significant decision is made in conversation that future sessions should know about
- The user expresses a preference about how to work with them that isn't in the philosophy files
- New context emerges that updates the picture of who they are or where they stand
- Something from the conversation would visibly improve cold-start orientation next session

Do NOT invoke for ephemeral task details, things already in the philosophy files, or anything that will be irrelevant within a week.

## How to write the entry

1. Identify the domain the memory belongs to: `professional`, `financial`, `health-fitness`, `growth`, or `social-life`
2. Read that domain's `memory.md` first — check if an existing entry should be updated rather than duplicated
3. Write a new entry in this format:

```
**[YYYY-MM-DD] — [Domain or topic]**
[1-3 sentences. Specific and concrete. What changed, what was decided, what should be known next session.]
```

4. Append it to `[domain]/memory.md` below the existing entries, replacing the `_No entries yet._` placeholder if this is the first entry
5. Keep entries tight — a memory that requires a paragraph to explain probably belongs in the philosophy file, not here

## Domain memory file paths

- `professional/memory.md`
- `financial/memory.md`
- `health-fitness/memory.md`
- `growth/memory.md`
- `social-life/memory.md`

If a memory clearly spans multiple domains, write it to the most relevant one.
