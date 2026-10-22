Instructions for creating mods for UNV_PROMPT.md. This file is documentation, not a mod. Application rules are defined in UNV_PROMPT.md under Mod rules.

Name each mod TOPIC_MOD.md, e.g. MATH_MOD.md. Use a short, descriptive uppercase name with underscores; the exact suffix _MOD.md is required. Do not name an active mod MOD_TEMPLATE.md.

Start with Obsidian YAML frontmatter enclosed in --- lines: title (readable mod name), description (brief summary of changes), base ("[[UNV_PROMPT]]"). Metadata is for people, not instructions; put all behavior and conditions in entries. Quote YAML values. Do not use metadata to set priority or enable/disable a mod.

After frontmatter, write only the changes, in English. No introduction, tables, code fences, or copied base sections. Separate entries with a standalone --- line, with a blank line on each side.

Keep mods compact: short, direct sentences; one instruction per entry; no rationale, repetition, examples, or unchanged base rules outside Target. Use only necessary conditions and details; do not sacrifice precision for brevity. Keep descriptions to one short sentence.

Use plain text fields, without headings, bold, italics, or decorative lists. Preserve original formatting inside exact Target quotes. Task answers inherit the base formatting and brevity rules unless explicitly overridden: only task/version headers and the identification separator use Markdown; prefer Unicode math, use LaTeX only when needed, and fit answer lines without omitting work required for credit. Do not repeat these defaults in mods.

Each entry uses these fields:
Target: exact section title / exact complete original rule
Action: REPLACE
Rule: replacement instruction

REPLACE: quote one complete base rule in Target, without its Markdown bullet or numbering; include its nested lines. Replace only that rule, not its section.
REMOVE: use the same Target format, set Action to REMOVE, and omit Rule.
ADD: set Target to the exact section title only, Action to ADD, and Rule to the additional instruction. Do not use ADD to override an existing rule.

Use one entry per changed rule. Check related rules elsewhere; override each conflicting rule explicitly. Keep unrelated rules unchanged. Put any scope or condition inside Rule; otherwise the entry applies throughout the chat. Do not target another mod's rewritten text. If mods conflict, the user must specify their priority separately.

Example file MATH_MOD.md:
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
