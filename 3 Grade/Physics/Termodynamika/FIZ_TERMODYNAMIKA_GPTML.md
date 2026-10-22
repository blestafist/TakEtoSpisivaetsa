# FIZ — Termodynamika — GPTML

## 1. Instrukcja dla AI-solwera

Rozwiązuj zadania po polsku, na poziomie podstawowym liceum. Pisz prostymi słowami, tak jak uczeń na sprawdzianie. Korzystaj z poniższych oznaczeń, wzorów i sposobów zapisu z zeszytu. To jest baza konwencji rozwiązywania zadań oraz notatka z lekcji.

- W zadaniu obliczeniowym: dane i szukane → zamiana jednostek → wzór → przekształcenie, jeśli potrzebne → podstawienie → wynik z jednostką → krótka odpowiedź.
- W zadaniu teoretycznym wystarczy krótka odpowiedź z notatki. Nie dopisuj wykładu ani trudniejszych pojęć.
- Stosuj LaTeX do wzorów. Używaj przecinka dziesiętnego, np. $8{,}6^\circ\mathrm{C}$.
- Najpierw korzystaj z danych zadania, następnie z tego pliku. Nie zastępuj danych zadania wartościami zapamiętanymi z innych źródeł.
- Nie wymyślaj brakujących danych ani treści zadań, których nie ma na zdjęciach. Gdy brakuje danych, wskaż konkretnie czego brakuje.
- Dopuszczalne są zwykłe przekształcenia poniższych wzorów, dodawanie energii kolejnych etapów i bilans cieplny.
- Nie wprowadzaj rachunku różniczkowego, moli, stałej Boltzmanna, równań gazu doskonałego, entropii ani równania Clausiusa–Clapeyrona. Nie są potrzebne do pokazanych metod.
- Nie traktuj oczywistych pomyłek zapisu jako nowych konwencji. Uwagi redakcyjne w sekcji 8 wyjaśniają takie miejsca.

## 2. Oznaczenia i jednostki — obowiązujące przy rozwiązywaniu

| Symbol | Znaczenie | Jednostka / zapis |
|---|---|---|
| $E$ | energia potrzebna do ogrzania, stopienia lub odparowania substancji | $\mathrm{J}$ |
| $E_w$ | energia wewnętrzna | $\mathrm{J}$ |
| $\Delta E_w$ | zmiana energii wewnętrznej | $\mathrm{J}$ |
| $E_k$ | energia kinetyczna | $\mathrm{J}$ |
| $Q$ | ciepło przekazane lub oddane w I zasadzie termodynamiki | $\mathrm{J}$ |
| $W$ | praca wykonana przez ciało lub nad ciałem | $\mathrm{J}$ |
| $m$ | masa | $\mathrm{kg}$ |
| $v$ | prędkość | $\mathrm{m/s}$ |
| $c_w$ | ciepło właściwe | $\mathrm{J/(kg\cdot{}^\circ C)}$ |
| $c_{ww}$ | ciepło właściwe wody | jak wyżej |
| $c_{wl}$ | ciepło właściwe lodu | jak wyżej |
| $c_t$ | ciepło topnienia | $\mathrm{J/kg}$ |
| $c_p$ | ciepło parowania | $\mathrm{J/kg}$ |
| $T$ | temperatura | w tych zadaniach zwykle $^\circ\mathrm{C}$ |
| $\Delta T$ | zmiana temperatury | $^\circ\mathrm{C}$ |
| $P$ | moc | $\mathrm{W}$ |
| $t$ | czas | $\mathrm{s}$ |

**Zapis z klasy:** w obliczeniach ogrzewania i przemian fazowych używaj $E$, nie zamieniaj go bez potrzeby na $Q$. Symbol $Q$ zostaje przy I zasadzie termodynamiki. Nie zastępuj $E_w$ symbolem $U$, $c_t$ symbolem $\lambda$, a $c_p$ symbolem $L$ lub $r$.

$c_p$ oznacza tutaj ciepło parowania, a nie ciepło właściwe przy stałym ciśnieniu. $c_w$ oznacza ciepło właściwe dowolnej wskazanej substancji, nie zawsze wody. Symbol $W$ to praca, natomiast $\mathrm{W}$ po liczbie to jednostka mocy — wat.

### Wartości

