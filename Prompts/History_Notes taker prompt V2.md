# History Lessons → Full Information (V2)

## 1. Task

Turn history lesson recordings into a complete record of the information the teacher gave. It is not a summary, and it is not a copy of the transcript.

Principle: every fact stays, every word that carries no fact goes. The most important content is kept word for word, the rest as short facts, and stories and talk are dropped.

The teacher's tests ask about small details: dates, names, places, numbers, causes, consequences, definitions, complete lists. A missing detail, or one changed by paraphrasing, costs me points.

The output is a source file that another AI will read later (to quiz me, make flashcards, etc.). It must be complete, exact and consistently formatted. It does not need to read nicely for a human.

The file contains only final, resolved information. Every doubt is resolved before the file is written (section 4). The file never contains question marks, conflicts, gaps or "maybe".

## 2. Input

Detect everything yourself. A batch of lessons, each with:
- `.srt`: the full Whisper transcript. Complete and usually accurate.
- `.md`: my timecodes of important moments, sometimes with short labels.

Rules:
1. Pair the files by name, otherwise by order or content.
2. Work out the topic, the language and the number of lessons yourself.
3. Accept any timecode format.

Timecodes are approximate. They mark roughly where something important was said, before or after the timecode.
1. Search ±3 min around the timecode in both directions. If nothing fits, widen to ±5 min.
2. Pick the passage that matches the label or topic. If there is no label, pick the most substantive content in that window.
3. Take the whole passage, from where the topic starts to where it ends, not just the sentence closest to the timecode.
4. If two passages fit equally well, keep both or ask me.

Passages at my timecodes are priority 1 (section 3).

## 3. Priorities

### Priority 1: word for word
What:
- reforms;
- lists: causes, effects, goals, points of a treaty/law/constitution, demands;
- definitions;
- anything the teacher stresses (see "Stress signals");
- passages at my timecodes.

How: every sentence of hers stays, in her words and in her order, including explanations ("czyli…", "to znaczy…"), examples and side details. Remove only fillers, stutters and word-for-word repeats. Add punctuation.

Never: summarise, merge, shorten, rephrase.

### Priority 2: short facts
What: everything else factual: the course of events, context, background, who did what, causes and effects outside of lists.

How: one bullet per fact, in short note form. Shorten only by deleting words, never by rewriting: what remains is still her wording and her terms. Every date, name, place, number, cause and effect stays.

Never: synonyms, "in your own words", generalising ("różne reformy" instead of the actual reforms).

### Priority 3: drop
What:
- fillers and tics: "yyy", "no więc", "jakby", "tak?", "prawda?", "słuchajcie", "w sumie", "generalnie";
- false starts, stutters and repeats. If she says the same fact twice, write it once, but keep every detail from both versions;
- classroom talk with no facts: "pamiętacie, mówiłam wam", "teraz przejdziemy do", rhetorical questions she then answers (keep the answer);
- questions to the class: keep only the correct answer she confirms, as a fact. Drop wrong guesses from students;
- anecdotes, fun stories, digressions, anything "na marginesie";
- recaps of the previous lesson and summaries at the end: add only new details, at the place where that topic first appears;
- off-topic: discipline, attendance, jokes, small talk, technical chatter (microphone, board, doors).

Exception: if dropped content contains a date, name or number not mentioned anywhere else, keep that one fact as a priority 2 bullet.

### Borderline cases
1. When in doubt, go one priority up (3 → 2, 2 → 1).
2. Only the reform, list or definition itself is priority 1, not the whole story around it.
3. Before dropping a sentence, ask: "Could this be a test question?" If yes, it stays as at least priority 2.

### Stress signals
Always priority 1, marked `[WAŻNE]` at the start of the bullet.
- She says it's important: "to jest ważne", "to jest kluczowe", "zwróćcie uwagę", "musicie to znać", "pamiętajcie".
- She mentions the test: "to będzie na sprawdzianie / kartkówce", "o to będę pytać", "to się często pojawia".
- She dictates or writes it down: "zapiszcie", "zapisuję na tablicy", dictating slowly word by word.
- She repeats the same thing several times in the lesson. Write it once and mark it.

Don't write out the signal phrase itself. The marker replaces it.

### Lists
Every single point matters. One missing point means lost points on the test.
1. Lists are always priority 1: every point with the teacher's full explanation (who, when, what it changed, why), in her words.
2. Never shorten, merge or summarise a list. Each point is a separate item, even if two points look similar.
3. Lists are often spread out: the teacher gives a point, digresses, then continues ("a po drugie…", "kolejna reforma…", "i jeszcze…"). Collect all points of a list, even if they come minutes apart.
4. Number every list (1., 2., 3.) and put the number of points in the heading: `Reformy (5)`.
5. If the teacher announced a number ("trzy przyczyny") and you found a different number of points, that's a gap: resolve it (section 4) before writing.

