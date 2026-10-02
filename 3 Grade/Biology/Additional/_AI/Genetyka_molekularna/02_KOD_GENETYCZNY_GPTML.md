# 1.2. Kod genetyczny — GPTML

Źródło zakresu: `bio.pdf`, strony PDF 8–11 (strony podręcznika 13–16); powtórzenie i zadania na stronach PDF 17 i 19. Stosuj standardowy kod genetyczny oraz szkolny model rozpoczynania translacji od AUG, chyba że polecenie podaje inny kontekst.

## A. Definicje i sześć cech kodu

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

## B. Pełna tabela standardowego kodu — 64 kodony

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

## C. mRNA, nić matrycowa i nić kodująca

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

## D. Algorytmy zadań sekwencyjnych

### D1. DNA → mRNA → polipeptyd

1. Przepisz dokładnie litery sekwencji. Nie zgaduj nieczytelnego nukleotydu. Odczytaj strzałkę i oznaczenie nici.
2. Ustal kierunek oraz obecność intronów. Jeśli wynik ma być dojrzałym mRNA, usuń oznaczone introny przez splicing.
3. Utwórz mRNA zgodnie z tabelą w części C. Sprawdź brak T w wyniku.
4. Ustal ramkę odczytu. Dla kompletnego szkolnego odcinka od START do STOP zacznij od wskazanego AUG. Dla fragmentu z podaną ramką tłumacz od jej początku, nawet gdy nie zaczyna się od AUG.
5. Dziel mRNA na niepokrywające się trójki. Nie przesuwaj granic, aby otrzymać „ładniejszą” odpowiedź.
6. Przypisz każdemu kodonowi aminokwas z tabeli. Zakończ na pierwszym STOP w tej samej ramce. Nie tłumacz dalszej sekwencji jako części tego polipeptydu.
7. Podaj mRNA i łańcuch, jeżeli oba były wymagane; STOP opisz osobno.

Brak AUG w podanym fragmencie nie dowodzi, że fragment nie koduje aminokwasów — może leżeć wewnątrz części kodującej. Brak STOP może oznaczać niepełny fragment. Przy pełnym mRNA bez wskazanego miejsca inicjacji kilka AUG może dawać niejednoznaczność; nie przedstawiaj dowolnie wybranej ramki jako jedynej pewnej.

Niepełna trójka na końcu fragmentu nie koduje kompletnego aminokwasu. Zgłoś pozostałe 1–2 nukleotydy. Nie dopisuj brakujących liter i nie zakładaj, że dowodzą błędnej sekwencji biologicznej — fragment może kończyć się w środku kodonu.

### D2. Antykodon tRNA

Kodon `5′-AUG-3′` paruje w szkolnym modelu z antykodonem `3′-UAC-5′`. Ten sam antykodon zapisany 5′→3′ to `5′-CAU-3′`. Jeśli polecenie nie podaje kierunku, wpisz końce, aby uniknąć niejednoznaczności.

Do kodonu STOP w standardowym szkolnym modelu nie dopasowuj tRNA z „aminokwasem STOP”. Zakończenie rozpoznają czynniki uwalniające. Uproszczone ścisłe parowanie wystarcza w tych zadaniach; mechanizm wobble stosuj dopiero, gdy polecenie go wymaga.

### D3. Aminokwasy → przykładowe mRNA → DNA

1. Dla każdego aminokwasu wybierz **jeden** poprawny kodon. Zachowaj kolejność aminokwasów.
2. Dodaj kodon STOP, jeśli wymaga tego polecenie; dla kompletnej sekwencji użyj jednego z UAA/UAG/UGA.
3. Nie dodawaj dodatkowego AUG przed podaną metioniną — jej AUG już pełni funkcję START w kompletnym szkolnym przykładzie.
4. Połącz kodony i nazwij wynik **przykładową**, a nie jedyną możliwą sekwencją.
5. Jeśli potrzebna jest matryca DNA, dobierz A→T, U→A, C→G, G→C i zapisz partnera RNA 5′→3′ jako DNA 3′→5′. Nić kodująca powstaje przez U→T bez komplementowania.
6. Odczytaj własne mRNA ponownie tabelą. Łańcuch musi dokładnie odpowiadać wejściu.

