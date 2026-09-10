Map of OCR prompts in `OCR/`. Send the prompt, agent replies `understand.`, then send the image.

| Prompt | Use for | Guesses? | Output |
|---|---|---|---|
| [[OCR]] | Clean printed text, literal transcription | No | Text + LaTeX |
| [[OCR-LaTeX]] | Math-heavy pages, readable formulas | No | Unicode math + LaTeX blocks |
| [[OCR-Smart]] | Blurry scans, cut edges, ambiguous glyphs | Yes, marked `⟪⟫` | Text + LaTeX + confidence markers |
| [[OCR-Markdown]] | Textbooks, notes, tables | Markup only | Markdown |
| [[OCR-Layout]] | Multi-column pages, margins, diagrams | No | Text + region markers |
| [[OCR-Handwriting]] | Notebooks, drafts, whiteboards | Yes, marked `[?a\|b]` | Text + edit artifacts |

Notes:
- Don't OCR and solve in one pass — transcribe first, solve separately.
- Gappy output from [[OCR]] → rerun the image through [[OCR-Smart]].
- One image per request. Cropping beats switching prompts.