### Never
1. Change any date, number, name or term, except by the rules in section 4.
2. Change the order of facts inside a passage.
3. Add anything she didn't say, except what I approve in my answers (section 4, step 3).

### Example: priority 1 (a reform she stresses)

Transcript:
```
No i teraz, słuchajcie, reforma monetarna, to będzie na sprawdzianie. On, jakby, przeprowadził reformę monetarną, czyli wprowadził, yyy, grosz krakowski. Grosz krakowski. I to było mniej więcej w 1338, może trochę później, historycy się kłócą. No więc to było po to, żeby ujednolicić pieniądz w kraju, bo wcześniej każda dzielnica miała swój, no i to było strasznie niewygodne dla kupców, bo musieli wymieniać.
```

Output:
```
- [WAŻNE] Reforma monetarna: przeprowadził reformę monetarną, czyli wprowadził grosz krakowski.
  - To było mniej więcej w 1338, może trochę później, historycy się kłócą.
  - To było po to, żeby ujednolicić pieniądz w kraju, bo wcześniej każda dzielnica miała swój, i to było strasznie niewygodne dla kupców, bo musieli wymieniać.
```

Every sentence stayed in her words, including "czyli…" and the detail about the merchants. "To będzie na sprawdzianie" became `[WAŻNE]`. Only fillers and the repeated "Grosz krakowski" went. "Mniej więcej… historycy się kłócą" is the teacher's own content, not uncertainty in the transcript, so it stays.

### Example: priority 2 and 3 (background with an anecdote)

Transcript:
```
No i teraz tak, Kazimierz Wielki, tak? Ostatni z Piastów, no, na tronie, bo potem już byli inni, ale o tym za tydzień. Jego ojciec to był Władysław Łokietek, o nim mówiłam wam na poprzedniej lekcji, pamiętacie? No i on, Kazimierz, objął tron w 1333 roku, jak ojciec zmarł. I wiecie, jest taka historia, że on podobno był strasznie kochliwy, miał mnóstwo romansów, no, ale to tak na marginesie.
```

Output:
```
- Kazimierz Wielki: ostatni z Piastów na tronie.
- Ojciec: Władysław Łokietek.
- Objął tron w 1333, jak ojciec zmarł.
```

The facts stayed, in her words, as short notes. "Ale o tym za tydzień", "mówiłam wam, pamiętacie?" and the anecdote "na marginesie" went.

## 4. Correctness: resolve everything before writing

The work has two phases:
- Phase 1: find every doubt and resolve it, by yourself (steps 1–2) or by asking me (step 3).
- Phase 2: write the file, with every decision already applied.

Default: trust the transcript. Whisper is accurate on these recordings. Raise a doubt only when there is concrete evidence (the steps below), never just because a word looks unusual.

### Step 1: resolve inside the transcript
Apply the first rule that fits. Log every change in the report (section 7).

1. Self-correction. The teacher says something and corrects it right away ("nie, przepraszam", "znaczy", "pomyliłam się", "właściwie", "sorry"), or a student corrects her and she agrees. The corrected version wins.
2. My label. If my label in the `.md` file spells a name or term, use my spelling.
3. Same thing elsewhere. If a name or term appears clearly and consistently elsewhere in the batch, and once in a different form, use the consistent form.
4. Obvious mishearing of a name or term. The transcribed word doesn't exist or makes the sentence nonsense, AND it sounds almost the same as exactly one well-known name or term that fits the context ("Pił suski" → "Piłsudski"). Fix it. Never for dates or numbers.
5. Teacher contradicts herself (no correction, e.g. 1791 at 10:20 and 1792 at 31:05). Pick the version she dictated, wrote down or stressed. If none, and exactly one version matches standard sources, pick that one. Otherwise go to step 3.
6. Whisper hallucinations. Ignore looping lines and phrases that appear during silence ("Napisy stworzone przez społeczność Amara.org", "Dziękuję za uwagę" out of context, etc.).

Example of rule 1:
```
Pokój toruński, to był rok 1456, nie, przepraszam, 1466. Tysiąc czterysta sześćdziesiąt sześć.
```
In the file: `- Pokój toruński: 1466.` In the report: `| L1 | 14:05 | 1456 | 1466 |`

### Step 2: check every fact against your knowledge
For every date, number, name and key fact in priority 1 and 2, check whether it matches standard sources (school textbooks, encyclopedias).

- If it matches: nothing to do.
- If it differs: it goes to step 3 as a question. Include the sound test:
  - write both versions as spoken Polish words, e.g. 1791 = "tysiąc siedemset dziewięćdziesiąt jeden", 1792 = "tysiąc siedemset dziewięćdziesiąt dwa";
  - "brzmi podobnie": the two could be confused by ear, so it may be a mishearing;
  - "brzmi inaczej": Whisper almost certainly heard it right, so the teacher really said it.
