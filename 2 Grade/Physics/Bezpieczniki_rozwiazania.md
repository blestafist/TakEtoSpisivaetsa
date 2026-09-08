
# Pytania

## Grupa A

**Bezpieczniki,** imię, nazwisko ........................................................... klasa ........................ data ........................

suma punktów ............................ procent punktów ............................ ocena ............................

**Zadanie 1 [0 - 4]** Przez żarówkę pracującą pod napięciem miejskim płynie prąd o natężeniu skutecznym 0,261A. Jaka jest moc żarówki? [punkty]

**Zadanie 2 [0 - 4]** Czy w strefie mieszkalnej chronionej bezpiecznikiem 7A mogą jednocześnie pracować urządzenia o mocach 900W i 800W? Odpowiedź uzasadnij [punkty]

**Zadanie 3 [0 - 4]** W strefie mieszkalnej chronionej bezpiecznikiem 12A pracuje urządzenie o mocy 0,7kW. Jaką moc co najwyżej mogą mieć dodatkowe urządzenia włączone w tej strefie? [punkty]

## Grupa B

**Bezpieczniki,** imię, nazwisko ........................................................... klasa ........................ data ........................

suma punktów ............................ procent punktów ............................ ocena ............................

**Zadanie 1 [0 - 4]** Żarówka o mocy 200W pracuje pod napięciem miejskim. Jakie jest natężenie prądu płynącego przez tę żarówkę? [punkty]

**Zadanie 2 [0 - 4]** W strefie mieszkalnej chronionej bezpiecznikiem 7A pracuje urządzenie o mocy P1 = 800W. Jaka może być maksymalna moc urządzenia P2, które będzie pracowało w tej samej strefie? Odpowiedź uzasadnij [punkty]

**Zadanie 3 [0 - 4]** Czy w strefie mieszkalnej chronionej bezpiecznikiem 12A mogą jednocześnie pracować urządzenia o mocach 600W i 1,2kW? Odpowiedź uzasadnij. [punkty]

# Bezpieczniki — rozwiązania (Grupa A i Grupa B)

Napięcie sieciowe: $U_s = 230\ \text{V}$ (wartość skuteczna).

---

## GRUPA A

### Zadanie 1

**Wzory:**
$$P = U_s \cdot J$$

**Część 1 — Dane i szukane:**

Ujednolicenie jednostek: prąd już w amperach, napięcie w woltach — bez zmian.

Dane: $U_s = 230\ \text{V}$, $J = 0{,}261\ \text{A}$

Szukane: $P$

**Część 2 — Obliczenia:**

$$P = U_s \cdot J = 230 \cdot 0{,}261 = 60{,}03\ \text{W} \qquad [\text{W} = \text{V} \cdot \text{A}]$$

**Część 3 — Odpowiedź:**

$$\boxed{P = 60{,}03\ \text{W}}$$

**Odp.:** Moc żarówki wynosi **60,03 W**.

---

### Zadanie 2

**Wzory:**
$$P = U_s \cdot J \qquad P_{max} = U_s \cdot J_B$$

**Część 1 — Dane i szukane:**

Ujednolicenie jednostek: moce już w watach — bez zmian.

Dane: $U_s = 230\ \text{V}$, $J_B = 7\ \text{A}$, $P_1 = 900\ \text{W}$, $P_2 = 800\ \text{W}$

Szukane: czy strefa zadziała (czy bezpiecznik nie wyłączy obwodu)

**Część 2 — Obliczenia:**

Maksymalna moc strefy:
$$P_{max} = U_s \cdot J_B = 230 \cdot 7 = 1610\ \text{W} \qquad [\text{W} = \text{V} \cdot \text{A}]$$

Suma mocy urządzeń:
$$P_{całk} = P_1 + P_2 = 900 + 800 = 1700\ \text{W} \qquad [\text{W} = \text{W} + \text{W}]$$

Porównanie:
$$P_{całk} > P_{max} \quad\Rightarrow\quad 1700\ \text{W} > 1610\ \text{W}$$

**Część 3 — Odpowiedź:**

$$\boxed{P_{całk} = 1700\ \text{W} > P_{max} = 1610\ \text{W}}$$

**Odp.:** Nie mogą. Suma mocy urządzeń (**1700 W**) przekracza moc dopuszczalną przez bezpiecznik (**1610 W**), więc bezpiecznik przerwie obwód i strefa się wyłączy.

---

### Zadanie 3

**Wzory:**
$$P_{max} = U_s \cdot J_B$$

**Część 1 — Dane i szukane:**

Ujednolicenie jednostek: $P_1 = 0{,}7\ \text{kW} = 700\ \text{W}$.

