# Termodynamika – oznaczenia i sposób rozwiązywania zadań

> **Dla AI:** Uczeń ma fizykę w szkole podstawowej, dział termodynamika. Przy wyjaśnianiu i rozwiązywaniu zadań używaj **dokładnie tych oznaczeń i tego schematu**. Wzory zapisuj w LaTeX. Odpowiadaj po polsku. 

## 1. Oznaczenia

| Symbol | Znaczenie | Jednostka |
|---|---|---|
| $E$ | energia / ciepło pobrane lub oddane (zamiast $Q$) | $\text{J}$ |
| $m$ | masa | $\text{kg}$ |
| $\Delta T$ | zmiana temperatury $= T_{\text{końc}} - T_{\text{pocz}}$ | $^\circ\text{C}$ |
| $c_w$ | ciepło właściwe ($c_{ww}$ – wody, $c_{wl}$ – lodu) | $\frac{\text{J}}{\text{kg}\cdot{}^\circ\text{C}}$ |
| $c_t$ | ciepło topnienia | $\frac{\text{J}}{\text{kg}}$ |
| $c_p$ | ciepło parowania | $\frac{\text{J}}{\text{kg}}$ |
| $P$ | moc | $\text{W}$ |
| $W$ | praca | $\text{J}$ |
| $t$ | czas | $\text{s}$ |
| $\Delta E_w$, $Q$ | zmiana energii wewnętrznej, ciepło (tylko w I zasadzie) | $\text{J}$ |

## 2. Wartości (jeśli zadanie nie podaje innych)

$c_{ww} = 4200$, $c_{wl} = 2100$, żelazo $450$, aluminium $900$ $\left[\frac{\text{J}}{\text{kg}\cdot{}^\circ\text{C}}\right]$

$c_t$ lodu $= 334\,000\ \frac{\text{J}}{\text{kg}}$, $c_p$ wody $\approx 2\,256\,000\ \frac{\text{J}}{\text{kg}}$

Woda: topnienie $0\ ^\circ\text{C}$, wrzenie $100\ ^\circ\text{C}$. Zero bezwzględne: $0\ \text{K} = -273\ ^\circ\text{C}$.

## 3. Wzory

$$E = m \cdot c_w \cdot \Delta T \qquad E = m \cdot c_t \qquad E = m \cdot c_p$$

$$P = \frac{W}{t} = \frac{E}{t} \qquad E_k = \frac{m v^2}{2} \qquad \Delta E_w = Q + W$$

Bilans cieplny: $E_{\text{oddane}} = E_{\text{pobrane}}$

## 4. Schemat rozwiązywania

1. **Dane / Szukane.**
2. **Jednostki:** g → kg, min/h → s. Wynik w J (nie kJ, chyba że przeliczone).
3. **Etapy procesu** – każdy to osobne $E_1, E_2, E_3$, np.:
   $$\text{lód } (-5^\circ) \xrightarrow{E_1} \text{lód } (0^\circ) \xrightarrow{E_2} \text{woda } (0^\circ) \xrightarrow{E_3} \text{woda } (20^\circ)$$
4. **Wzór → podstawienie → wynik**, kroki łączone strzałką $\Rightarrow$.
5. **Znak:** przy stygnięciu $\Delta T < 0$, więc $E < 0$ (energia oddana). W bilansie porównujemy wartości bez minusa.
6. Wynik z jednostką i poprawnie zaokrąglony.

**Pułapki:** do lodu $c_{wl} = 2100$, do wody $4200$; stopiony lód ogrzewa się dalej, jeśli temperatura końcowa $> 0^\circ$; moc w W, energia w J.

## 5. Najważniejsza teoria

- Wyższa temperatura → cząsteczki poruszają się szybciej.
- **Temperatura** – miara średniej energii kinetycznej cząsteczek. **Energia wewnętrzna** – suma energii kinetycznej i potencjalnej wszystkich cząsteczek. Lód i woda w $0^\circ$ mają tę samą $E_k$, ale woda ma większą energię wewnętrzną.
- **Ciepło** – przepływ energii z ciała cieplejszego do zimniejszego.
- **Dyfuzja** – samorzutne mieszanie się cząsteczek (perfumy, sok w wodzie). **Konwekcja** – ciepła ciecz/gaz unosi się, zimna opada (tylko ciecze i gazy).
- Ciała przy ogrzewaniu się rozszerzają, przy ochładzaniu kurczą (wyjątek: woda $0$–$4^\circ$).
- **Przemiany:** topnienie / krzepnięcie, parowanie / skraplanie, sublimacja / resublimacja. Parowanie – w każdej temperaturze, z powierzchni. Wrzenie – w całej objętości, w temperaturze wrzenia (zależy od ciśnienia; dlatego w szybkowarze woda wrze ok. $120^\circ$).
- Ciało krystaliczne topi się w stałej temperaturze (poziomy odcinek na wykresie). Ciało bezpostaciowe (szkło, wosk) – w szerokim zakresie temperatur, bez poziomego odcinka.

## 6. Przykłady

**Grzałka $1200\ \text{W}$, $1\ \text{min}$, $2\ \text{kg}$ wody. Szukane $\Delta T$.**
$$E = P \cdot t = 1200 \cdot 60 = 72\,000\ \text{J} \;\Rightarrow\; \Delta T = \frac{E}{m \cdot c_w} = \frac{72\,000}{2 \cdot 4200} \approx 8{,}6\ ^\circ\text{C}$$

**$20\ \text{g}$ lodu z $-5^\circ$ na wodę $20^\circ$.**
$$E = m\,(c_{wl} \cdot \Delta T_1 + c_t + c_{ww} \cdot \Delta T_2) = 0{,}02\,(2100 \cdot 5 + 334\,000 + 4200 \cdot 20) = 8570\ \text{J}$$

**Bilans: $250\ \text{g}$ wody $30^\circ$; ile lodu $0^\circ$ dać, by było $10^\circ$?**
$$E_{\text{oddane}} = 0{,}25 \cdot 4200 \cdot 20 = 21\,000\ \text{J}$$
$$m\,(c_t + c_{ww} \cdot 10) = 21\,000 \;\Rightarrow\; m = \frac{21\,000}{376\,000} \approx 0{,}056\ \text{kg} = 56\ \text{g}$$

**Czajnik $1800\ \text{W}$: $1\ \text{kg}$ wody i $0{,}1\ \text{kg}$ lodu z $0^\circ$ do $50^\circ$. Szukane $t$.**
$$E = 1 \cdot 4190 \cdot 50 + 0{,}1 \cdot 334\,000 + 0{,}1 \cdot 4190 \cdot 50 = 263\,850\ \text{J}$$
$$t = \frac{E}{P} = \frac{263\,850}{1800} \approx 147\ \text{s}$$
