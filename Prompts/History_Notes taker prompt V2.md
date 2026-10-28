# History Lessons → Full Information (V2)

## 1. Task

Turn history lesson recordings into a complete record of the information the teacher gave. It is not a summary, and it is not a copy of the transcript.

Principle: every fact stays, every word that carries no fact goes. The most important content is kept word for word, the rest as short facts, and stories and talk are dropped.

The teacher's tests ask about small details: dates, names, places, numbers, causes, consequences, definitions, complete lists. A missing detail, or one changed by paraphrasing, costs me points.

The output is very precise notes on the topic, read as Markdown text. It is not a lesson-by-lesson recap: the information is organised by topic, and nothing in it refers to lessons, recordings or timecodes. It must be complete, exact and consistently formatted.

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
- source texts (teksty źródłowe) she reads aloud or quotes: fragments of documents, chronicles, treaties, laws, letters, speeches. Keep the whole passage, plus the author, title and date if she gives them;
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

Default: trust the transcript. Whisper is accurate on these recordings. Its weak spot is names of people and places, especially foreign ones; pay the most attention there. Raise a doubt only when there is concrete evidence (the steps below), never just because a word looks unusual.

### Step 1: resolve inside the transcript
Apply the first rule that fits. Log every change in the report (section 7).

1. Self-correction. The teacher says something and corrects it right away ("nie, przepraszam", "znaczy", "pomyliłam się", "właściwie", "sorry"), or a student corrects her and she agrees. The corrected version wins.
2. My label. If my label in the `.md` file spells a name or term, use my spelling.
3. Same thing elsewhere. If a name or term appears clearly and consistently elsewhere in the batch, and once in a different form, use the consistent form.
4. Obvious mishearing of a name, place or term. The transcribed word doesn't exist or makes the sentence nonsense, AND it sounds almost the same as exactly one well-known name, place or term that fits the context ("Pił suski" → "Piłsudski", "Westfalii" written as "West Valii" → "Westfalii"). Fix it, using the standard Polish spelling. Never for dates or numbers.
5. Teacher contradicts herself (no correction, e.g. 1791 at 10:20 and 1792 at 31:05). Pick the version she repeats more often. If it's a tie, pick the version she dictated, wrote down or stressed. Otherwise go to step 3.
6. Whisper hallucinations. Ignore looping lines and phrases that appear during silence ("Napisy stworzone przez społeczność Amara.org", "Dziękuję za uwagę" out of context, etc.).

Example of rule 1:
```
Pokój toruński, to był rok 1456, nie, przepraszam, 1466. Tysiąc czterysta sześćdziesiąt sześć.
```
In the file: `- Pokój toruński: 1466.` In the report: `| L1 | 14:05 | 1456 | 1466 |`

### Step 2: check key claims against sources

What to check (only these):
- claims that could be a test question: classifications (who belonged to which school of thought), who did what, causes and effects, what a reform, treaty or law contained, key terms;
- names of people and places. These are Whisper's weak spot;
- dates, but only those tied to an important event: a battle, treaty, reform, law, constitution, coronation, uprising, or the start or end of a war. Skip minor dates.

What not to check:
- differences in emphasis or interpretation that don't change a fact;
- spelling conventions, Polish vs Latin form of a name;
- numbers she marks as approximate ("około");
- details that only add colour.

How to check:
1. Prefer Polish sources: Polish school textbooks and the school curriculum (podstawa programowa), Encyklopedia PWN, Polish Wikipedia. Polish school history sometimes presents things differently from English sources. The Polish school version wins.
2. If you can search the web, verify there.
3. If you can run subagents, delegate the lookups to a small, fast model (e.g. Claude Haiku). Give each subagent a group of claims. Ask for one line per claim: `twierdzenie | zgodne / niezgodne / nie wiadomo | poprawna wersja | źródło`. Keep it short: one claim, one answer, one source.
4. If you can't search, use your own knowledge, but flag a difference only when you are confident. Write `źródło: wiedza modelu` in the question, so I know it wasn't looked up.
5. "Nie wiadomo" counts as no difference. No question.

Results:
- If it matches: nothing to do.
- If it differs: never change it yourself. It goes to step 3 as a question, with two pieces of evidence:
  1. How firmly she said it. Find every place in the batch where she states it, and list the timecodes. It counts as her firm belief if she says it 2 or more times, or dictates it, stresses it, or explains why it's true.
  2. The sound test (only for words, names and numbers that could be misheard). Write both versions as spoken Polish words, e.g. 1791 = "tysiąc siedemset dziewięćdziesiąt jeden", 1792 = "tysiąc siedemset dziewięćdziesiąt dwa".
     - "brzmi podobnie": the two could be confused by ear, so it may be a mishearing;
     - "brzmi inaczej": Whisper heard it right, so she really said it.

