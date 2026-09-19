## name: german-dativ-akkusativ-generator  
description: Generate German Dativ + Akkusativ exercises with controlled difficulty and answer keys.

# Goal

Generate exercises like:
`Ich / schenken / mein Bruder / der Ball`

The learner must produce:
1. full sentence;
2. Dativ → pronoun;
3. Akkusativ → pronoun;
4. both → pronouns.

# Generation rules

Use verbs that normally follow:
`jemandem etwas + Verb`

Good verbs:
`geben, schenken, zeigen, erklären, erzählen, schicken, bringen, leihen, verkaufen, empfehlen, schreiben, kaufen, anbieten, zurückgeben`

Generate:
- a subject;
- one Dativ receiver/person;
- a subject;
- one Dativ receiver/person;
- one Akkusativ thing/information.

Source noun phrases should stay in base/Nominativ form:
`mein Bruder`, not `meinem Bruder`  
`der Ball`, not `den Ball`

Randomize object order in the prompt.

Both are valid exercise formats:
`Ich / schenken / mein Bruder / der Ball`
`Du / erklären / der Weg / die Touristen`

This prevents solving by position.

# Required answer rules
- noun + noun → DAT + AKK
- one pronoun → pronoun first
- both pronouns → AKK + DAT

Example:
`Ich schenke meinem Bruder den Ball.`  
`Ich schenke ihm den Ball.`  
`Ich schenke ihn meinem Bruder.`  
`Ich schenke ihn ihm.`

# Difficulty

**Easy**
- singular nouns
- der/die/das
- simple subjects and verbs

**Normal**
- possessives
- all genders
- plural objects
- randomized input order

**Hard**
- Dativ plural
- N-Deklination
- separable verbs
- less obvious noun combinations

Examples of traps:
`die Kinder → den Kindern → ihnen`
`der Student → dem Studenten → ihm`
`das Buch → es`
`die Tasche → sie`

# Variety

Across a set, mix:

- masculine/feminine/neuter/plural;
- definite, indefinite and possessive articles;
- different subjects and verbs;
- both possible source object orders.

Do not generate repetitive sets such as ten sentences with `ich + geben`.

Sentences must be semantically natural.

Good:
`jemandem den Weg erklären`  
`jemandem ein Buch schenken`

Bad:
`jemandem den Lehrer schenken`

# Validation

Before output, verify:
- verb really supports Dat + Akk;
- verb conjugation;
- article endings;
- Dativ plural `-n`;
- N-Deklination;
- correct pronouns;
- correct word order;
- German capitalization and spelling.

# Modes
**practice** — exercises only  
**answers** — exercises + solutions  
**interactive** — one exercise at a time  
**exam** — no hints

Default exercise:
`Subject / infinitive / noun phrase / noun phrase`

Default solution contains the four sentence variants.
