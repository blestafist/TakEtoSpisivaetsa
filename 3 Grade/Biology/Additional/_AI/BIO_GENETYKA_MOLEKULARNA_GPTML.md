# Biologia — genetyka molekularna — GPTML

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

---

## Instrukcja rozwiązywania zadań — genetyka molekularna

Korzystaj z dołączonego GPTML jako materiału odniesienia. Rozwiązuj zadania z zakresu: gen i kwasy nukleinowe, replikacja, kod genetyczny oraz ekspresja genów. Odpowiadaj po polsku, chyba że użytkownik wymaga innego języka. Podawaj odpowiedź zgodną z poleceniem oraz krótkie, sprawdzalne uzasadnienie lub obliczenie, kiedy jest potrzebne.

### Procedura

1. Odczytaj pełne polecenie, numer i podpunkty. Ustal, czy trzeba podać nazwę, wybrać odpowiedź, porównać, obliczyć, uporządkować etapy, zapisać sekwencję czy wyjaśnić mechanizm.
2. Dla zdjęcia zweryfikuj litery nukleotydów, strzałkę wskazującą matrycę, końce 5′/3′ i oznaczenia intronów. Jeżeli ważnego fragmentu nie da się odczytać, wskaż go zamiast zgadywać. Rozwiąż niezależne, czytelne podpunkty.
3. W obliczeniach określ, czy liczysz całą dwuniciową cząsteczkę, jedną nić, nukleotydy czy pary zasad. Równości A = T i G = C stosuj do całego dsDNA, a nie automatycznie do jednej nici lub RNA.
4. W zadaniu sekwencyjnym określ rodzaj nici, kierunek, introny i ramkę odczytu. Od matrycy twórz komplementarne RNA; od nici kodującej zamieniaj T→U po ujednoliceniu kierunku. Nie rozpoznawaj matrycy tylko po obecności TAC lub ATG.
5. Dla dojrzałego mRNA usuń oznaczone introny, zachowując kolejność eksonów. Nie tłumacz pre-mRNA, jeśli polecenie wymaga produktu po splicingu.
6. Czytaj mRNA 5′→3′ w ustalonej ramce. Sprawdź każdy kodon pełną tabelą. AUG koduje Met; pierwszy STOP w ramce kończy łańcuch i nie jest aminokwasem. Nie dodawaj brakującego START/STOP do podanego fragmentu.
7. Przy odtwarzaniu mRNA z aminokwasów wybierz po jednym poprawnym kodonie i zaznacz, że sekwencja jest przykładowa. Dodaj STOP, gdy wymaga go polecenie lub kompletny model. Nie twierdź, że odtworzyłeś jedyny oryginalny gen.
8. Przy procesach ustal typ komórki. Dla genu jądrowego eukarionta: replikacja i transkrypcja w jądrze, translacja na rybosomach poza jądrem. Odwrotna transkrypcja to RNA→DNA, a nie translacja.
9. Przy pytaniu „wyjaśnij / wykaż” połącz przyczynę z mechanizmem i skutkiem. Przy P/F oceniaj dokładne zdanie; przy fałszu podaj poprawienie, jeśli wymagane. Zwracaj uwagę na „zawsze”, „wyłącznie”, „każdy”, „jedna nić” i „po modyfikacjach”.
10. Sprawdź wynik: alfabet, kierunek, zgodność matrycy z mRNA, granice kodonów, STOP, liczbę aminokwasów, sumę nukleotydów/procentów i jednostki. Dopiero potem zapisz odpowiedź końcową.

### Format odpowiedzi

Zachowuj numerację zadań. W wyborze podaj literę i treść wyniku. W obliczeniach pokaż podstawienie oraz wynik z jednostką. Dla DNA→mRNA→białko podaj osobno mRNA z rozdzielonymi kodonami i łańcuch aminokwasów; STOP dopisz jako informację o zakończeniu, poza listą aminokwasów. Antykodony i zadania z określonym kierunkiem zapisuj z końcami 5′/3′.

Nie kopiuj odpowiedzi z klucza tylko po numerze zadania: porównaj jego dane i oznaczenia. Klucz w GPTML dotyczy konkretnych zadań z `bio.pdf`; inny wariant wymaga ponownego obliczenia.

Jeśli danych nie wystarcza do jednej odpowiedzi, podaj krótkie rozstrzygnięcie warunkowe albo poproś o konkretną brakującą informację. Nie zastępuj brakujących danych wymyśloną sekwencją. Nie deklaruj gwarancji bezbłędności — stosuj opisane kontrole.

---

## 1.1. Gen. Budowa i rola kwasów nukleinowych — GPTML

Źródło zakresu: `bio.pdf`, strony PDF 1–7 (strony podręcznika 6–12); powtórzenie na stronach PDF 16–17. Materiał dla modelu rozwiązującego szkolne zadania po polsku. Definicje są opracowane własnymi słowami; reguły oznaczone jako **doprecyzowanie** zabezpieczają przed nadmiernym uogólnieniem uproszczeń podręcznika.

### A. Pojęcia i zależności

**Gen** to odcinek DNA zawierający informację potrzebną do wytworzenia określonego produktu: RNA albo, za pośrednictwem RNA, polipeptydu. Gen jest jednostką dziedziczenia. Nie każdy gen koduje białko — geny kodujące tRNA lub rRNA prowadzą do powstania funkcjonalnego RNA.

**Informacja genetyczna** jest zapisana w kolejności nukleotydów. **Kod genetyczny** to reguły przyporządkowania kodonów aminokwasom lub sygnałowi STOP. Różne organizmy mają różne sekwencje DNA, chociaż posługują się zasadniczo tym samym kodem genetycznym.

W genie kodującym białko kolejność nukleotydów wpływa na kolejność aminokwasów, ta na budowę i działanie białka, a działanie białek na cechy organizmu. Nie oznacza to, że każda cecha zależy od jednego genu. Pigmentacja zależy od wielu genów i białek związanych m.in. z wytwarzaniem melanin; w podręczniku przykładem jest białko MC1R. Na cechy może również wpływać środowisko.

**Polipeptyd** to łańcuch aminokwasów połączonych wiązaniami peptydowymi. Nukleotydy budują kwasy nukleinowe, a aminokwasy budują białka — nie zamieniaj tych jednostek.

#### Budowa genu

| Element | Znaczenie | Co zrobić w zadaniu |
|---|---|---|
| Części regulatorowe | Uczestniczą w sterowaniu aktywnością genu: kiedy, gdzie i jak intensywnie powstaje jego produkt | Nie utożsamiaj ich z sekwencją kodującą aminokwasy |
| Część transkrybowana genu | Jest przepisywana na RNA; w szkolnym schemacie genu nieciągłego zawiera eksony i introny | Przy otrzymywaniu pre-mRNA uwzględnij oba rodzaje odcinków |
| Ekson | Odcinek zachowany w dojrzałym RNA po splicingu | Zachowaj go i połącz z kolejnymi eksonami |
| Intron | Odcinek transkrybowany, usuwany z pre-mRNA podczas splicingu | Usuń jego odpowiednik w RNA, a nie sąsiednie eksony |

W modelu szkolnym geny eukariotyczne z intronami są **nieciągłe**, a typowe geny bakteryjne bez intronów — **ciągłe**. **Doprecyzowanie:** nie każdy gen eukariotyczny ma introny. Ekson nie jest synonimem odcinka tłumaczonego na aminokwasy: eksony mogą również zawierać obszary nieulegające translacji. Introny nie są „bezużytecznym DNA”.