The teacher is the reference for the test. Sometimes she deliberately teaches a version different from the internet, and that version is what she will ask about. Your knowledge never overrides her. It only produces questions.

Example:
```
[L1 08:15] „John Locke był racjonalistą".
Też w: 24:30, L2 03:10. Podkreśliła: tak (24:30, „zapiszcie").
Źródła: Locke był empirystą, przeciwnikiem racjonalizmu (Encyklopedia PWN).
Brzmi inaczej.
→ A) racjonalista, jej wersja (domyślnie) / B) empirysta, wersja ze źródeł
```

### Step 3: ask me about everything still open
Send ONE message with numbered questions BEFORE writing the file. Group them by type. Within each type, put the most important first: priority 1 and `[WAŻNE]` items, then the rest.

If there are more than about 15 questions, write the 15 most important ones in full. List the rest as one line each (`12) [L2 31:40] Grunwald 1411? → 1410`). These take the default unless I object.

Each full question has:
- lesson and timecode, so I can re-listen;
- the transcript text;
- the problem in one line (for step 2 items: the source version with the source name, how firmly she said it, and the sound test);
- options, with the default marked `(domyślnie)`.

Types and their default options:
1. Teacher vs sources (from step 2). The default depends on the evidence:
   - her firm belief (2+ times, dictated, stressed or explained): default = her version;
   - said once, "brzmi inaczej": default = her version;
   - said once, "brzmi podobnie": default = the source version (probably a mishearing).

   `[L2 14:05] „Konstytucja 3 maja 1792". Tylko raz. Źródła: 1791. Brzmi podobnie. → A) 1791, wersja ze źródeł (domyślnie) / B) 1792, jej wersja`
2. Unresolved teacher contradiction (from step 1, rule 5): she gave two versions equally often and stressed neither.
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
3. The only marker allowed is `[WAŻNE]`, always written exactly like this.
4. No timecodes anywhere in the information file. Timecodes belong only in the questions and the report.
5. One fact or one sentence of hers per bullet. Sub-bullets for details of the bullet above.
6. Write each thing only once:
   - definitions only in "Definicje"; in the main text write `Liberum veto (zob. Definicje)`;
   - stressed items only in the main text; "Wskazówki nauczyciela" only points to them;
   - when the same topic comes up in several lessons, or in a recap, merge everything into one place.
7. Source texts: write them as a quote block (`>`), with a line before it: `Tekst źródłowy: <autor, tytuł, data, if given>`. Word for word, only fillers removed.

### Consistent formats
Write the same kind of thing the same way everywhere, so the file is easy to search and quiz from. This applies to the file, not to the teacher's wording: only the format changes, never the content.
1. Years: always digits, `1466`, never words. In her sentences, keep her "w 1466 roku". In short notes and tables, just `1466`.
2. Full dates: `15 lipca 1410`.
3. Ranges: `1618–1648` (en dash, no spaces). Reigns: `Kazimierz Wielki (1333–1370)`, only if she gives the dates.
4. Centuries: Roman numerals with `w.`: `XV w.`, `XV–XVI w.`, `poł. XVII w.`, `koniec XVIII w.`
5. Before Christ: `p.n.e.`, after: `n.e.` only when needed to avoid confusion.
6. Other numbers: digits (`3 rozbiory`, `40 tys. żołnierzy`), except at the start of a sentence.
7. Names: the standard Polish form (`Ludwik XIV`, `Karol Wielki`, `Fryderyk II Wielki`), the same form everywhere. The first time a person appears, write the full name; later, the short form she uses, consistently.
8. Ruler numbers: Roman numerals (`Zygmunt III Waza`, `Henryk VIII`).
9. Terms: the same term for the same thing everywhere. If she uses two names for one thing, write it as `Sejm Wielki (Sejm Czteroletni)` the first time, then one of them consistently.

### Structure
Output exactly these sections, in this order:

```
# <Przedmiot>: <temat>

## Legenda
- [WAŻNE]: nauczycielka podkreśliła, że to ważne / będzie na sprawdzianie / kazała zapisać.
- (n) w nagłówku wyliczenia: liczba punktów.

## <Temat 1>
### <Podtemat>
- ...
### <Podtemat>
- ...

## <Temat 2>
...

## Definicje
- <Termin>: <definicja, słowo w słowo>

## Chronologia
| data | wydarzenie |
| --- | --- |

## Wskazówki nauczyciela i sprawdzian
### Podkreślone
- <Temat> › <Podtemat>: <czego dotyczy>
### Organizacja
- <terminy sprawdzianów i zakres, zadania domowe, terminy, materiały, w całości>
```

