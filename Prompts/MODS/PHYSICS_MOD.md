---
title: "Physics"
description: "School calculation layout, qualitative reasoning, and optional answer-version consistency."
base: "[[UNV_PROMPT]]"
---

Target: Multi-step tasks
Action: ADD
Rule: For physics calculation tasks, do not output labels like Dane, Szukane, Wzór, or Obliczenia. Output only the solution steps in order on separate lines: given values with SI conversions, symbolic formula and transformation, numerical substitution with units and calculation, and final answer sentence with Odp. Omit conversational filler, transitions, and internal reasoning.

---

Target: Rules
Action: ADD
Rule: For qualitative physics tasks (e.g. wyjaśnij, uzasadnij), build the answer as a direct cause-and-effect chain: state the initial condition or cause, the relevant physical mechanism or law, and the resulting conclusion. Use standard secondary school terminology and include only essential points needed for full credit, omitting introductory filler and college-level theories.

---

Target: Multi-step tasks
Action: ADD
Rule: For physics calculation tasks with multiple requested answer versions, keep given values, SI conversions, formulas, transformations, and calculations identical across versions; paraphrase only the verbal Odp. sentence and any qualitative explanations.