- Ignore differences that don't change a fact: spelling conventions, Polish vs Latin form of a name, rounding the teacher marks as approximate ("około").

Your own knowledge never goes into the file by itself. It only produces questions.

### Step 3: ask me about everything still open
Send ONE message with numbered questions BEFORE writing the file. Group them by type. Each question has:
- lesson and timecode, so I can re-listen;
- the transcript text;
- the problem in one line (for step 2 items: the source version and the sound test);
- options, with the default marked `(domyślnie)`.

Types and their default options:
1. Teacher vs sources (from step 2).
   `[L2 14:05] „Konstytucja 3 maja 1792". Źródła: 1791. Brzmi podobnie. → A) 1791 (domyślnie, jeśli brzmi podobnie) / B) 1792, tak powiedziała (domyślnie, jeśli brzmi inaczej)`
2. Unresolved teacher contradiction (from step 1, rule 5).
   `[L1 10:20 i 31:05] Raz 1791, raz 1792. Źródła: 1791. → A) 1791 (domyślnie) / B) 1792`
3. Unclear word, name or number that no rule in step 1 settles.
   `[L3 22:40] „hetman Żółkowski". → A) Żółkiewski (domyślnie) / B) zostawić`
4. Gap: an inaudible or garbled passage, or a list shorter than she announced.
   `[L2 33:10] Zapowiedziała 3 skutki, podała 2. → A) uzupełnij ze źródeł (domyślnie) / B) podam sam / C) zostaw 2`
5. Other doubts: file pairing, a timecode with no match or two matches.

Rules:
1. Don't ask about things step 1 already settled.
2. I can answer briefly, e.g. "1B, 3: Żółkiewski, reszta domyślnie". Apply exactly what I chose, and the default for everything I didn't mention.
3. Only after my answer, write the file.
4. If there are no open questions, write the file right away.

### After the answers
- Everything goes into the file as plain, final text. No markers, no alternatives, no "według źródeł".
- Content filled in from sources (option "uzupełnij ze źródeł") also goes in as plain text, in the place where it belongs.
- Every decision is logged in the report, so I can trace it. The report is a separate output (section 7), never part of the information file.

## 5. Completeness

1. Go through each transcript in order, in blocks of about 5 minutes. Every block with facts must end up in the file, or in "Pominięte fragmenty" in the report with a reason.
2. If the batch is too long to process fully in one answer, say so and do one lesson per answer. Never skim.
3. Don't aim for a length. The output gets shorter only by dropping priority 3, writing priority 2 as short notes, and writing each thing once. Never shorten priority 1 to save space.

## 6. Output format: the information file

### General
1. Language: Polish, always (file, report, questions).
2. Plain Markdown: headings, bullets, numbered lists, tables. No emojis, no bold, no highlights, no callouts, no decorative symbols.
3. The only markers allowed are `[WAŻNE]` and `[TC 14:05]`, always written exactly like this.
4. One fact or one sentence of hers per bullet. Sub-bullets for details of the bullet above.
5. Write each thing only once:
   - definitions only in "Definicje"; in the lesson text write `Liberum veto (zob. Definicje)`;
   - stressed items only in the lesson text; "Wskazówki nauczyciela" only points to them;
   - facts from recaps are merged into the first place where the topic appears.

### Structure
Output exactly these sections, in this order:

```
# <Przedmiot>: <temat> (lekcje <pierwsza>–<ostatnia>)

## Legenda
- [WAŻNE]: nauczycielka podkreśliła, że to ważne / będzie na sprawdzianie / kazała zapisać.
- [TC 14:05]: fragment przy timecodzie ucznia.
- (n) w nagłówku wyliczenia: liczba punktów.

## Lekcja 1 (<data, jeśli padła>)
### <Temat> (12:30–18:40)
- ...
### <Temat> (18:40–25:10)
- ...

## Lekcja 2 (...)
...

## Definicje
- <Termin> (L1 12:30): <definicja, słowo w słowo>

## Chronologia
| data | wydarzenie |
| --- | --- |

## Wskazówki nauczyciela i sprawdzian
### Podkreślone
- L1 › <Temat>: <czego dotyczy>
### Organizacja
- <terminy sprawdzianów i zakres, zadania domowe, terminy, materiały, w całości>
```

Rules for the structure:
1. Topic subsections follow the order of the lesson, each with its time range.
2. `[TC 14:05]` goes at the end of the first bullet of a passage at my timecode.

### File name
`<Przedmiot>_<Temat-lub-okres>_lekcje-<pierwsza>-<ostatnia>.md`, e.g. `Historia_Rewolucja-Francuska_lekcje-1-3.md`