Z aminokwasów można uzyskać wiele poprawnych sekwencji, ponieważ kod jest zdegenerowany. Bez dodatkowych danych nie można odtworzyć dokładnej oryginalnej sekwencji genu, jego intronów ani części regulatorowych.

### D4. Długości — zakres obowiązywania wzorów

Jeżeli sekwencja zawiera wyłącznie kodony dla `k` aminokwasów oraz jeden końcowy STOP, ma `3(k + 1)` nukleotydów. AUG kodujący początkową metioninę jest już wśród tych k kodonów. Dla fragmentu bez STOP k kompletnych kodonów to 3k nukleotydów.

Przykład: odcinek mRNA od AUG do UAA włącznie ma 303 nukleotydy. Zawiera 101 kodonów, z których jeden to STOP, więc koduje **100 aminokwasów**. Odpowiadający mu odcinek jednej nici DNA ma 303 nukleotydy, a dwuniciowy odcinek DNA — 303 pary zasad, czyli 606 nukleotydów.

Nie stosuj `długość mRNA / 3 − 1` do całego dowolnego mRNA ani genu z intronami. Regiony nieulegające translacji, introny i ogon poli(A) nie są automatycznie częścią sekwencji kodującej.

## E. Przykłady ze skanu i klucz kontrolny

Spacje w zapisach poniżej jedynie wyznaczają kodony; nie są elementem cząsteczki.

### E1. Schemat, s. 13 — fragment wewnętrzny

DNA kodujące `CGG AGC GCA TGA`, DNA matrycowe `GCC TCG CGT ACT`.

**mRNA:** `CGG AGC GCA UGA`. **Łańcuch:** Arg–Ser–Ala. UGA jest STOP. Fragment nie zaczyna się od AUG, ale w schemacie podano ramkę odczytu, więc odczytujemy przedstawione kodony.

### E2. Przykład krok po kroku, s. 15

DNA matrycowe `TAC GGA CGG TTT ATT` daje mRNA `AUG CCU GCC AAA UAA` i łańcuch **Met–Pro–Ala–Lys**. To 15 nukleotydów, 5 kodonów i 4 aminokwasy.

### E3. Odtwarzanie mRNA, s. 16

Łańcuch Met–Arg–His–Cys–Leu–Tyr można zapisać jako `AUG AGA CAC UGU CUA UAU UGA`. To **sześć aminokwasów**, siedem kodonów i 21 nukleotydów. Sformułowanie o „pięciu” aminokwasach w podpisie przykładowej odpowiedzi na skanie jest omyłką; wymieniono sześć.

### E4. Polecenie kontrolne 1, s. 16

mRNA ze skanu: `AUGCCGGGCAUCUUUACGUAA`.

Podział: `AUG CCG GGC AUC UUU ACG UAA`.

**Odpowiedź:** metionina–prolina–glicyna–izoleucyna–fenyloalanina–treonina. UAA kończy translację i nie dodaje siódmego aminokwasu.

### E5. Polecenie kontrolne 2, s. 16

DNA kodujące: `ATG CCG AGC CAA CGC ACT`.

Wskazana matryca: `TAC GGC TCG GTT GCG TGA`.

**mRNA:** `AUG CCG AGC CAA CGC ACU`.

**Łańcuch:** metionina–prolina–seryna–glutamina–arginina–treonina. Nie dopisuj STOP: podano fragment bez kodonu STOP. Końcowe TGA jest w **matrycy**, więc daje ACU, a nie UGA. To celowo ważne rozróżnienie.

### E6. Polecenie kontrolne 3, s. 16

Met–Ser–Gly–Ala–Trp; przykład z wymaganym STOP: `AUG UCU GGU GCU UGG UAA`. Inne kodony dla Ser/Gly/Ala i inny STOP mogą dawać równie poprawną odpowiedź.

### E7. Zadanie końcowe 9, s. 24

Matryca wskazana strzałką: `AGCCATGG`. Komplementarne mRNA w układzie rysunku: **`UCGGUACC`**, czyli **odpowiedź B**. Odpowiedź z T nie może być poprawnym RNA. Zamiana T→U w samej matrycy daje niewłaściwy wynik.

