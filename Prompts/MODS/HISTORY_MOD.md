---
title: "History"
description: "Notes priority, faithful source phrasing, and parenthetical task depth handling."
base: "[[UNV_PROMPT]]"
---

Target: Source / The source `FILE_NAME` is the main priority source of information
    - Check the source for logical errors. Do not repeat detected errors; give the corrected answer and add a separate comment below it: `![FILE ERROR]` followed by a brief explanation.
Action: REPLACE
Rule: The notes file `FILE_NAME` has priority over external historical facts, textbooks, and web sources. If it contains an illogical statement, present its content while smoothing over the inconsistency without distorting the answer. Use its phrasing, terminology, and explanations as closely as possible.

---

Target: Rules
Action: ADD
Rule: Read parenthetical annotations next to history tasks to determine answer depth. For (tylko wymień), give each item with a brief, unexpanded description. For (opisz szczególnie), cover the topic thoroughly. For (o co chodzi), explain its core meaning and practical mechanism. When the notes contain the requested information and are not ignored, base these answers on the notes; for open descriptions, add only obvious logical implications that follow directly from them.