W zeszycie w przykładach:
- woda: $c_w=4200\ \mathrm{J/(kg\cdot{}^\circ C)}$;
- żelazo: $c_w=450\ \mathrm{J/(kg\cdot{}^\circ C)}$.

W istniejącej notatce repozytorium podano dodatkowo wartości do zadań, jeżeli zadanie nie podaje innych:
- lód: $c_{wl}=2100\ \mathrm{J/(kg\cdot{}^\circ C)}$;
- aluminium: $c_w=900\ \mathrm{J/(kg\cdot{}^\circ C)}$;
- ciepło topnienia lodu: $c_t=334\,000\ \mathrm{J/kg}$;
- ciepło parowania wody: $c_p\approx2\,256\,000\ \mathrm{J/kg}$.

Wartości współczynników odczytuj z tabeli lub treści zadania. Dla wody przy zwykłym ciśnieniu: temperatura topnienia $0^\circ\mathrm{C}$, temperatura wrzenia $100^\circ\mathrm{C}$.

Przeliczenia: $1\ \mathrm{kg}=1000\ \mathrm{g}$, $1\ \mathrm{min}=60\ \mathrm{s}$, $1\ \mathrm{h}=3600\ \mathrm{s}$, $1\ \mathrm{kJ}=1000\ \mathrm{J}$, $1\ \mathrm{kW}=1000\ \mathrm{W}$.

## 3. Wzory i sposób ich używania

### Energia kinetyczna

$$E_k=\frac{mv^2}{2}$$

„Energia kinetyczna jest związana z masą i prędkością.”

### I zasada termodynamiki

W zeszycie zapisano wybór znaków:

$$\Delta E_w=(\pm Q)+(\pm W)$$

- $\Delta E_w$ — „zmiana energii wewnętrznej”;
- $Q$ — „ciepło przekazane lub oddane”;
- $W$ — „praca wykonana przez ciało lub nad ciałem”.

Znaki stosuj z punktu widzenia rozpatrywanego ciała:
- ciało pobiera ciepło: $+Q$;
- ciało oddaje ciepło: $-Q$;
- praca wykonywana nad ciałem: $+W$;
- praca wykonywana przez ciało: $-W$.

Można też zapisać $\Delta E_w=Q+W$, jeśli $Q$ i $W$ mają już odpowiednie znaki. Nie wybieraj znaków drugi raz.

### Ogrzewanie lub ochładzanie bez zmiany stanu skupienia

$$E=m\cdot c_w\cdot\Delta T$$

$$\Delta T=T_{\mathrm{końc}}-T_{\mathrm{pocz}}$$

Przekształcenia, gdy są potrzebne:

$$\Delta T=\frac{E}{m c_w},\qquad m=\frac{E}{c_w\Delta T},\qquad c_w=\frac{E}{m\Delta T}$$

Przy stygnięciu tak obliczona $\Delta T$ jest ujemna, więc $E<0$. Jeżeli pytanie dotyczy ilości energii oddanej, podaj dodatnią wartość tej energii. W bilansie „oddane = pobrane” porównuj dodatnie ilości energii: dla ciała stygnącego użyj spadku temperatury $T_{\mathrm{pocz}}-T_{\mathrm{końc}}$. Nie mieszaj obu sposobów zapisu.

### Topnienie i parowanie

$$E=m\cdot c_t$$

$$E=m\cdot c_p$$

Pierwszy wzór dotyczy samego topnienia substancji już w temperaturze topnienia. Drugi dotyczy odparowania substancji już w temperaturze wrzenia. W tych wzorach nie ma $\Delta T$. Przy krzepnięciu i skraplaniu oddawana jest odpowiadająca im ilość energii.

### Moc, energia, czas

$$P=\frac{W}{t}=\frac{E}{t}$$

$$E=P\cdot t,\qquad t=\frac{E}{P}$$

Przy mocy w watach podstawiaj czas w sekundach. W zadaniach z grzałką utożsamiaj energię $Pt$ z energią ogrzewania, jeżeli przyjmujemy brak strat. Jeżeli zadanie uwzględnia straty, nie pomijaj ich.

### Kilka etapów i bilans cieplny

Każdy etap policz osobno. Przykład z zeszytu:

lód $(-5^\circ\mathrm{C})$ → lód $(0^\circ\mathrm{C})$ → woda $(0^\circ\mathrm{C})$ → woda $(20^\circ\mathrm{C})$.