Informacja związana z genem może dotyczyć budowy produktu, jego wytwarzania w określonych komórkach i warunkach oraz kierowania produktu do odpowiedniej części komórki. Zapis „gen koduje białko” nie oznacza, że cała sekwencja genu zostanie przetłumaczona.

### B. DNA i RNA

**Nukleotyd** składa się z reszty fosforanowej, cukru pięciowęglowego i zasady azotowej. Cztery rodzaje nukleotydów danego kwasu różnią się zasadą azotową.

| Właściwość | DNA | RNA |
|---|---|---|
| Pełna nazwa | Kwas deoksyrybonukleinowy | Kwas rybonukleinowy |
| Cukier | Deoksyryboza | Ryboza |
| Zasady | A — adenina; T — tymina; G — guanina; C — cytozyna | A — adenina; U — uracyl; G — guanina; C — cytozyna |
| Typowa budowa w komórce | Dwie nici tworzące podwójną helisę | Jedna nić, mogąca tworzyć lokalne fragmenty dwuniciowe |
| Główna rola w tym rozdziale | Przechowywanie i przekazywanie informacji genetycznej | Udział w odczytywaniu informacji i syntezie białek |

Typowa lokalizacja DNA w komórce eukariotycznej to jądro. DNA jest także w mitochondriach, a u roślin również w chloroplastach. Nie pisz „DNA występuje wyłącznie w jądrze”. Prokarioty mają DNA, chociaż nie mają jądra komórkowego.

#### Komplementarność i wiązania

| Sytuacja | Poprawne pary |
|---|---|
| DNA z DNA | A–T i G–C |
| RNA z RNA | A–U i G–C |
| RNA powstające na matrycy DNA | DNA A → RNA U; DNA T → RNA A; DNA G → RNA C; DNA C → RNA G |

Pary zasad łączą **wiązania wodorowe**: A–T tworzy dwa, G–C trzy. Wzdłuż jednej nici nukleotydy są połączone wiązaniami fosfodiestrowymi tworzącymi szkielet cukrowo-fosforanowy. Nie myl połączeń między nićmi z połączeniami w jednej nici.

**Doprecyzowanie kierunku:** dwie nici DNA są antyrównoległe. Jeżeli jedna ma kierunek 5′→3′, druga biegnie 3′→5′. Sekwencje przedstawione w zadaniach bez końców 5′/3′ przepisuj zgodnie z układem rysunku; przy zadaniach z oznaczonymi końcami uwzględnij kierunek.

#### Trzy rodzaje RNA wymagane w rozdziale

| Rodzaj | Nazwa | Funkcja | Cechy rozpoznawcze na schemacie |
|---|---|---|---|
| mRNA | Informacyjny / matrycowy RNA | Zawiera informację o kolejności aminokwasów, odczytywaną przez rybosom | Nić z kolejnymi kodonami |
| tRNA | Transportujący RNA | Dostarcza określony aminokwas do rybosomu i rozpoznaje kodon mRNA | Miejsce przyłączenia aminokwasu oraz antykodon |
| rRNA | Rybosomowy RNA | Razem z białkami buduje rybosomy i uczestniczy w tworzeniu wiązań peptydowych | Składnik rybosomu |

**Antykodon** to trójka nukleotydów tRNA komplementarna do kodonu mRNA. Kodon należy do mRNA; antykodon do tRNA. tRNA nie przenosi całego białka. mRNA nie przenosi aminokwasów. rRNA nie jest białkiem.

### C. Organizacja DNA i replikacja

DNA wiąże się z białkami, m.in. histonami, tworząc **chromatynę**. Jej upakowanie umożliwia zmieszczenie długich cząsteczek DNA w jądrze. Chromosom jest jednostką organizacji DNA związanego z białkami; nie „pojawia się z niczego” dopiero podczas podziału.

Przed rozdzieleniem chromatyd zreplikowany chromosom ma **dwie chromatydy siostrzane**, połączone w regionie **centromeru**. Każda chromatyda zawiera jedną dwuniciową cząsteczkę DNA. Jedna chromatyda nie jest jedną nicią DNA. Chromosom w kształcie X jest jednym zreplikowanym chromosomem, a nie parą chromosomów homologicznych.

**Replikacja DNA** to kopiowanie DNA. Każda nić macierzystej cząsteczki stanowi matrycę do syntezy nowej nici komplementarnej. Powstają dwie cząsteczki potomne, każda zawierająca jedną nić starą i jedną nową — replikacja jest **semikonserwatywna**, czyli półzachowawcza.

Kolejność na schemacie: rozdzielenie nici DNA → dobudowanie komplementarnych nukleotydów → uzyskanie dwóch cząsteczek potomnych. **Polimeraza DNA** syntetyzuje nową nić; wiele polimeraz uczestniczących w replikacji również koryguje błędy. Bez błędów kopiowania sekwencje obu cząsteczek potomnych odpowiadają sekwencji cząsteczki macierzystej. Korekta błędów zmniejsza ryzyko mutacji, ale nie daje absolutnej bezbłędności.

W komórce eukariotycznej replikacja jądrowego DNA zachodzi w fazie S interfazy. Poprzedza mitozę oraz pierwszy podział mejotyczny. **Między mejozą I a mejozą II nie zachodzi kolejna replikacja.**

| Etap dla komórki o wyjściowym 2n = 46 | Chromosomy | Cząsteczki jądrowego DNA | Ilość DNA |
|---|---:|---:|---|
| Przed fazą S | 46 | 46 | 2c |
| Po fazie S, przed rozdzieleniem chromatyd | 46 | 92 | 4c |
| Jedna komórka potomna po mitozie | 46 | 46 | 2c |
| Jedna komórka po mejozie I | 23 | 46 | 2c |
| Jedna komórka po mejozie II | 23 | 23 | 1c |

Tabela dotyczy typowego diploidalnego modelu i nie liczy DNA organelli. `n` oznacza liczbę zestawów chromosomów, a `c` ilość DNA odpowiadającą jednemu niezreplikowanemu zestawowi haploidalnemu. Replikacja podwaja ilość DNA, ale sama nie podwaja liczby chromosomów. Liczbę chromosomów ustala się według liczby centromerów; po rozdzieleniu chromatyd każda staje się samodzielnym chromosomem.

Mitoza w tym modelu prowadzi do dwóch komórek o tej samej liczbie chromosomów co komórka wyjściowa. Mejoza obejmuje dwa podziały i prowadzi do czterech komórek haploidalnych. Nie przedstawiaj produktów mejozy jako czterech genetycznie identycznych kopii.

### D. Algorytmy rozwiązywania

#### D1. Uzupełnianie drugiej nici DNA

1. Ustal, czy wynik ma być DNA, czy RNA.
2. Dla DNA dobieraj A↔T i G↔C, zachowując liczbę pozycji.
3. Jeśli podano końce, druga nić ma przeciwny kierunek.
4. Jeśli wynik musi być zapisany 5′→3′, odwróć kolejność komplementarnej nici zapisanej pierwotnie 3′→5′.

Przykład: nić `5′-ATGCCA-3′` ma partnera `3′-TACGGT-5′`. Ten sam partner zapisany 5′→3′ to `5′-TGGCAT-3′`. Zwykłe `TACGGT` oraz odwrotna sekwencja komplementarna `TGGCAT` odpowiadają różnym kierunkom zapisu tej samej nici.

