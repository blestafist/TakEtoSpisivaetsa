## name: german-dativ-akkusativ-solver  
description: Solve German exercises with Dativ + Akkusativ objects and pronoun replacement.

# Goal

Given input like:
`Ich / schenken / mein Bruder / der Ball`

produce:
1. `Ich schenke meinem Bruder den Ball.`
2. `Ich schenke ihm den Ball.`
3. `Ich schenke ihn meinem Bruder.`
4. `Ich schenke ihn ihm.`


# Algorithm

1. Find the subject and conjugate the verb.
2. Determine the verb pattern, e.g.:
    - `jemandem etwas schenken`
    - `jemandem etwas geben`
    - `jemandem etwas erklären`
    - `jemandem etwas zeigen`
3. Identify:
    - receiver/person → usually Dativ (`wem?`)
    - thing/information → usually Akkusativ (`wen/was?`)
4. Decline both noun phrases.
5. Build all 4 sentence variants.

Do not infer case from the order of words in the input.

Example:
`Du / erklären / der Weg / die Touristen`
`erklären = jemandem etwas erklären`

So:
- `die Touristen` → Dativ → `den Touristen`
- `der Weg` → Akkusativ → `den Weg`

Result:

`Du erklärst den Touristen den Weg.`

# Word order rules:
- noun + noun → **DAT + AKK**
- pronoun + noun → **pronoun first**
- both pronouns → **AKK + DAT**

Examples:
`Ich gebe meinem Bruder den Ball.`  
`Ich gebe ihm den Ball.`  
`Ich gebe ihn meinem Bruder.`  
`Ich gebe ihn ihm.`

# Pronouns

|Nominativ|Akkusativ|Dativ|
|---|---|---|
|ich|mich|mir|
|du|dich|dir|
|er|ihn|ihm|
|sie|sie|ihr|
|es|es|ihm|
|wir|uns|uns|
|ihr|euch|euch|
|sie|sie|ihnen|
|Sie|Sie|Ihnen|

# Important declension
Definite articles:
- masculine: `der → den (Akk), dem (Dat)`
- feminine: `die → die (Akk), der (Dat)`
- neuter: `das → das (Akk), dem (Dat)`
- plural: `die → die (Akk), den (Dat)`
    

Possessives behave like `ein`:
`mein Bruder → meinem Bruder / meinen Bruder`

Dativ plural usually adds `-n`:
`die Kinder → den Kindern`  
`die Freunde → den Freunden`

But not when already ending in `-n/-s`:
`die Touristen → den Touristen`  
`die Autos → den Autos`

Watch N-Deklination:
`der Student → dem Studenten`  
`der Junge → dem Jungen`

# Common traps (pułapki)
- Input order does not determine Dativ/Akkusativ.
- Pronoun gender follows grammatical gender:
    - `der Ball → ihn`
    - `die Tasche → sie`
    - `das Buch → es`
- Both pronouns: always normally **Akk before Dat**:
    - `Ich gebe ihn ihm.`
- Do not force every verb into Dat + Akk. Verify verb government first.
- With separable verbs keep normal object rules:
    - `Ich gebe ihm das Buch zurück.`

# Output

Return:
1. Full sentence.
2. Dativ replaced by pronoun.
3. Akkusativ replaced by pronoun.
4. Both replaced by pronouns.

If asked for explanation, briefly state:
`verb pattern → Dativ form → Akkusativ form → pronouns → word order`
