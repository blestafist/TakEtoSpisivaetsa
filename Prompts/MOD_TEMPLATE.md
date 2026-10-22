Instructions for creating mods for [[UNV_PROMPT]]. This file is documentation, not a mod. Application rules: UNV_PROMPT.md → Mod rules.

## File name
Use `TOPIC_MOD.md`: a short uppercase name with underscores, e.g. `MATH_MOD.md`. The exact suffix `_MOD.md` is required. `MOD_TEMPLATE.md` is reserved for this guide.

## Obsidian properties
Start with YAML frontmatter enclosed in `---` lines. Quote all values.
- `title`: readable mod name.
- `description`: one short sentence describing the changes.
- `base`: "[[UNV_PROMPT]]".

Properties are metadata for people, not instructions. Put behavior and conditions in entries, not properties. Do not set priority or activation status in metadata.

## Override entries
After frontmatter, write entries in English. Separate them with a standalone `---` line and a blank line on each side.

```text
Target: exact section title / exact complete original rule
Action: REPLACE
Rule: replacement instruction
```

- `REPLACE`: replace one complete rule, not its section.
- `REMOVE`: use the same Target format; omit Rule.
- `ADD`: Target contains only the exact section title; Rule adds an instruction without overriding existing rules.

For REPLACE/REMOVE, copy the original rule exactly, without its bullet or numbering. Include nested lines. Never target another mod's rewritten text.

## Scope and conflicts
- Use one entry per changed rule; check related rules elsewhere and override each conflict explicitly.
- Keep unrelated rules active. ADD cannot replace them implicitly.
- Put conditions in Rule; otherwise the entry applies throughout the chat.
- For conflicting mods, the user must specify priority separately.

## Brevity and formatting
- Write only changes: short, direct sentences, without rationale, repetition, or examples.
- Do not copy unchanged base rules except inside Target. Keep necessary conditions; precision comes before brevity.
- Use plain text fields in mods: no introductions, headings, tables, bold, italics, decorative lists, or code fences. Preserve formatting inside exact Target quotes.
- Task answers inherit base formatting unless explicitly overridden: only task/version headers and the identification separator use Markdown; prefer Unicode math, use LaTeX only when needed, and fit answer lines without omitting work required for credit. Do not repeat these defaults in mods.

## Example: MATH_MOD.md

Only an example. Use as a base for writing your own mods. Do not use code blocks or copy this example into your mod.

```text
---
title: "Math"
description: "LaTeX expressions and explicit root validity checks."
base: "[[UNV_PROMPT]]"
---

Target: Formatting rules / Use unicode math symbols preferrably over LaTeX formatting for mathematical expressions. Use LaTeX formatting only if unicode is not possible.
Action: REPLACE
Rule: For math tasks, use LaTeX for mathematical expressions.

---

Target: Multi-step tasks
Action: ADD
Rule: For rational, radical, and logarithmic equations, show necessary domain restrictions and reject inadmissible roots. Keep these steps concise.
```