## 7. Output format: the report

A separate output, never inside the information file: a second file `<same name>_raport.md`, or, if you can't create files, a second code block after the file. Include only subsections that have entries.

```
# Raport: <same title>

## Autopoprawki nauczyciela
| lekcja | timecode | najpierw | poprawiła na |
| --- | --- | --- | --- |

## Poprawki transkrypcji
| lekcja | timecode | w transkrypcji | w pliku | reguła (etykieta / to samo w 23:10 / znana nazwa) |
| --- | --- | --- | --- | --- |

## Rozstrzygnięte sprzeczności
| lekcja | timecode'y | wersje | wybrano | dlaczego (podyktowała / podkreśliła / zgodne ze źródłami) |
| --- | --- | --- | --- | --- |

## Moje odpowiedzi
| nr | lekcja | timecode | pytanie | wybrano |
| --- | --- | --- | --- | --- |

## Uzupełnione ze źródeł
| lekcja | gdzie w pliku | co dodano |
| --- | --- | --- |

## Pominięte fragmenty
| lekcja | zakres czasu | powód |
| --- | --- | --- |
```

"Pominięte fragmenty" lists only stretches longer than about 1 min.

## 8. Process

1. Pair the files and locate every timecode (search before and after it).
2. Read each transcript block by block. Note stress signals, reforms, lists, definitions, self-corrections and anything that needs checking.
3. Resolve what you can (section 4, steps 1–2).
4. If anything is still open, send the questions and STOP until I answer.
5. Write the information file and the report.
6. Check:
   - every priority 1 item (reforms, lists, definitions, `[WAŻNE]` items, timecode passages) is word for word: compare it sentence by sentence with the transcript;
   - every stress signal is marked `[WAŻNE]` and has a pointer in "Wskazówki";
   - every list has its count in the heading, no point merged or dropped (re-read the transcript for each list);
   - priority 2: every fact kept, in her words, as short notes;
   - no anecdotes, classroom talk, fillers or recaps without new information;
   - each thing written only once;
   - every block is in the file or in "Pominięte fragmenty";
   - every decision and my answers are applied, and each one is logged in the report;
   - the file contains no uncertainty: no "?", no alternatives, no markers other than `[WAŻNE]` and `[TC]`;
   - no emojis, no bold, everything in Polish.
7. Output the information file, then the report.

## Appendix: Audit prompt

Paste into a NEW chat with the information file, the report and the `.srt` files:

```text
Porównaj załączony plik z informacjami z transkrypcjami. Raport opisuje wszystkie świadome zmiany (autopoprawki, poprawki transkrypcji, rozstrzygnięcia, uzupełnienia ze źródeł). Nie przepisuj pliku. Wypisz tylko:
1. Fakty z transkrypcji, których brakuje w pliku (daty, nazwiska, miejsca, liczby, przyczyny, skutki, elementy wyliczeń, definicje), z timecode'em.
2. Reformy, wyliczenia, definicje i fragmenty oznaczone [WAŻNE] lub [TC], w których cokolwiek zostało skrócone, pominięte lub ujęte innymi słowami niż w transkrypcji (nawet jedno zdanie, wyjaśnienie „czyli…" czy przykład). Porównaj zdanie po zdaniu. Podaj oryginał i wersję z pliku.
3. Miejsca, gdzie nauczycielka podkreśliła wagę („ważne", „będzie na sprawdzianie", „zapiszcie", „pamiętajcie", dyktowanie, wielokrotne powtarzanie), a w pliku nie ma [WAŻNE].
4. Wyliczenia, w których brakuje choć jednego punktu, punkty zostały połączone, albo liczba w nagłówku nie zgadza się z liczbą punktów.
5. Miejsca, gdzie nauczycielka się poprawiła, a w pliku jest pierwsza (błędna) wersja.
6. Pozostałe miejsca, gdzie słowa nauczycielki sparafrazowano albo usunięto zastrzeżenia („około", „prawdopodobnie", „głównie" itp.).
7. Daty, liczby, nazwy i twierdzenia, które w pliku różnią się od transkrypcji albo w niej nie występują, a nie są opisane w raporcie.
8. Daty, liczby i nazwy w pliku, które są niezgodne ze standardowymi źródłami, a nie są opisane w raporcie (pytanie do ucznia lub rozstrzygnięcie).
9. Niepewności w pliku: znaki zapytania, alternatywne wersje, „może", „według źródeł", znaczniki inne niż [WAŻNE] i [TC].
10. Anegdoty, wypełniacze, powtórzenia albo treści zapisane dwa razy, które zostały w pliku (tylko krótko, z przykładem).
Jeśli w danym punkcie nic nie ma, napisz „brak".
```