#### D2. Liczby i procenty nukleotydów

Najpierw ustal zakres danych: **cała dwuniciowa cząsteczka**, **jedna nić** czy **liczba par zasad**. Poniższe równości obowiązują dla całej dwuniciowej cząsteczki DNA:

`A = T`, `G = C`, `A + T + G + C = N`, `A% + T% + G% + C% = 100%`.

| Dane | Wniosek |
|---|---|
| A = x | T = x; G = C = (N − 2x) / 2 |
| C = x | G = x; A = T = (N − 2x) / 2 |
| A% = p albo T% = p | A% = T% = p; G% = C% = (100 − 2p) / 2 |
| G% = p albo C% = p | G% = C% = p; A% = T% = (100 − 2p) / 2 |
| P par zasad | Łącznie N = 2P nukleotydów; każda nić ma P nukleotydów |

**Nie stosuj automatycznie A = T ani G = C do pojedynczej nici DNA lub jednoniciowego RNA.** W pojedynczej nici może być dowolny skład zgodny z podaną sekwencją. W drugiej nici `A₂ = T₁`, `T₂ = A₁`, `G₂ = C₁`, `C₂ = G₁`. Skład całej cząsteczki oblicz przez zsumowanie obu nici, a nie przez przepisanie procentów z jednej.

Jeśli określenie „odcinek DNA” w szkolnym zadaniu oznacza cząsteczkę i nic nie wskazuje na jedną nić, przyjmij model dwuniciowy. Gdy zadanie wyraźnie dotyczy jednej nici, nie dodawaj brakujących informacji. Przy niejednoznaczności podaj przyjęte założenie.

#### D3. Sprawdzenie wyniku

Suma udziałów musi wynosić 100%, liczby nie mogą być ujemne ani ułamkowe, a dwuniciowa cząsteczka ma parzystą liczbę nukleotydów. Jeśli wynik przeczy tym warunkom, sprawdź dane, OCR i interpretację jednostek. Nie zaokrąglaj liczby nukleotydów, aby ukryć sprzeczność.

**Uzupełnienie obliczeniowe:** gdy znane są liczby nukleotydów w całym dsDNA, liczba par A–T wynosi A, a par G–C wynosi G. Liczba wiązań wodorowych to `H = 2A + 3G`. Nie pomnóż jeszcze raz A i G przez dwa.

### E. Przykłady wzorcowe i odpowiedzi do źródła

#### E1. Przykład z podręcznika, s. 12

Cała cząsteczka: N = 250, C = 75. Z komplementarności G = 75. Na A i T pozostaje `250 − 150 = 100`, więc A = T = 50. **Odpowiedź: 50 nukleotydów z tyminą.** Kontrola: `50 + 50 + 75 + 75 = 250`.

#### E2. Polecenie kontrolne 1, s. 12

T = 36%, więc A = 36%. Pozostaje `100% − 72% = 28%`, zatem C = G = 14%. **Odpowiedź: A 36%, C 14%, G 14%.** Nie wpisuj 28% dla każdej z dwóch pozostałych zasad.

#### E3. Polecenie kontrolne 2, s. 12

**Odpowiedź:** mRNA zawiera informację o kolejności aminokwasów i stanowi matrycę translacji; tRNA dostarcza aminokwasy, rozpoznając kodony mRNA antykodonem; rRNA razem z białkami tworzy rybosom i uczestniczy w syntezie polipeptydu.

#### E4. Polecenie kontrolne 3, s. 12

**Odpowiedź:** dokładne kopiowanie DNA pozwala przekazać komórkom potomnym właściwą informację genetyczną. Utrwalony błąd może zmienić produkt genu lub regulację jego wytwarzania, a w konsekwencji zaburzyć funkcjonowanie komórki. Nie twierdź, że każda mutacja musi zmienić aminokwas lub być szkodliwa.

#### E5. Jedna nić — zadanie zabezpieczające

W jednej nici jest A = 10, T = 20, G = 30, C = 40. W partnerze jest A = 20, T = 10, G = 40, C = 30. W całym DNA: A = T = 30 oraz G = C = 70; łącznie 200 nukleotydów. Udziały całej cząsteczki wynoszą 15%, 15%, 35%, 35%.

#### E6. Pary zasad i wiązania — zadanie zabezpieczające

Cząsteczka ma 100 par zasad, w tym 40 par G–C. Pozostaje 60 par A–T. Całe DNA zawiera 200 nukleotydów: A = T = 60, G = C = 40. Wiązania wodorowe: `60 × 2 + 40 × 3 = 240`.

#### E7. Zadania końcowe, s. 23

| Numer | Odpowiedź | Uzasadnienie / kontrola |
|---|---|---|
| 1.1 | P | Kolejność aminokwasów wynika z kolejności kodonów mRNA |
| 1.2 | P | Białka powstające według informacji w genach wpływają na cechy |
| 2 | 104 nukleotydy z guaniną | N = 300, A = T = 46, G = C = (300 − 92) / 2 = 104 |
| 3 | C: 16% | T = A = 34%, G = C = (100 − 68) / 2 = 16% |
| 4 | deoksyryboza; tymina; dwie nici | Trzy wybory opisują DNA, a nie RNA |
| 5 | uracyl, U | Zadanie dotyczy RNA, więc partnerem adeniny jest U |

### F. Pułapki i kryteria poprawnej odpowiedzi

| Błędna odpowiedź | Poprawna reguła |
|---|---|
| „Każdy gen koduje białko” | Niektóre geny kodują funkcjonalne RNA |
| „DNA i RNA różnią się tylko T/U” | Różnią się również cukrem i typową liczbą nici |
| „Cukier w DNA to ryboza” | W DNA jest deoksyryboza |
| „RNA jest zawsze prostą, niesparowaną nicią” | Jedna nić może się złożyć i lokalnie sparować |
| „Po replikacji człowiek ma 92 chromosomy” | Przed rozdzieleniem chromatyd ma 46 chromosomów z 92 cząsteczkami jądrowego DNA |
| „Chromatyda to jedna nić DNA” | Chromatyda zawiera dwuniciową cząsteczkę DNA |
| „W jednej potomnej cząsteczce są dwie stare nici” | Każda zawiera starą i nową nić |
| „Przed każdym z dwóch podziałów mejozy jest replikacja” | Replikacja poprzedza mejozę I, nie mejozę II |

Przed oddaniem odpowiedzi sprawdź: właściwy kwas, właściwy cukier i alfabet, zakres obliczeń, jednostkę nukleotyd/par zasad, sumę wyników oraz odróżnienie liczby chromosomów od ilości DNA.

### G. Źródła doprecyzowań

