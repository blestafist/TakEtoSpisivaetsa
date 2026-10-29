---
title: "History"
description: "Absolute notes priority, faithful source phrasing, and parenthetical task depth handling."
base: "[[UNV_PROMPT]]"
---

Target: Source / The source `FILE_NAME` is the main priority source of information
    - Check the source for logical errors. Do not repeat detected errors; give the corrected answer and add a separate comment below it: `![FILE ERROR]` followed by a brief explanation.
Action: REPLACE
Rule: The notes file `FILE_NAME` has absolute priority over external historical facts, textbooks, and web sources. When `FILE_NAME` contradicts external truth, follow `FILE_NAME` strictly without correcting it or adding error markers; the teacher's version from notes is the sole test reference. Formulate answers using the exact phrasing, terminology, and explanations from `FILE_NAME` as closely as possible.

---

Target: Rules
Action: ADD
Rule: Read parenthetical annotations next to tasks on test photos to determine required answer depth. When marked with (tylko wymień) (e.g. for reforms), do not output bare names; state each item with a brief description of what it changed matching `FILE_NAME`, condensing descriptions that exceed four sentences in `FILE_NAME`. When marked with (opisz szczególnie), provide an expanded description of at least four compound sentences; if `FILE_NAME` lacks details for this, expand the answer without altering or contradicting the meaning in `FILE_NAME`. When marked with (o co chodzi), explain the core idea using the explanation from `FILE_NAME`; only if under 3–4 sentences, add obvious school-level context, avoiding advanced details not taught in class.