### E8. Zadanie końcowe 10, s. 24

mRNA: `AUGCUAAGGGACCGUAUUUAA`.

Podział: `AUG CUA AGG GAC CGU AUU UAA`.

**Odpowiedź:** metionina–leucyna–arginina–kwas asparaginowy–arginina–izoleucyna. 21 nukleotydów, 7 kodonów i 6 aminokwasów.

### E9. Zadanie końcowe 11, s. 24

Met–Ala–Ser–Gly–Lys–Val. Jedna poprawna para sekwencji:

- mRNA: `5′-AUG GCU UCU GGU AAA GUU UAA-3′`.
- DNA matrycowe: `3′-TAC CGA AGA CCA TTT CAA ATT-5′`.

Kontrola: kodony dają dokładnie sześć wymaganych aminokwasów, a UAA jest STOP. Nie oceniaj innych poprawnych wyborów synonimicznych kodonów jako błędnych.

### E10. Zadanie końcowe 12, s. 24

**Jednoznaczność: schemat B. Zdegenerowanie: schemat C.** W B każdy kodon ma pojedyncze znaczenie. W C kilka kodonów prowadzi do tego samego aminokwasu. Schemat A, gdzie jeden kodon prowadzi do różnych aminokwasów, nie przedstawia poprawnej reguły standardowego kodu.

## F. Dodatkowe zadania zabezpieczające

### F1. Matryca podana 5′→3′

DNA matrycowe: `5′-TTATTTCAT-3′`. Po odwróceniu: `3′-TACTTTATT-5′`. mRNA: `5′-AUG AAA UAA-3′`. Łańcuch: **Met–Lys**. Bez odwrócenia otrzymano by RNA w niewłaściwym kierunku do translacji.

### F2. STOP w środku

mRNA w podanej ramce: `AUG GCU UGA AAA`. Łańcuch: **Met–Ala**. Po UGA translacja tego łańcucha się kończy, więc AAA nie dodaje lizyny.

### F3. Nieznany rodzaj nici

Dla DNA `ATGAAA` bez oznaczeń nie ma jednej pewnej odpowiedzi. Jeśli to nić kodująca 5′→3′, mRNA = `5′-AUGAAA-3′`. Jeśli to matryca 3′→5′, mRNA = `5′-UACUUU-3′`. Jeśli to matryca 5′→3′, mRNA = `5′-UUUCAU-3′`. Nie wybieraj pierwszej możliwości tylko dlatego, że zaczyna się od ATG.

### F4. Zmiana kodonu — uzupełnienie

GCU→GCC nadal oznacza alaninę: zmiana synonimiczna. GCU→GUU zmienia alaninę na walinę. UAU→UAA w części kodującej może przedwcześnie zakończyć translację. Wstawienie lub usunięcie liczby nukleotydów niepodzielnej przez trzy w tłumaczonym odcinku zwykle zmienia ramkę dalszego odczytu. Nie twierdź, że zdegenerowanie chroni przed każdą mutacją.

## G. Lista kontroli dla modelu

Wynik ma poprawny alfabet; nić i kierunek są ustalone; introny uwzględniono zgodnie z poleceniem; ramki nie przesunięto; każdy pełny kodon sprawdzono tabelą; AUG policzono jako Met; STOP nie policzono jako aminokwas; translacji nie kontynuowano za STOP; przy zadaniu odwrotnym wynik nazwano przykładowym.

## H. Źródła doprecyzowań

- [NCBI — The Genetic Codes, tabela standardowa 1](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/genetic-codes/): wzorzec przyporządkowania wszystkich 64 kodonów. NCBI zapisuje w tabeli T; tutaj zastąpiono je U, aby przedstawić kodony mRNA.
- [NHGRI — Codon](https://www.genome.gov/genetics-glossary/Codon): 61 kodonów aminokwasowych i trzy sygnały STOP.
- [NCBI Bookshelf — From DNA to RNA](https://www.ncbi.nlm.nih.gov/books/NBK26887/): synteza RNA 5′→3′ na matrycy odczytywanej 3′→5′.