1. Ogrzewanie lodu: $E_1=m c_{wl}\cdot5^\circ\mathrm{C}$.
2. Topnienie lodu: $E_2=m c_t$.
3. Ogrzewanie wody: $E_3=m c_{ww}\cdot20^\circ\mathrm{C}$.

$$E=E_1+E_2+E_3$$

Bilans cieplny przy braku strat:

$$E_{\mathrm{oddane}}=E_{\mathrm{pobrane}}$$

Najpierw ustal, co się ogrzewa, co stygnie i czy zachodzi przemiana fazowa. Nie zakładaj bez sprawdzenia, że cały lód się stopił. Nie używaj ciepła właściwego wody do ogrzewania lodu. Powyższy podział na etapy i zapis bilansu rozwijają schemat z zeszytu oraz istniejącą notatkę, nie są dosłownym zapisem obliczeń ze zdjęcia 5.

## 4. Cząsteczki i energia — przepisane z zeszytu

Poniżej zachowano sformułowania zeszytu, łącząc fragmenty dotyczące tego samego tematu. Pominięto skreślone słowa; ujednolicono interpunkcję, skróty jednostek i zapis wzorów. Dopowiedzenia oznaczono osobno.

### Cząsteczki a stan skupienia

| Cecha | Stan stały | Stan ciekły | Stan gazowy |
|---|---|---|---|
| Położenie cząsteczek | „ściśle, blisko” | „trochę dalej od siebie” | „w dużych odległościach” |
| Ruch cząsteczek | „drgają, niewielki ruch” | „poruszają się swobodnie” | „poruszają się swobodnie, ruchem chaotycznym” |
| Inne | „ciężko jest zmienić kształt, objętość” | „kształt lekko zmienić, objętość trudno” | „kształt, objętość lekko zmienić” |

„Im wyższa temp., tym cząsteczki poruszają się z większą prędkością.”

„Im niższa temperatura, tym prędkość cząsteczki jest mniejsza.”

„Temp. zera absolutnego, temp. zera bezwzględnego”: $0\ \mathrm{K}=-273{,}15^\circ\mathrm{C}$.

### Dyfuzja i konwekcja

„Dyfuzja to samorzutne mieszanie się cząsteczek.”

„Zjawisko konwekcji to samorzutne unoszenie się cieplejszych cząsteczek do góry.”

„Przykłady zjawisk dyfuzji, konwekcji” — w tym miejscu nie zapisano konkretnych przykładów.

„Dyfuzja zachodzi w ciałach stałych.”

Dopowiedzenie do rozwiązywania: dyfuzja zachodzi także w cieczach i gazach; ostatnie zdanie nie ogranicza jej do ciał stałych. Konwekcję opisuj prosto jako unoszenie cieplejszej cieczy lub gazu.

### Temperatura i energia wewnętrzna

| Temperatura | Energia wewnętrzna |
|---|---|
| „związana tylko z energią kinetyczną cząsteczki” | „związana z energią kinetyczną cząsteczki oraz energią potencjalną związaną z oddziaływaniem między cząsteczkami. (suma)” |

Z dalszej części tabeli:
- „lód temp. $0^\circ$ — mniejsza en. wew.”;
- „woda temp. $0^\circ$ — większa en. wew.”;
- „Ciała mogą mieć taką samą temp., ale różne energie wewnętrzne.”
- $E_w$ lodu $<E_w$ wody.

Doprecyzowanie z wcześniejszego GPTML: porównujemy tę samą masę lodu i wody w $0^\circ\mathrm{C}$. Temperatura wiąże się ze średnią energią kinetyczną cząsteczek, a energia wewnętrzna jest sumą energii kinetycznych i potencjalnych wszystkich cząsteczek.

### Ciepło

„Ciepło to przepływ energii wynikające z różnicy temperatur.”

Krótka poprawna odpowiedź: ciepło to przepływ energii wynikający z różnicy temperatur; energia przepływa od ciała cieplejszego do zimniejszego.

Przy I zasadzie zapisano też polecenie: „Zadanie obliczeniowe, oraz krótkie teorie” — nie podano jego treści.

## 5. Rozszerzalność cieplna — przepisane z zeszytu

1. „Ciała rozszerzają się na skutek wzrostu temperatury.”
2. „Ciała kurczą się na skutek spadku temp.”
3. „Przykłady”:
   - „Termometr”;
   - „Hotend na drukarce 3D”;
   - „Tory kolejowe (dystans pomiędzy)”;
   - „Przewody elektryczne”;
   - „Silniki spalinowe”.

