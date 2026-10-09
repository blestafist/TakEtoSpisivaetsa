#!/usr/bin/env python3
"""Build the standalone GPTML from the editable topic files; --check verifies freshness."""

from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT.parent / "BIO_GENETYKA_MOLEKULARNA_GPTML.md"
PARTS = (
    "BIO_GENETYKA_SOLVER_PROMPT.md",
    "01_GEN_DNA_RNA_GPTML.md",
    "02_KOD_GENETYCZNY_GPTML.md",
    "03_EKSPRESJA_GENOW_GPTML.md",
)
HEADER = """# Biologia — genetyka molekularna — GPTML

Samodzielny materiał do rozwiązywania zadań po polsku. Zakres: trzy tematy z `bio.pdf`,
19 stron skanu odpowiadających stronom podręcznika 6–24. Zawiera teorię, algorytmy,
pełną tabelę standardowego kodu, przykłady, pułapki oraz odpowiedzi do wszystkich
10 poleceń kontrolnych i 12 zadań końcowych.

Kolejność: instrukcja solvera; 1.1 gen, DNA i RNA; 1.2 kod genetyczny; 1.3 ekspresja genów.
Materiał nie obejmuje krzyżówek Mendla ani dalszych rozdziałów spoza skanu.
Szkolne uproszczenia zostały doprecyzowane w oznaczonych miejscach.

Plik jest składany automatycznie z plików w `Genetyka_molekularna/`.
Aktualizuj pliki tematyczne, następnie uruchom `python3 build_gptml.py`.
Do pracy z modelem wystarczy treść tego pliku; instrukcja solvera jest już dołączona.
"""


def demote_headings(content: str) -> str:
    """Add one heading level outside fenced code, preserving all other text."""
    lines = []
    fenced = False
    for line in content.splitlines():
        if line.startswith("```"):
            fenced = not fenced
        if not fenced and re.match(r"^#{1,5} ", line):
            line = "#" + line
        lines.append(line)
    return "\n".join(lines)


def build() -> str:
    sections = [HEADER.rstrip()]
    for name in PARTS:
        content = (ROOT / name).read_text(encoding="utf-8").strip()
        sections.append(demote_headings(content))
    return "\n\n---\n\n".join(sections) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Do not write; fail if output is stale")
    args = parser.parse_args()
    expected = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print("Combined GPTML is missing or stale; run python3 build_gptml.py", file=sys.stderr)
            return 1
        print("Combined GPTML matches all source files.")
        return 0
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Built {OUTPUT.name} from {len(PARTS)} source files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
