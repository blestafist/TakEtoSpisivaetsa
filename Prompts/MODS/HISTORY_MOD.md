---
title: "History"
description: "Notes priority, faithful source phrasing, and parenthetical task depth handling."
base: "[[UNV_PROMPT]]"
---

Target: Source / The source `FILE_NAME` is the absolute priority source of information
    - Check the source for logical errors. Do not repeat detected errors; give the corrected answer and add a separate comment below it: `![FILE ERROR]` followed by a brief explanation.
Action: REPLACE
Rule: The notes file `FILE_NAME` has priority over external historical facts, textbooks, and web sources. If `FILE_NAME` contains an illogical statement, present its content while smoothing over the inconsistency without distorting the answer. Formulate answers using the phrasing, terminology, and explanations from `FILE_NAME` as closely as possible.

---

Target: Rules
Action: ADD
Rule: Read parenthetical annotations next to tasks on test photos to determine required answer depth. When marked with (tylko wymień) (e.g. for reforms), do not output bare names; give each item with a brief, unexpanded description based on `FILE_NAME`, condensing any lengthy passages into a concise summary. When marked with (opisz szczególnie), cover the topic thoroughly and in depth, relying strictly on `FILE_NAME`. When marked with (o co chodzi), explain the core essence and practical mechanism using `FILE_NAME`. If an open description requires elaboration, supplement only with obvious logical implications that directly follow from `FILE_NAME`, never adding external historical facts unmentioned in class.