„Kiedy hotend jest «na zimno» ma trochę inne wymiary.”

Do odpowiedzi wystarczy nazwać zjawisko i związać je ze wzrostem lub spadkiem temperatury. Na zdjęciach nie ma wzorów na rozszerzalność — nie wprowadzaj współczynników rozszerzalności do zwykłego pytania o przykłady.

## 6. Ciepło właściwe — definicja i przykłady z zeszytu

„Ciepło właściwe to wielkość określająca ile energii potrzeba aby ogrzać 1 kg substancji o 1°C.”

$$E=m c_w\Delta T$$

- „$E$ energia [J]”;
- „$m$ masa [kg]”;
- „$c_w$ ciepło właściwe — odczytujemy z tabeli”;
- „$\Delta T$ zmiana temperatury [°C]”.

### Zadanie 3 — zapis obliczeń

Pełnej treści zadania nie ma na zdjęciu.

$$c_w(\mathrm{woda})=4200\ \frac{\mathrm{J}}{\mathrm{kg}\cdot{}^\circ\mathrm{C}},\qquad m=2\ \mathrm{kg}$$

$$\Delta T=30^\circ\mathrm{C}-20^\circ\mathrm{C}=10^\circ\mathrm{C}$$

$$E=2\cdot4200\cdot10=84\,000\ \mathrm{J}$$

Odp.: $84\ \mathrm{kJ}$.

### Zadanie 4 — porównanie energii

$$E_{\mathrm{wody}}=4200\cdot2\cdot10=84\,000\ \mathrm{J}$$

$$E_{\mathrm{żelaza}}=4\cdot30\cdot450=54\,000\ \mathrm{J}$$

$$E_{\mathrm{wody}}>E_{\mathrm{żelaza}}$$

Nie dopisuj brakującej treści zadania. Zapis pokazuje obliczenie energii dla wody i żelaza oraz porównanie wyników.

### Zadanie 5 — grzałka

W zeszycie: „$t$ — czas [s]”, „$P$ — moc [W]”, „$W$ — praca [J]”.

Dane widoczne w obliczeniach: $P=1200\ \mathrm{W}$, $t=1\ \mathrm{min}=60\ \mathrm{s}$, $m=2\ \mathrm{kg}$, $c_w=4200\ \mathrm{J/(kg\cdot{}^\circ C)}$.

$$P=\frac{E}{t}\ \Rightarrow\ P\cdot t=E$$

$$E=1200\cdot60=72\,000\ \mathrm{J}$$

$$E=m c_w\Delta T$$

$$72\,000=2\cdot4200\cdot\Delta T$$

$$\Delta T=\frac{72\,000}{2\cdot4200}^\circ\mathrm{C}\approx8{,}6^\circ\mathrm{C}$$

Odp.: Temperatura wzrosła o około $8{,}6^\circ\mathrm{C}$.

To wzrost temperatury, a nie temperatura końcowa. Bez temperatury początkowej nie podawaj temperatury końcowej.

## 7. Przemiany fazowe, ciepło topnienia i parowania

### Nazwy przemian — przepisany schemat

| Stan początkowy | Stan końcowy | Przemiana |
|---|---|---|
| ciało stałe | ciecz | topnienie |
| ciecz | ciało stałe | krzepnięcie |
| ciecz | gaz | parowanie |
| gaz | ciecz | skraplanie |
| ciało stałe | gaz | sublimacja |
| gaz | ciało stałe | resublimacja |

### Parowanie i wrzenie — zapis z zeszytu

„Temp. topnienia (krzepnięcia) dla wody wynosi 0°C.”

„Woda paruje w każdej temp. ale tylko na powierzchni cieczy.”

„Wrzenie to gwałtowne parowanie w całej objętości cieczy.”

„Im wyższa temp. tym szybsze parowanie cieczy.”

„Żeby przyśpieszyć parowanie możemy zwiększyć powierzchnię cieczy.”

### Wykresy z zeszytu

**Ciało o budowie krystalicznej:** oś pionowa „temp.”, oś pozioma „energia”. Wykres zaczyna się przy $-5^\circ\mathrm{C}$, ma rosnący odcinek „ogrzewanie ciała”, poziomy odcinek „topnienie” i rosnący odcinek „ogrzewanie cieczy”. Podczas topnienia temperatura się nie zmienia mimo dostarczania energii.