Rules for the structure:
1. Organise by topic, not by lesson. No lesson headings, no lesson numbers, no dates of lessons.
2. Order the topics logically: chronologically, or from causes to events to effects. Usually that's the order she taught them in.
3. If a topic is spread over several lessons, it's still one section.

### File name
`<Przedmiot>_<Temat-lub-okres>.md`, e.g. `Historia_Rewolucja-Francuska.md`

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
| lekcja | timecode'y | wersje | wybrano | dlaczego (częściej powtarzana / podyktowała / podkreśliła) |
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
   - every priority 1 item (reforms, lists, definitions, source texts, `[WAŻNE]` items, passages at my timecodes) is word for word: compare it sentence by sentence with the transcript;
   - every stress signal is marked `[WAŻNE]` and has a pointer in "Wskazówki";
   - every list has its count in the heading, no point merged or dropped (re-read the transcript for each list);
   - priority 2: every fact kept, in her words, as short notes;
   - no anecdotes, classroom talk, fillers or recaps without new information;
   - each thing written only once;
   - every block is in the file or in "Pominięte fragmenty";
   - every decision and my answers are applied, and each one is logged in the report;
   - every source text she read is in the file word for word, as a quote block;
   - consistent formats: years as digits, centuries as `XV w.`, ranges with `–`, the same form of every name and term throughout;
   - the file contains no uncertainty: no "?", no alternatives, no markers other than `[WAŻNE]`;
   - the information file contains no timecodes, no lesson numbers or lesson headings, and is organised by topic;
   - no emojis, no bold, everything in Polish.
7. Output the information file, then the report.

## Appendix: Audit prompt

Paste into a NEW chat with the information file, the report and the `.srt` files:

```text
Porównaj załączony plik z informacjami z transkrypcjami. Raport opisuje wszystkie świadome zmiany (autopoprawki, poprawki transkrypcji, rozstrzygnięcia, uzupełnienia ze źródeł). Nie przepisuj pliku. Wypisz tylko:
1. Fakty z transkrypcji, których brakuje w pliku (daty, nazwiska, miejsca, liczby, przyczyny, skutki, elementy wyliczeń, definicje), z timecode'em.
2. Reformy, wyliczenia, definicje, teksty źródłowe i fragmenty oznaczone [WAŻNE], w których cokolwiek zostało skrócone, pominięte lub ujęte innymi słowami niż w transkrypcji (nawet jedno zdanie, wyjaśnienie „czyli…" czy przykład). Porównaj zdanie po zdaniu. Podaj oryginał i wersję z pliku.
3. Miejsca, gdzie nauczycielka podkreśliła wagę („ważne", „będzie na sprawdzianie", „zapiszcie", „pamiętajcie", dyktowanie, wielokrotne powtarzanie), a w pliku nie ma [WAŻNE].
4. Wyliczenia, w których brakuje choć jednego punktu, punkty zostały połączone, albo liczba w nagłówku nie zgadza się z liczbą punktów.
5. Miejsca, gdzie nauczycielka się poprawiła, a w pliku jest pierwsza (błędna) wersja.
6. Pozostałe miejsca, gdzie słowa nauczycielki sparafrazowano albo usunięto zastrzeżenia („około", „prawdopodobnie", „głównie" itp.).
7. Daty, liczby, nazwy i twierdzenia, które w pliku różnią się od transkrypcji albo w niej nie występują, a nie są opisane w raporcie.
8. Ważne twierdzenia, nazwiska, nazwy miejsc i daty ważnych wydarzeń w pliku, które są niezgodne z polskimi źródłami szkolnymi (podręczniki, Encyklopedia PWN), a nie są opisane w raporcie (pytanie do ucznia lub rozstrzygnięcie). Pomiń drobne daty i różnice w interpretacji.
9. Teksty źródłowe odczytane przez nauczycielkę, których nie ma w pliku słowo w słowo.
10. Niepewności w pliku: znaki zapytania, alternatywne wersje, „może", „według źródeł", znaczniki inne niż [WAŻNE], timecode'y, numery lekcji.
11. Niespójny zapis: lata słownie, różne formy tego samego nazwiska lub terminu, wieki nie w formie „XV w.".
12. Anegdoty, wypełniacze, powtórzenia albo treści zapisane dwa razy, które zostały w pliku (tylko krótko, z przykładem).
Jeśli w danym punkcie nic nie ma, napisz „brak".
```