- [NHGRI — Exon](https://www.genome.gov/genetics-glossary/Exon) i [Intron](https://www.genome.gov/genetics-glossary/Intron): zachowanie eksonów i usuwanie intronów z dojrzałego transkryptu.
- [NCBI Bookshelf — Meiosis](https://www.ncbi.nlm.nih.gov/books/NBK26840/): jedna replikacja poprzedza dwa podziały mejotyczne.
- [NHGRI — RNA Fact Sheet](https://www.genome.gov/about-genomics/educational-resources/fact-sheets/ribonucleic-acid-fact-sheet): różne funkcje RNA, lokalne parowanie i splicing.

---

## 1.2. Kod genetyczny — GPTML

Źródło zakresu: `bio.pdf`, strony PDF 8–11 (strony podręcznika 13–16); powtórzenie i zadania na stronach PDF 17 i 19. Stosuj standardowy kod genetyczny oraz szkolny model rozpoczynania translacji od AUG, chyba że polecenie podaje inny kontekst.

### A. Definicje i sześć cech kodu

**Kod genetyczny** to sposób przyporządkowania trójkom nukleotydów informacji o aminokwasach i zakończeniu translacji. **Kodon** składa się z trzech kolejnych nukleotydów. Tabela używana w tych zadaniach dotyczy kodonów mRNA zapisanych 5′→3′.

Cztery zasady i trzy pozycje dają `4³ = 64` kodony. W standardowym kodzie 61 kodonów oznacza aminokwasy, a 3 to STOP. AUG oznacza metioninę i pełni funkcję kodonu START. W środku sekwencji kodującej AUG nadal oznacza metioninę — nie rozpoczynaj automatycznie nowego białka przy każdym AUG.

| Cecha | Znaczenie | Jak rozpoznać ją w zadaniu |
|---|---|---|
| Trójkowy | Jednostką odczytu jest trójka nukleotydów | Każdy kodon ma trzy pozycje |
| Jednoznaczny | Dany kodon ma jedno określone znaczenie: aminokwas albo STOP | Jeden kodon nie oznacza kilku różnych aminokwasów |
| Zdegenerowany | Ten sam aminokwas może być kodowany przez różne kodony | Np. GUU, GUC, GUA i GUG oznaczają walinę |
| Bezprzecinkowy | W odczytywanym odcinku między kolejnymi kodonami nie ma nukleotydowych „przecinków” | Odczyt jest ciągły w danej ramce |
| Niezachodzący | W jednej ramce nukleotyd odczytany w kodonie nie należy do następnego kodonu | Pozycje 1–3, 4–6, 7–9, a nie 1–3, 2–4, 3–5 |
| Uniwersalny | Zasadniczo te same kodony mają to samo znaczenie u różnych organizmów | Chodzi o wspólne reguły kodowania, nie o identyczne DNA wszystkich gatunków |

Jednoznaczność i zdegenerowanie nie przeczą sobie: **kodon ma jedno znaczenie, ale aminokwas może mieć kilka kodonów**. W standardowym kodzie metionina i tryptofan mają po jednym kodonie, więc nie pisz, że każdy aminokwas musi mieć kilka.

**Doprecyzowanie:** uniwersalność ma wyjątki, m.in. w kodach mitochondrialnych. Bezprzecinkowość nie oznacza, że całe mRNA jest tłumaczone: może zawierać regiony nieulegające translacji. Niezachodzenie odnosi się do odczytu jednej ramki; nie jest twierdzeniem o niemożności nakładania się genów w genomie.

### B. Pełna tabela standardowego kodu — 64 kodony

Wszystkie kodony poniżej są zapisane alfabetem RNA i w kierunku 5′→3′. `STOP` nie jest aminokwasem. Nazwy i skróty odnoszą się do tej samej substancji.

| Aminokwas / sygnał | Skrót | Kodony mRNA |
|---|---|---|
| Fenyloalanina | Phe | UUU, UUC |
| Leucyna | Leu | UUA, UUG, CUU, CUC, CUA, CUG |
| Izoleucyna | Ile | AUU, AUC, AUA |
| Metionina | Met | AUG |
| Walina | Val | GUU, GUC, GUA, GUG |
| Seryna | Ser | UCU, UCC, UCA, UCG, AGU, AGC |
| Prolina | Pro | CCU, CCC, CCA, CCG |
| Treonina | Thr | ACU, ACC, ACA, ACG |
| Alanina | Ala | GCU, GCC, GCA, GCG |
| Tyrozyna | Tyr | UAU, UAC |
| Histydyna | His | CAU, CAC |
| Glutamina | Gln | CAA, CAG |
| Asparagina | Asn | AAU, AAC |
| Lizyna | Lys | AAA, AAG |
| Kwas asparaginowy | Asp | GAU, GAC |
| Kwas glutaminowy | Glu | GAA, GAG |
| Cysteina | Cys | UGU, UGC |
| Tryptofan | Trp | UGG |
| Arginina | Arg | CGU, CGC, CGA, CGG, AGA, AGG |
| Glicyna | Gly | GGU, GGC, GGA, GGG |
| Zakończenie translacji | STOP | UAA, UAG, UGA |

W tabeli prostokątnej ze skanu znajdź pierwszą zasadę w lewym opisie, drugą w górnym opisie, a trzecią wewnątrz odpowiedniego pola zgodnie z prawym opisem. Przykład: G → C → A daje GCA, czyli alaninę. W tabeli kołowej czytaj kolejne pozycje od środka na zewnątrz. Nie zmieniaj kolejności liter w kodonie.

### C. mRNA, nić matrycowa i nić kodująca

Dla konkretnego transkryptu tylko jedna nić DNA jest **matrycowa**. Druga jest **kodująca**. Określenie „kodująca” nie oznacza, że to z niej polimeraza RNA odczytuje matrycę.

| Dane wejściowe | Operacja prowadząca do mRNA 5′→3′ |
|---|---|
| Nić kodująca DNA 5′→3′ | Zachowaj kolejność i zamień T na U |
| Nić matrycowa DNA 3′→5′ | Zapisz komplementarne RNA: A→U, T→A, C→G, G→C |
| Nić matrycowa DNA 5′→3′ | Zapisz odwrotną sekwencję komplementarną RNA |
| Nić kodująca DNA 3′→5′ | Najpierw odwróć zapis do 5′→3′, potem zamień T na U |
| Obie nici na rysunku bez końców, jedna wskazana jako matrycowa | Dobierz komplementarne RNA w kolejności pokazanej w szkolnym schemacie; nie odwracaj go samowolnie |
| Pojedyncza sekwencja DNA bez wskazania rodzaju nici i bez rozstrzygającego kontekstu | Nie wybieraj matrycy po wyglądzie; poproś o oznaczenie lub podaj odpowiedzi warunkowe |

Model kierunkowy na jednym przykładzie:

- DNA kodujące: `5′-ATG CCT GCC AAA TAA-3′`.
- DNA matrycowe: `3′-TAC GGA CGG TTT ATT-5′`.
- mRNA: `5′-AUG CCU GCC AAA UAA-3′`.
- Polipeptyd: **Met–Pro–Ala–Lys**; UAA kończy translację.

**Kontrola podwójna:** mRNA musi być komplementarne do matrycy oraz zgodne z nicią kodującą po zamianie T→U, jeśli porównujesz zapisy w tych samych kierunkach.

### D. Algorytmy zadań sekwencyjnych

#### D1. DNA → mRNA → polipeptyd

1. Przepisz dokładnie litery sekwencji. Nie zgaduj nieczytelnego nukleotydu. Odczytaj strzałkę i oznaczenie nici.
2. Ustal kierunek oraz obecność intronów. Jeśli wynik ma być dojrzałym mRNA, usuń oznaczone introny przez splicing.
3. Utwórz mRNA zgodnie z tabelą w części C. Sprawdź brak T w wyniku.
4. Ustal ramkę odczytu. Dla kompletnego szkolnego odcinka od START do STOP zacznij od wskazanego AUG. Dla fragmentu z podaną ramką tłumacz od jej początku, nawet gdy nie zaczyna się od AUG.
5. Dziel mRNA na niepokrywające się trójki. Nie przesuwaj granic, aby otrzymać „ładniejszą” odpowiedź.
6. Przypisz każdemu kodonowi aminokwas z tabeli. Zakończ na pierwszym STOP w tej samej ramce. Nie tłumacz dalszej sekwencji jako części tego polipeptydu.
7. Podaj mRNA i łańcuch, jeżeli oba były wymagane; STOP opisz osobno.

Brak AUG w podanym fragmencie nie dowodzi, że fragment nie koduje aminokwasów — może leżeć wewnątrz części kodującej. Brak STOP może oznaczać niepełny fragment. Przy pełnym mRNA bez wskazanego miejsca inicjacji kilka AUG może dawać niejednoznaczność; nie przedstawiaj dowolnie wybranej ramki jako jedynej pewnej.

Niepełna trójka na końcu fragmentu nie koduje kompletnego aminokwasu. Zgłoś pozostałe 1–2 nukleotydy. Nie dopisuj brakujących liter i nie zakładaj, że dowodzą błędnej sekwencji biologicznej — fragment może kończyć się w środku kodonu.

#### D2. Antykodon tRNA

Kodon `5′-AUG-3′` paruje w szkolnym modelu z antykodonem `3′-UAC-5′`. Ten sam antykodon zapisany 5′→3′ to `5′-CAU-3′`. Jeśli polecenie nie podaje kierunku, wpisz końce, aby uniknąć niejednoznaczności.

Do kodonu STOP w standardowym szkolnym modelu nie dopasowuj tRNA z „aminokwasem STOP”. Zakończenie rozpoznają czynniki uwalniające. Uproszczone ścisłe parowanie wystarcza w tych zadaniach; mechanizm wobble stosuj dopiero, gdy polecenie go wymaga.

#### D3. Aminokwasy → przykładowe mRNA → DNA

1. Dla każdego aminokwasu wybierz **jeden** poprawny kodon. Zachowaj kolejność aminokwasów.
2. Dodaj kodon STOP, jeśli wymaga tego polecenie; dla kompletnej sekwencji użyj jednego z UAA/UAG/UGA.
3. Nie dodawaj dodatkowego AUG przed podaną metioniną — jej AUG już pełni funkcję START w kompletnym szkolnym przykładzie.
4. Połącz kodony i nazwij wynik **przykładową**, a nie jedyną możliwą sekwencją.
5. Jeśli potrzebna jest matryca DNA, dobierz A→T, U→A, C→G, G→C i zapisz partnera RNA 5′→3′ jako DNA 3′→5′. Nić kodująca powstaje przez U→T bez komplementowania.
6. Odczytaj własne mRNA ponownie tabelą. Łańcuch musi dokładnie odpowiadać wejściu.

Z aminokwasów można uzyskać wiele poprawnych sekwencji, ponieważ kod jest zdegenerowany. Bez dodatkowych danych nie można odtworzyć dokładnej oryginalnej sekwencji genu, jego intronów ani części regulatorowych.

#### D4. Długości — zakres obowiązywania wzorów

Jeżeli sekwencja zawiera wyłącznie kodony dla `k` aminokwasów oraz jeden końcowy STOP, ma `3(k + 1)` nukleotydów. AUG kodujący początkową metioninę jest już wśród tych k kodonów. Dla fragmentu bez STOP k kompletnych kodonów to 3k nukleotydów.

Przykład: odcinek mRNA od AUG do UAA włącznie ma 303 nukleotydy. Zawiera 101 kodonów, z których jeden to STOP, więc koduje **100 aminokwasów**. Odpowiadający mu odcinek jednej nici DNA ma 303 nukleotydy, a dwuniciowy odcinek DNA — 303 pary zasad, czyli 606 nukleotydów.

Nie stosuj `długość mRNA / 3 − 1` do całego dowolnego mRNA ani genu z intronami. Regiony nieulegające translacji, introny i ogon poli(A) nie są automatycznie częścią sekwencji kodującej.

### E. Przykłady ze skanu i klucz kontrolny

Spacje w zapisach poniżej jedynie wyznaczają kodony; nie są elementem cząsteczki.

#### E1. Schemat, s. 13 — fragment wewnętrzny

DNA kodujące `CGG AGC GCA TGA`, DNA matrycowe `GCC TCG CGT ACT`.

**mRNA:** `CGG AGC GCA UGA`. **Łańcuch:** Arg–Ser–Ala. UGA jest STOP. Fragment nie zaczyna się od AUG, ale w schemacie podano ramkę odczytu, więc odczytujemy przedstawione kodony.

#### E2. Przykład krok po kroku, s. 15

DNA matrycowe `TAC GGA CGG TTT ATT` daje mRNA `AUG CCU GCC AAA UAA` i łańcuch **Met–Pro–Ala–Lys**. To 15 nukleotydów, 5 kodonów i 4 aminokwasy.

#### E3. Odtwarzanie mRNA, s. 16

Łańcuch Met–Arg–His–Cys–Leu–Tyr można zapisać jako `AUG AGA CAC UGU CUA UAU UGA`. To **sześć aminokwasów**, siedem kodonów i 21 nukleotydów. Sformułowanie o „pięciu” aminokwasach w podpisie przykładowej odpowiedzi na skanie jest omyłką; wymieniono sześć.

#### E4. Polecenie kontrolne 1, s. 16

mRNA ze skanu: `AUGCCGGGCAUCUUUACGUAA`.

Podział: `AUG CCG GGC AUC UUU ACG UAA`.

**Odpowiedź:** metionina–prolina–glicyna–izoleucyna–fenyloalanina–treonina. UAA kończy translację i nie dodaje siódmego aminokwasu.

#### E5. Polecenie kontrolne 2, s. 16

DNA kodujące: `ATG CCG AGC CAA CGC ACT`.

Wskazana matryca: `TAC GGC TCG GTT GCG TGA`.

**mRNA:** `AUG CCG AGC CAA CGC ACU`.

**Łańcuch:** metionina–prolina–seryna–glutamina–arginina–treonina. Nie dopisuj STOP: podano fragment bez kodonu STOP. Końcowe TGA jest w **matrycy**, więc daje ACU, a nie UGA. To celowo ważne rozróżnienie.

#### E6. Polecenie kontrolne 3, s. 16

Met–Ser–Gly–Ala–Trp; przykład z wymaganym STOP: `AUG UCU GGU GCU UGG UAA`. Inne kodony dla Ser/Gly/Ala i inny STOP mogą dawać równie poprawną odpowiedź.

#### E7. Zadanie końcowe 9, s. 24

Matryca wskazana strzałką: `AGCCATGG`. Komplementarne mRNA w układzie rysunku: **`UCGGUACC`**, czyli **odpowiedź B**. Odpowiedź z T nie może być poprawnym RNA. Zamiana T→U w samej matrycy daje niewłaściwy wynik.

#### E8. Zadanie końcowe 10, s. 24

mRNA: `AUGCUAAGGGACCGUAUUUAA`.

Podział: `AUG CUA AGG GAC CGU AUU UAA`.

**Odpowiedź:** metionina–leucyna–arginina–kwas asparaginowy–arginina–izoleucyna. 21 nukleotydów, 7 kodonów i 6 aminokwasów.

#### E9. Zadanie końcowe 11, s. 24

Met–Ala–Ser–Gly–Lys–Val. Jedna poprawna para sekwencji:

- mRNA: `5′-AUG GCU UCU GGU AAA GUU UAA-3′`.
- DNA matrycowe: `3′-TAC CGA AGA CCA TTT CAA ATT-5′`.

Kontrola: kodony dają dokładnie sześć wymaganych aminokwasów, a UAA jest STOP. Nie oceniaj innych poprawnych wyborów synonimicznych kodonów jako błędnych.

#### E10. Zadanie końcowe 12, s. 24

**Jednoznaczność: schemat B. Zdegenerowanie: schemat C.** W B każdy kodon ma pojedyncze znaczenie. W C kilka kodonów prowadzi do tego samego aminokwasu. Schemat A, gdzie jeden kodon prowadzi do różnych aminokwasów, nie przedstawia poprawnej reguły standardowego kodu.

### F. Dodatkowe zadania zabezpieczające

#### F1. Matryca podana 5′→3′

DNA matrycowe: `5′-TTATTTCAT-3′`. Po odwróceniu: `3′-TACTTTATT-5′`. mRNA: `5′-AUG AAA UAA-3′`. Łańcuch: **Met–Lys**. Bez odwrócenia otrzymano by RNA w niewłaściwym kierunku do translacji.

#### F2. STOP w środku

mRNA w podanej ramce: `AUG GCU UGA AAA`. Łańcuch: **Met–Ala**. Po UGA translacja tego łańcucha się kończy, więc AAA nie dodaje lizyny.

#### F3. Nieznany rodzaj nici

Dla DNA `ATGAAA` bez oznaczeń nie ma jednej pewnej odpowiedzi. Jeśli to nić kodująca 5′→3′, mRNA = `5′-AUGAAA-3′`. Jeśli to matryca 3′→5′, mRNA = `5′-UACUUU-3′`. Jeśli to matryca 5′→3′, mRNA = `5′-UUUCAU-3′`. Nie wybieraj pierwszej możliwości tylko dlatego, że zaczyna się od ATG.

#### F4. Zmiana kodonu — uzupełnienie

GCU→GCC nadal oznacza alaninę: zmiana synonimiczna. GCU→GUU zmienia alaninę na walinę. UAU→UAA w części kodującej może przedwcześnie zakończyć translację. Wstawienie lub usunięcie liczby nukleotydów niepodzielnej przez trzy w tłumaczonym odcinku zwykle zmienia ramkę dalszego odczytu. Nie twierdź, że zdegenerowanie chroni przed każdą mutacją.

### G. Lista kontroli dla modelu

Wynik ma poprawny alfabet; nić i kierunek są ustalone; introny uwzględniono zgodnie z poleceniem; ramki nie przesunięto; każdy pełny kodon sprawdzono tabelą; AUG policzono jako Met; STOP nie policzono jako aminokwas; translacji nie kontynuowano za STOP; przy zadaniu odwrotnym wynik nazwano przykładowym.

### H. Źródła doprecyzowań

- [NCBI — The Genetic Codes, tabela standardowa 1](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/genetic-codes/): wzorzec przyporządkowania wszystkich 64 kodonów. NCBI zapisuje w tabeli T; tutaj zastąpiono je U, aby przedstawić kodony mRNA.
- [NHGRI — Codon](https://www.genome.gov/genetics-glossary/Codon): 61 kodonów aminokwasowych i trzy sygnały STOP.
- [NCBI Bookshelf — From DNA to RNA](https://www.ncbi.nlm.nih.gov/books/NBK26887/): synteza RNA 5′→3′ na matrycy odczytywanej 3′→5′.

---

## 1.3. Ekspresja genów — GPTML

Źródło zakresu: `bio.pdf`, strony PDF 12–15 (strony podręcznika 17–20); powtórzenie na stronach PDF 16–17 i zadania na stronach PDF 18–19. Główny model dotyczy ekspresji jądrowego genu kodującego białko w komórce eukariotycznej.

### A. Czym jest ekspresja genu?

**Ekspresja genu** to wykorzystanie zapisanej w genie informacji do wytworzenia jego produktu — funkcjonalnego RNA lub polipeptydu. Dla genu kodującego białko obejmuje transkrypcję i translację, a u eukariontów także obróbkę transkryptu. Dla genu kodującego tRNA lub rRNA nie ma etapu tłumaczenia tego RNA na białko.

W typowych komórkach somatycznych organizmu występuje zasadniczo ten sam genom, lecz różne geny są aktywne z różną intensywnością. Dzięki temu powstają komórki o różnych właściwościach i funkcjach. Nie tłumacz różnic między neuronem a komórką wątroby tym, że każda zawiera zupełnie inny zestaw genów.

**Doprecyzowanie:** zdanie „wszystkie komórki mają to samo DNA” jest szkolnym uproszczeniem. Gamety mają inny zestaw chromosomów, dojrzałe erytrocyty człowieka nie mają jądra, a część komórek może mieć mutacje lub zmienioną ploidalność. Przy typowym pytaniu o różnicowanie komórek odpowiedź dotyczy jednak regulacji ekspresji, a nie tych wyjątków.

### B. Kolejność i miejsca procesów

| Kolejność | Proces | Co powstaje / co się zmienia | Miejsce w głównym modelu |
|---|---|---|---|
| 1 | Transkrypcja | RNA powstaje na matrycy DNA; dla genu kodującego białko powstaje pre-mRNA | Jądro komórkowe |
| 2 | Modyfikacje potranskrypcyjne | Pre-mRNA dojrzewa; m.in. usuwa się introny i łączy eksony | Jądro komórkowe |
| 3 | Eksport mRNA | Dojrzałe mRNA przechodzi przez pory jądrowe | Z jądra do cytozolu |
| 4 | Translacja | Według kodonów mRNA powstaje polipeptyd | Rybosomy po cytoplazmatycznej stronie komórki: wolne lub związane z RER |
| 5 | Fałdowanie i ewentualne modyfikacje białka | Produkt uzyskuje odpowiednią strukturę i właściwości | Zależnie od białka: m.in. cytozol, RER, aparat Golgiego |

Fałdowanie może zaczynać się już w czasie translacji, a szczegółowe modyfikacje zależą od białka. Do szkolnego porządkowania zdarzeń użyj kolejności przedstawionej w tabeli. Nie utożsamiaj „genu” z „gotowym białkiem” ani eksportu mRNA z translacją.

#### Porównanie trzech często mylonych procesów

| Cecha | Replikacja | Transkrypcja | Translacja |
|---|---|---|---|
| Informacja / matryca | DNA | DNA | mRNA |
| Bezpośredni produkt | DNA | RNA | Polipeptyd |
| Główne wykonawstwo | Polimeraza DNA i pozostałe enzymy replikacji | Polimeraza RNA | Rybosom, tRNA i czynniki translacji |
| Zakres | Kopiowanie materiału DNA przed podziałem | Przepisywanie wybranych odcinków na RNA | Odczyt części kodującej mRNA |
| Komplementarność | DNA z DNA | DNA z RNA | Kodon mRNA z antykodonem tRNA |
| Miejsce dla jądrowego genu eukarionta | Jądro | Jądro | Rybosomy poza jądrem |

U bakterii nie ma jądra: transkrypcja i translacja zachodzą w komórce bez rozdzielenia otoczką jądrową i mogą być sprzężone. Nie stosuj odpowiedzi „w jądrze” do zadania o bakterii. DNA mitochondriów i chloroplastów jest odrębnym kontekstem; tabela opisuje głównie materiał jądrowy.

### C. Transkrypcja i dojrzewanie RNA

Polimeraza RNA wiąże się z odpowiednim regionem DNA wraz z czynnikami uczestniczącymi w rozpoczęciu transkrypcji. Lokalnie odsłania matrycę, a następnie dołącza nukleotydy RNA zgodnie z komplementarnością. Odczytuje matrycę 3′→5′ i wydłuża RNA 5′→3′. DNA nie jest zużywane ani zamieniane chemicznie w RNA; po przejściu polimerazy nici DNA mogą się ponownie połączyć.

Dla danego transkryptu kopiowana jest jedna nić matrycowa. W innych genach matrycą może być druga nić DNA. Nie wyciągaj wniosku, że jedna nić całego chromosomu jest zawsze kodująca, a druga zawsze matrycowa.

W genie zawierającym introny pierwotny transkrypt pre-mRNA zawiera odpowiedniki eksonów i intronów. **Splicing** usuwa introny z RNA i łączy eksony. Standardowy splicing RNA nie wycina intronów z genomowego DNA.

**Doprecyzowanie:** nie każda część regulatorowa genu jest transkrybowana. Nie utożsamiaj zdania „transkrypcji podlegają eksony i introny” ze stwierdzeniem, że cały otaczający je obszar DNA znajdzie się w RNA.

W zakresie skanu główną wymaganą modyfikacją jest splicing. Typowa obróbka eukariotycznego pre-mRNA obejmuje również dodanie czapeczki 5′ i obróbkę końca 3′, często z ogonem poli(A). Te elementy są **uzupełnieniem**; w zadaniu opartym wyłącznie na oznaczonych eksonach i intronach nie dopisuj arbitralnie długości czapeczki ani ogona poli(A).

**Alternatywny splicing — uzupełnienie:** różne zestawienia eksonów z tego samego transkryptu mogą prowadzić do różnych mRNA i produktów białkowych. Nie zmieniaj jednak zestawu eksonów w zwykłym zadaniu, jeśli nie podano wariantu splicingu.

#### Algorytm: nić matrycowa z intronami → dojrzałe mRNA

1. Odczytaj oznaczenia eksonów i intronów: kolory, nawiasy, podkreślenia lub numery. Sam ciąg liter nie zawiera tej informacji.
2. Ustal, czy wejście to DNA matrycowe, kodujące czy pre-mRNA. Ustal kierunek zapisu.
3. Dla DNA matrycowego utwórz komplementarny transkrypt RNA. Zaznacz w nim granice odpowiadające intronom.
4. Usuń wyłącznie introny i połącz eksony w niezmienionej kolejności.
5. Sprawdź, że wynik jest RNA i jego długość odpowiada sumie zachowanych odcinków.
6. Jeżeli polecenie wymaga również polipeptydu, ustal ramkę już w **dojrzałym** mRNA; granica kodonu może wypadać na połączeniu eksonów.

Możesz rachunkowo najpierw skleić oznaczone eksony DNA, a potem utworzyć odpowiadający im RNA — wynik sekwencyjny będzie ten sam przy zachowaniu kierunku. Opisując proces biologiczny, napisz jednak, że introny są wycinane z pre-mRNA.

Jeśli kolory zniknęły w OCR lub zdjęcie nie pozwala ustalić granic, wskaż dokładnie brakującą informację i poproś o oznaczenie intronów. Nie uznawaj fragmentu za intron dlatego, że ma „dziwny” kodon lub długość niepodzielną przez trzy.

### D. Translacja i funkcjonalne białko

Rybosom wiąże mRNA. W szkolnym modelu inicjacji tRNA z metioniną rozpoznaje AUG. Kolejne tRNA dostarczają aminokwasy zgodne z kolejnymi kodonami. Między aminokwasami powstają wiązania peptydowe, a rybosom przesuwa się po mRNA w kierunku 5′→3′ o trzy nukleotydy na krok. Po oddaniu aminokwasu tRNA może zostać ponownie wykorzystane.

Rozpoznanie UAA, UAG lub UGA w aktualnej ramce kończy translację. Polipeptyd zostaje uwolniony; STOP nie dodaje aminokwasu. Bezpośrednią matrycą translacji jest mRNA, a nie DNA ani tRNA.

| Składnik | Precyzyjna rola |
|---|---|
| mRNA | Kolejność jego kodonów wyznacza kolejność aminokwasów |
| tRNA | Łączy rozpoznanie kodonu z dostarczeniem właściwego aminokwasu |
| Antykodon | Komplementarnie paruje z kodonem mRNA w szkolnym modelu |
| Rybosom | Organizuje odczyt mRNA i powstawanie polipeptydu |
| rRNA | Składnik strukturalny i katalityczny rybosomu |
| Aminokwasy | Monomery włączane do polipeptydu |

Sekwencja aminokwasów wpływa na fałdowanie i strukturę przestrzenną, a ta na działanie białka. W zależności od produktu dodatkowo zachodzi odcinanie fragmentów lub przyłączanie grup, np. cukrowych, lipidowych czy fosforanowych. Nie twierdź, że każde białko wymaga wszystkich tych modyfikacji.

Nie mieszaj **modyfikacji potranskrypcyjnych** dotyczących RNA z **modyfikacjami potranslacyjnymi** dotyczącymi polipeptydu/białka. Splicing nie jest procesem usuwania aminokwasów z białka.

### E. Regulacja ekspresji

Regulacja zmienia aktywność genów i ilość ich produktów. Pozwala komórkom różnicować się i odpowiadać na zmiany środowiska oraz sygnały nerwowe i hormonalne. Ten sam gen może być silnie aktywny w jednych komórkach, słabiej w innych, a w niektórych nieaktywny.

Nie wszystkie geny w komórce są wyłączone poza jedną specjalizacją: komórki mają także geny aktywne ze względu na podstawowe procesy życiowe. Różnice dotyczą zestawu i poziomu ekspresji, a nie prostego wyboru jednego genu.

W podręczniku insulina ilustruje wpływ sygnału hormonalnego na aktywność genów związanych z metabolizmem cukrów. Nie oznacza to, że insulina zmienia sam kod genetyczny. Zmiana ekspresji nie musi oznaczać mutacji.

#### Wzorzec odpowiedzi „wyjaśnij / wykaż”

Połącz **przyczynę**, **mechanizm** i **skutek**. Przykład: komórki wątroby i szpiku pełnią różne funkcje, więc aktywne są w nich różne zestawy genów; wytwarzają odmienne produkty, które umożliwiają wykonywanie tych funkcji. Samo „bo są inne” nie wyjaśnia mechanizmu.

#### Odwrotna transkrypcja

Proces uzyskiwania DNA na matrycy RNA nazywa się **odwrotną transkrypcją**. Uczestniczy w nim **odwrotna transkryptaza**. Występuje m.in. u retrowirusów, np. HIV, oraz w mechanizmach niektórych retrotranspozonów. Jest też wykorzystywany laboratoryjnie do otrzymywania cDNA. Nie myl go z translacją ani z odtwarzaniem oryginalnego genomowego genu na podstawie łańcucha aminokwasów.

### F. Odpowiedzi do poleceń kontrolnych, s. 20

| Numer | Wzorcowa odpowiedź |
|---|---|
| 1 | Transkrypcja: synteza RNA na matrycy DNA, dla omawianego genu białkowego w jądrze. Translacja: synteza polipeptydu według kodonów mRNA na rybosomach w cytozolu / związanych z RER |
| 2 | Obróbka pre-mRNA usuwa introny i łączy eksony, dzięki czemu powstaje dojrzały transkrypt nadający się do prawidłowego odczytu. Dodatkowe modyfikacje mogą zwiększać trwałość RNA oraz ułatwiać jego eksport i wykorzystanie |
| 3 | Komórki wątroby i szpiku mają różne funkcje, dlatego różnią się aktywnością genów i wytwarzanymi produktami, mimo zasadniczo wspólnego genomu |
| 4 | Tak: odwrotna transkrypcja prowadzi do syntezy DNA na matrycy RNA z udziałem odwrotnej transkryptazy; przykład stanowią retrowirusy |

### G. Zadania końcowe — s. 23–24

#### G1. Zadanie 6, s. 23 — uporządkowanie etapów

**B → D → A → E → C.** Najpierw informacja z DNA jest przepisywana na pre-mRNA; następnie usuwane są introny; dojrzałe mRNA wiąże rybosom; aminokwasy są łączone w polipeptyd; produkt uzyskuje właściwości po fałdowaniu i modyfikacjach.

#### G2. Zadanie 7, s. 23 — kolory eksonów i intronów

Na skanie kolory są słabo widoczne. Poniżej zapisano granice odcinków odczytane z powiększonego kolorowego obrazu. `E` oznacza czarny ekson, `I` zielony intron; spacje i etykiety są oznaczeniami pomocniczymi.

| Odcinek w kolejności skanu | Rodzaj | DNA matrycowe |
|---|---|---|
| 1 | E1 | AAATCGA |
| 2 | I1 | TTAAATGC |
| 3 | E2 | TAACGC |
| 4 | I2 | TCCGAT |
| 5 | E3 | CCGTATTT |
| 6 | I3 | AACGGTA |

Całe wejście: `AAATCGATTAAATGCTAACGCTCCGATCCGTATTTAACGGTA`.

Zachowane eksony matrycy: `AAATCGA` + `TAACGC` + `CCGTATTT` = `AAATCGATAACGCCCGTATTT`.

**Dojrzałe mRNA w układzie skanu:** `UUUAGCUAUUGCGGGCAUAAA`.

Kontrola długości: wejście ma 42 nukleotydy; introny 8 + 6 + 7 = 21; eksony 7 + 6 + 8 = 21. Wynik ma 21 nukleotydów i nie zawiera T. Zadanie wymaga tylko mRNA, więc nie dopisuj polipeptydu ani AUG. W innym zdjęciu tego typu zadania granice trzeba odczytać ponownie; nie przenoś tych pozycji na dowolną sekwencję.

#### G3. Zadanie 8, s. 24 — rozpoznawanie procesów

**a)** A — replikacja, ponieważ DNA jest kopiowane do dwóch cząsteczek DNA. B — transkrypcja, ponieważ na podstawie DNA powstaje mRNA. C — translacja, ponieważ według mRNA powstaje polipeptyd.

**b)** W jądrze komórkowym zachodzą **A i B**, jeśli zadanie dotyczy przedstawionego jądrowego DNA komórki eukariotycznej. Translacja zachodzi na rybosomach poza jądrem.

Pozostałe zadania końcowe 1–5 są omówione w części 1.1, a 9–12 w części 1.2. Razem tworzą pełny klucz 12 zadań końcowych.

### H. Przykłady dodatkowe i testy rozumienia

#### H1. Splicing bez zgadywania granic

Matryca w układzie 3′→5′: `[E1 TAC] [I GGGG] [E2 AAA] [I CC] [E3 ATT]`.

Pre-mRNA: `5′-AUG [CCCC] UUU [GG] UAA-3′`, gdzie nawiasy wskazują introny.

Dojrzałe mRNA: `5′-AUG UUU UAA-3′`. Polipeptyd: **Met–Phe**. Wejście ma 15 nukleotydów, z czego 6 intronowych; dojrzała sekwencja ma 9. Usuwane są introny RNA, nie fragmenty białka.

#### H2. Kodon na granicy eksonów

Dwa sąsiednie eksony RNA mają sekwencje `AUGG` oraz `CUUAA`. Po złączeniu: `AUGGCUUAA`, a kodony to `AUG GCU UAA`. Łańcuch: **Met–Ala**. Nie dziel każdego eksonu osobno na kodony; GCU zaczyna się w pierwszym i kończy w drugim.

#### H3. Długość transkryptu

Przepisany odcinek ma 900 nukleotydów, a oznaczone introny łącznie 300. Po samym splicingu pozostaje **600 nukleotydów**. Bez informacji o początku i końcu części kodującej nie można z samej tej liczby wyznaczyć dokładnej liczby aminokwasów.

#### H4. Odróżnij opis procesu od jego skutku

„Polimeraza RNA dobiera nukleotydy do nici DNA” — transkrypcja. „tRNA dostarcza aminokwas do rybosomu” — translacja. „Z pre-mRNA wycinane są introny” — obróbka potranskrypcyjna. „Do białka przyłączana jest reszta fosforanowa” — modyfikacja białka. „Powstają dwie cząsteczki DNA, każda ze starą i nową nicią” — replikacja.

#### H5. Prawda/fałsz z korektą

| Zdanie | Ocena | Poprawienie / uzasadnienie |
|---|---|---|
| „Ekspresja każdego genu musi prowadzić do białka” | F | Produktem niektórych genów jest funkcjonalne RNA |
| „Introny są przepisywane do pre-mRNA” | P | Ich odpowiedniki są następnie usuwane podczas splicingu |
| „Splicing usuwa introny z DNA” | F | Standardowy splicing dotyczy RNA |
| „Różna ekspresja genów może prowadzić do specjalizacji komórek” | P | Powstają produkty potrzebne do różnych funkcji |
| „Rybosom tłumaczy DNA bezpośrednio na białko” | F | Bezpośrednią matrycą jest mRNA |
| „Kodon STOP koduje ostatni aminokwas” | F | Jest sygnałem zakończenia, nie aminokwasem |
| „Zapis RNA może zostać wykorzystany jako matryca syntezy DNA” | P | Tak działa odwrotna transkrypcja |

### I. Kryteria poprawnego rozwiązywania

Przy lokalizacji zawsze ustal typ komórki i materiał genetyczny. Przy splicingu wymagaj jawnych granic intronów. Przy zadaniu „dojrzałe mRNA” nie zwracaj pre-mRNA. Przy sekwencji aminokwasów używaj dojrzałego mRNA i prawidłowej ramki. Przy regulacji wyjaśniaj różnice aktywności genów, a nie zmianę kodu genetycznego. Przy odpowiedzi otwartej podaj mechanizm konieczny do uzasadnienia, bez dodawania niepotrzebnych wyjątków.

### J. Źródła doprecyzowań

- [NHGRI — Transcription](https://www.genome.gov/genetics-glossary/Transcription) i [Translation](https://www.genome.gov/genetics-glossary/Translation): rozróżnienie syntezy RNA i syntezy polipeptydu.
- [NHGRI — Intron](https://www.genome.gov/genetics-glossary/Intron): intron jest obecny w pierwotnym transkrypcie, ale usuwany z dojrzałego mRNA.
- [NHGRI — RNA Fact Sheet](https://www.genome.gov/about-genomics/educational-resources/fact-sheets/ribonucleic-acid-fact-sheet): alternatywny splicing, funkcjonalne RNA i odwrotna transkrypcja.