**Ciało o budowie amorficznej:** pod rysunkiem zapisano: „Topnienie ciał bezpostaciowych odbywa się w szerokim zakresie temperatur.” Rysunek jest schematyczny; nie odczytuj z jego falowania dodatkowych praw fizycznych ani wartości liczbowych.

### Ciepło topnienia

„Ciepło topnienia — wielkość określająca ile energii potrzeba aby stopić 1 kg substancji [substancja jest już w temp. topnienia].”

$$E=m\cdot c_t$$

$E$ — energia [J], $m$ — masa [kg], $c_t$ — ciepło topnienia [J/kg].

### Ciepło parowania

„Ciepło parowania — energia potrzebna do odparowania 1 kg substancji [substancja jest w temp. wrzenia].”

$$E=m\cdot c_p$$

$E$ — energia, $m$ — masa, $c_p$ — ciepło parowania [J/kg].

### Bilans cieplny — początek zapisu z zeszytu

Pod nagłówkiem „Bilans cieplny” zapisano „1/38” i schemat:

lód $(-5^\circ\mathrm{C})$ → lód $(0^\circ\mathrm{C})$ → woda $(0^\circ\mathrm{C})$ → woda $(20^\circ\mathrm{C})$.

Pierwsza strzałka ma podpis „ogrzewanie”. Na zdjęciu nie ma dalszych obliczeń ani pełnej treści zadania. Rozpisanie wzorów dla tych trzech etapów znajduje się w sekcji 3.

## 8. Uwagi do źródeł i niejednoznacznych zapisów

- Źródła: pięć zdjęć zeszytu przekazanych 22.10.2026 oraz istniejące pliki w tym samym folderze: [[termodynamika_notatki]], [[Cząsteczki i energia GPTML]] i [[Prompt]].
- To połączona transkrypcja z osobno oznaczonymi dopowiedzeniami dla solwera. Nie jest fotograficzną reprodukcją układu stron. Rysunki opisano lub przepisano jako tabele.
- Zdjęcie 1: cząsteczki i energia. Zdjęcie 2: dalsza część energii wewnętrznej, I zasada, rozszerzalność. Zdjęcie 3: ciepło właściwe i zadania 3–5. Zdjęcie 4: szybkowar i przemiany fazowe. Zdjęcie 5: ciepło topnienia, parowania i początek bilansu.
- W notatce repozytorium błędnie nazwano poziom „szkołą podstawową”. Tutaj obowiązuje zakres podstawowy liceum.
- W dolnym powtórzeniu I zasady na zdjęciu 2 zapis przypomina $E_w=(\pm Q)+(\pm W)$ bez $\Delta$. Do zmiany energii stosuj $\Delta E_w$, zgodnie z wcześniejszym zapisem i legendą na tej samej stronie.
- Na zdjęciu 5 przy legendzie ciepła parowania napisano symbol wyglądający jak $c_t$, ale we wzorze jest $c_p$. Właściwa konwencja: $c_t$ — topnienie, $c_p$ — parowanie.
- Zapis zera bezwzględnego z zeszytu: $-273{,}15^\circ\mathrm{C}$; $-273^\circ\mathrm{C}$ jest zaokrągleniem.
- Fragment o szybkowarze na zdjęciu 4 jest przykładem języka wykraczającego poza oczekiwany styl. Nie naśladuj go i nie używaj go jako metody rozwiązywania. Dosłowny zapis do zachowania materiału źródłowego:

> Szybkowar stanowi zamknięty układ o wysokim oporze cieplnym, w którym niemal zerowa konwekcja zewnętrzna i stan równowagi ciecz–para nasycona eliminują straty utajonego ciepła parowania.
>
> Zgodnie z równaniem Clausiusa–Clapeyrona izobaryczny wzrost ciśnienia podnosi temperaturę wrzenia cieczy, co wykładniczo zwiększa kinetykę zachodzących wewnątrz procesów termochemicznych.

Ten fragment nie jest wzorcem poprawnego wyjaśnienia: „izobaryczny wzrost ciśnienia” to sprzeczny zapis, bo izobaryczny oznacza stałe ciśnienie. Do szkolnego pytania wystarczy: **„W szybkowarze panuje wyższe ciśnienie, dlatego woda wrze w wyższej temperaturze i potrawy gotują się szybciej.”**