Dane: $U_s = 230\ \text{V}$, $J_B = 12\ \text{A}$, $P_1 = 700\ \text{W}$

Szukane: $P_d$ — maksymalna moc dodatkowych urządzeń

**Część 2 — Obliczenia:**

Maksymalna moc strefy:
$$P_{max} = U_s \cdot J_B = 230 \cdot 12 = 2760\ \text{W} \qquad [\text{W} = \text{V} \cdot \text{A}]$$

Moc dostępna dla dodatkowych urządzeń (od mocy maksymalnej odejmujemy moc urządzenia już pracującego):
$$P_d = P_{max} - P_1 = 2760 - 700 = 2060\ \text{W} \qquad [\text{W} = \text{W} - \text{W}]$$

**Część 3 — Odpowiedź:**

$$\boxed{P_d = 2060\ \text{W}}$$

**Odp.:** Dodatkowe urządzenia mogą mieć łączną moc co najwyżej **2060 W**, bo razem z pracującym urządzeniem (700 W) nie przekroczą wtedy mocy dopuszczalnej przez bezpiecznik (2760 W).

---

## GRUPA B

### Zadanie 1

**Wzory:**
$$P = U_s \cdot J$$

**Część 1 — Dane i szukane:**

Ujednolicenie jednostek: wszystkie wielkości w jednostkach podstawowych (W, V) — bez zmian.

Dane: $P = 200\ \text{W}$, $U_s = 230\ \text{V}$

Szukane: $J$

**Część 2 — Obliczenia:**

Z przekształcenia wzoru na moc:
$$J = \frac{P}{U_s} = \frac{200}{230} = 0{,}87\ \text{A} \qquad \left[\text{A} = \frac{\text{W}}{\text{V}}\right]$$

**Część 3 — Odpowiedź:**

$$\boxed{J = 0{,}87\ \text{A}}$$

**Odp.:** Natężenie prądu płynącego przez żarówkę wynosi **0,87 A**.

---

### Zadanie 2

**Wzory:**
$$P_{max} = U_s \cdot J_B$$

**Część 1 — Dane i szukane:**

Ujednolicenie jednostek: moc już w watach — bez zmian.

Dane: $U_s = 230\ \text{V}$, $J_B = 7\ \text{A}$, $P_1 = 800\ \text{W}$

Szukane: $P_2$ — maksymalna moc drugiego urządzenia

**Część 2 — Obliczenia:**

Maksymalna moc strefy:
$$P_{max} = U_s \cdot J_B = 230 \cdot 7 = 1610\ \text{W} \qquad [\text{W} = \text{V} \cdot \text{A}]$$

Moc dostępna dla drugiego urządzenia:
$$P_2 = P_{max} - P_1 = 1610 - 800 = 810\ \text{W} \qquad [\text{W} = \text{W} - \text{W}]$$

**Część 3 — Odpowiedź:**

$$\boxed{P_2 = 810\ \text{W}}$$

**Odp.:** Drugie urządzenie może mieć moc co najwyżej **810 W**, bo wtedy suma mocy obu urządzeń nie przekroczy mocy dopuszczalnej przez bezpiecznik (1610 W).

---

### Zadanie 3

**Wzory:**
$$P = U_s \cdot J \qquad P_{max} = U_s \cdot J_B$$

**Część 1 — Dane i szukane:**

Ujednolicenie jednostek: $P_2 = 1{,}2\ \text{kW} = 1200\ \text{W}$; $P_1 = 600\ \text{W}$ bez zmian.

Dane: $U_s = 230\ \text{V}$, $J_B = 12\ \text{A}$, $P_1 = 600\ \text{W}$, $P_2 = 1200\ \text{W}$

Szukane: czy strefa zadziała (czy bezpiecznik nie wyłączy obwodu)

**Część 2 — Obliczenia:**

Maksymalna moc strefy:
$$P_{max} = U_s \cdot J_B = 230 \cdot 12 = 2760\ \text{W} \qquad [\text{W} = \text{V} \cdot \text{A}]$$

Suma mocy urządzeń:
$$P = P_1 + P_2 = 600 + 1200 = 1800\ \text{W} \qquad [\text{W} = \text{W} + \text{W}]$$

Porównanie:
$$P < P_{max} \quad\Rightarrow\quad 1800\ \text{W} < 2760\ \text{W}$$

**Część 3 — Odpowiedź:**

$$\boxed{P = 1800\ \text{W} < P_{max} = 2760\ \text{W}}$$

**Odp.:** Tak, mogą. Suma mocy urządzeń (**1800 W**) jest mniejsza od mocy dopuszczalnej przez bezpiecznik (**2760 W**), więc bezpiecznik nie przerwie obwodu i oba urządzenia będą pracować jednocześnie.
