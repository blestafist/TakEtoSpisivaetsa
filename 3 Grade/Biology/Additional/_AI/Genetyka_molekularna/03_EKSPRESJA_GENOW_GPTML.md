# 1.3. Ekspresja genów — GPTML

Źródło zakresu: `bio.pdf`, strony PDF 12–15 (strony podręcznika 17–20); powtórzenie na stronach PDF 16–17 i zadania na stronach PDF 18–19. Główny model dotyczy ekspresji jądrowego genu kodującego białko w komórce eukariotycznej.

## A. Czym jest ekspresja genu?

**Ekspresja genu** to wykorzystanie zapisanej w genie informacji do wytworzenia jego produktu — funkcjonalnego RNA lub polipeptydu. Dla genu kodującego białko obejmuje transkrypcję i translację, a u eukariontów także obróbkę transkryptu. Dla genu kodującego tRNA lub rRNA nie ma etapu tłumaczenia tego RNA na białko.

W typowych komórkach somatycznych organizmu występuje zasadniczo ten sam genom, lecz różne geny są aktywne z różną intensywnością. Dzięki temu powstają komórki o różnych właściwościach i funkcjach. Nie tłumacz różnic między neuronem a komórką wątroby tym, że każda zawiera zupełnie inny zestaw genów.

**Doprecyzowanie:** zdanie „wszystkie komórki mają to samo DNA” jest szkolnym uproszczeniem. Gamety mają inny zestaw chromosomów, dojrzałe erytrocyty człowieka nie mają jądra, a część komórek może mieć mutacje lub zmienioną ploidalność. Przy typowym pytaniu o różnicowanie komórek odpowiedź dotyczy jednak regulacji ekspresji, a nie tych wyjątków.

## B. Kolejność i miejsca procesów

| Kolejność | Proces | Co powstaje / co się zmienia | Miejsce w głównym modelu |
|---|---|---|---|
| 1 | Transkrypcja | RNA powstaje na matrycy DNA; dla genu kodującego białko powstaje pre-mRNA | Jądro komórkowe |
| 2 | Modyfikacje potranskrypcyjne | Pre-mRNA dojrzewa; m.in. usuwa się introny i łączy eksony | Jądro komórkowe |
| 3 | Eksport mRNA | Dojrzałe mRNA przechodzi przez pory jądrowe | Z jądra do cytozolu |
| 4 | Translacja | Według kodonów mRNA powstaje polipeptyd | Rybosomy po cytoplazmatycznej stronie komórki: wolne lub związane z RER |
| 5 | Fałdowanie i ewentualne modyfikacje białka | Produkt uzyskuje odpowiednią strukturę i właściwości | Zależnie od białka: m.in. cytozol, RER, aparat Golgiego |

Fałdowanie może zaczynać się już w czasie translacji, a szczegółowe modyfikacje zależą od białka. Do szkolnego porządkowania zdarzeń użyj kolejności przedstawionej w tabeli. Nie utożsamiaj „genu” z „gotowym białkiem” ani eksportu mRNA z translacją.

### Porównanie trzech często mylonych procesów

| Cecha | Replikacja | Transkrypcja | Translacja |
|---|---|---|---|
| Informacja / matryca | DNA | DNA | mRNA |
| Bezpośredni produkt | DNA | RNA | Polipeptyd |
| Główne wykonawstwo | Polimeraza DNA i pozostałe enzymy replikacji | Polimeraza RNA | Rybosom, tRNA i czynniki translacji |
| Zakres | Kopiowanie materiału DNA przed podziałem | Przepisywanie wybranych odcinków na RNA | Odczyt części kodującej mRNA |
| Komplementarność | DNA z DNA | DNA z RNA | Kodon mRNA z antykodonem tRNA |
| Miejsce dla jądrowego genu eukarionta | Jądro | Jądro | Rybosomy poza jądrem |

U bakterii nie ma jądra: transkrypcja i translacja zachodzą w komórce bez rozdzielenia otoczką jądrową i mogą być sprzężone. Nie stosuj odpowiedzi „w jądrze” do zadania o bakterii. DNA mitochondriów i chloroplastów jest odrębnym kontekstem; tabela opisuje głównie materiał jądrowy.

## C. Transkrypcja i dojrzewanie RNA

Polimeraza RNA wiąże się z odpowiednim regionem DNA wraz z czynnikami uczestniczącymi w rozpoczęciu transkrypcji. Lokalnie odsłania matrycę, a następnie dołącza nukleotydy RNA zgodnie z komplementarnością. Odczytuje matrycę 3′→5′ i wydłuża RNA 5′→3′. DNA nie jest zużywane ani zamieniane chemicznie w RNA; po przejściu polimerazy nici DNA mogą się ponownie połączyć.

Dla danego transkryptu kopiowana jest jedna nić matrycowa. W innych genach matrycą może być druga nić DNA. Nie wyciągaj wniosku, że jedna nić całego chromosomu jest zawsze kodująca, a druga zawsze matrycowa.

W genie zawierającym introny pierwotny transkrypt pre-mRNA zawiera odpowiedniki eksonów i intronów. **Splicing** usuwa introny z RNA i łączy eksony. Standardowy splicing RNA nie wycina intronów z genomowego DNA.

**Doprecyzowanie:** nie każda część regulatorowa genu jest transkrybowana. Nie utożsamiaj zdania „transkrypcji podlegają eksony i introny” ze stwierdzeniem, że cały otaczający je obszar DNA znajdzie się w RNA.

W zakresie skanu główną wymaganą modyfikacją jest splicing. Typowa obróbka eukariotycznego pre-mRNA obejmuje również dodanie czapeczki 5′ i obróbkę końca 3′, często z ogonem poli(A). Te elementy są **uzupełnieniem**; w zadaniu opartym wyłącznie na oznaczonych eksonach i intronach nie dopisuj arbitralnie długości czapeczki ani ogona poli(A).

**Alternatywny splicing — uzupełnienie:** różne zestawienia eksonów z tego samego transkryptu mogą prowadzić do różnych mRNA i produktów białkowych. Nie zmieniaj jednak zestawu eksonów w zwykłym zadaniu, jeśli nie podano wariantu splicingu.

### Algorytm: nić matrycowa z intronami → dojrzałe mRNA

1. Odczytaj oznaczenia eksonów i intronów: kolory, nawiasy, podkreślenia lub numery. Sam ciąg liter nie zawiera tej informacji.
2. Ustal, czy wejście to DNA matrycowe, kodujące czy pre-mRNA. Ustal kierunek zapisu.
3. Dla DNA matrycowego utwórz komplementarny transkrypt RNA. Zaznacz w nim granice odpowiadające intronom.
4. Usuń wyłącznie introny i połącz eksony w niezmienionej kolejności.
5. Sprawdź, że wynik jest RNA i jego długość odpowiada sumie zachowanych odcinków.
6. Jeżeli polecenie wymaga również polipeptydu, ustal ramkę już w **dojrzałym** mRNA; granica kodonu może wypadać na połączeniu eksonów.

Możesz rachunkowo najpierw skleić oznaczone eksony DNA, a potem utworzyć odpowiadający im RNA — wynik sekwencyjny będzie ten sam przy zachowaniu kierunku. Opisując proces biologiczny, napisz jednak, że introny są wycinane z pre-mRNA.

Jeśli kolory zniknęły w OCR lub zdjęcie nie pozwala ustalić granic, wskaż dokładnie brakującą informację i poproś o oznaczenie intronów. Nie uznawaj fragmentu za intron dlatego, że ma „dziwny” kodon lub długość niepodzielną przez trzy.

## D. Translacja i funkcjonalne białko

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

## E. Regulacja ekspresji

Regulacja zmienia aktywność genów i ilość ich produktów. Pozwala komórkom różnicować się i odpowiadać na zmiany środowiska oraz sygnały nerwowe i hormonalne. Ten sam gen może być silnie aktywny w jednych komórkach, słabiej w innych, a w niektórych nieaktywny.

Nie wszystkie geny w komórce są wyłączone poza jedną specjalizacją: komórki mają także geny aktywne ze względu na podstawowe procesy życiowe. Różnice dotyczą zestawu i poziomu ekspresji, a nie prostego wyboru jednego genu.

W podręczniku insulina ilustruje wpływ sygnału hormonalnego na aktywność genów związanych z metabolizmem cukrów. Nie oznacza to, że insulina zmienia sam kod genetyczny. Zmiana ekspresji nie musi oznaczać mutacji.

### Wzorzec odpowiedzi „wyjaśnij / wykaż”

Połącz **przyczynę**, **mechanizm** i **skutek**. Przykład: komórki wątroby i szpiku pełnią różne funkcje, więc aktywne są w nich różne zestawy genów; wytwarzają odmienne produkty, które umożliwiają wykonywanie tych funkcji. Samo „bo są inne” nie wyjaśnia mechanizmu.

### Odwrotna transkrypcja

Proces uzyskiwania DNA na matrycy RNA nazywa się **odwrotną transkrypcją**. Uczestniczy w nim **odwrotna transkryptaza**. Występuje m.in. u retrowirusów, np. HIV, oraz w mechanizmach niektórych retrotranspozonów. Jest też wykorzystywany laboratoryjnie do otrzymywania cDNA. Nie myl go z translacją ani z odtwarzaniem oryginalnego genomowego genu na podstawie łańcucha aminokwasów.

## F. Odpowiedzi do poleceń kontrolnych, s. 20

| Numer | Wzorcowa odpowiedź |
|---|---|
| 1 | Transkrypcja: synteza RNA na matrycy DNA, dla omawianego genu białkowego w jądrze. Translacja: synteza polipeptydu według kodonów mRNA na rybosomach w cytozolu / związanych z RER |
| 2 | Obróbka pre-mRNA usuwa introny i łączy eksony, dzięki czemu powstaje dojrzały transkrypt nadający się do prawidłowego odczytu. Dodatkowe modyfikacje mogą zwiększać trwałość RNA oraz ułatwiać jego eksport i wykorzystanie |
| 3 | Komórki wątroby i szpiku mają różne funkcje, dlatego różnią się aktywnością genów i wytwarzanymi produktami, mimo zasadniczo wspólnego genomu |
| 4 | Tak: odwrotna transkrypcja prowadzi do syntezy DNA na matrycy RNA z udziałem odwrotnej transkryptazy; przykład stanowią retrowirusy |

## G. Zadania końcowe — s. 23–24

### G1. Zadanie 6, s. 23 — uporządkowanie etapów

**B → D → A → E → C.** Najpierw informacja z DNA jest przepisywana na pre-mRNA; następnie usuwane są introny; dojrzałe mRNA wiąże rybosom; aminokwasy są łączone w polipeptyd; produkt uzyskuje właściwości po fałdowaniu i modyfikacjach.

### G2. Zadanie 7, s. 23 — kolory eksonów i intronów

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

### G3. Zadanie 8, s. 24 — rozpoznawanie procesów

**a)** A — replikacja, ponieważ DNA jest kopiowane do dwóch cząsteczek DNA. B — transkrypcja, ponieważ na podstawie DNA powstaje mRNA. C — translacja, ponieważ według mRNA powstaje polipeptyd.

**b)** W jądrze komórkowym zachodzą **A i B**, jeśli zadanie dotyczy przedstawionego jądrowego DNA komórki eukariotycznej. Translacja zachodzi na rybosomach poza jądrem.

Pozostałe zadania końcowe 1–5 są omówione w części 1.1, a 9–12 w części 1.2. Razem tworzą pełny klucz 12 zadań końcowych.

## H. Przykłady dodatkowe i testy rozumienia

### H1. Splicing bez zgadywania granic

Matryca w układzie 3′→5′: `[E1 TAC] [I GGGG] [E2 AAA] [I CC] [E3 ATT]`.

Pre-mRNA: `5′-AUG [CCCC] UUU [GG] UAA-3′`, gdzie nawiasy wskazują introny.

Dojrzałe mRNA: `5′-AUG UUU UAA-3′`. Polipeptyd: **Met–Phe**. Wejście ma 15 nukleotydów, z czego 6 intronowych; dojrzała sekwencja ma 9. Usuwane są introny RNA, nie fragmenty białka.

### H2. Kodon na granicy eksonów

Dwa sąsiednie eksony RNA mają sekwencje `AUGG` oraz `CUUAA`. Po złączeniu: `AUGGCUUAA`, a kodony to `AUG GCU UAA`. Łańcuch: **Met–Ala**. Nie dziel każdego eksonu osobno na kodony; GCU zaczyna się w pierwszym i kończy w drugim.

### H3. Długość transkryptu

Przepisany odcinek ma 900 nukleotydów, a oznaczone introny łącznie 300. Po samym splicingu pozostaje **600 nukleotydów**. Bez informacji o początku i końcu części kodującej nie można z samej tej liczby wyznaczyć dokładnej liczby aminokwasów.

### H4. Odróżnij opis procesu od jego skutku

„Polimeraza RNA dobiera nukleotydy do nici DNA” — transkrypcja. „tRNA dostarcza aminokwas do rybosomu” — translacja. „Z pre-mRNA wycinane są introny” — obróbka potranskrypcyjna. „Do białka przyłączana jest reszta fosforanowa” — modyfikacja białka. „Powstają dwie cząsteczki DNA, każda ze starą i nową nicią” — replikacja.

### H5. Prawda/fałsz z korektą

| Zdanie | Ocena | Poprawienie / uzasadnienie |
|---|---|---|
| „Ekspresja każdego genu musi prowadzić do białka” | F | Produktem niektórych genów jest funkcjonalne RNA |
| „Introny są przepisywane do pre-mRNA” | P | Ich odpowiedniki są następnie usuwane podczas splicingu |
| „Splicing usuwa introny z DNA” | F | Standardowy splicing dotyczy RNA |
| „Różna ekspresja genów może prowadzić do specjalizacji komórek” | P | Powstają produkty potrzebne do różnych funkcji |
| „Rybosom tłumaczy DNA bezpośrednio na białko” | F | Bezpośrednią matrycą jest mRNA |
| „Kodon STOP koduje ostatni aminokwas” | F | Jest sygnałem zakończenia, nie aminokwasem |
| „Zapis RNA może zostać wykorzystany jako matryca syntezy DNA” | P | Tak działa odwrotna transkrypcja |

## I. Kryteria poprawnego rozwiązywania

Przy lokalizacji zawsze ustal typ komórki i materiał genetyczny. Przy splicingu wymagaj jawnych granic intronów. Przy zadaniu „dojrzałe mRNA” nie zwracaj pre-mRNA. Przy sekwencji aminokwasów używaj dojrzałego mRNA i prawidłowej ramki. Przy regulacji wyjaśniaj różnice aktywności genów, a nie zmianę kodu genetycznego. Przy odpowiedzi otwartej podaj mechanizm konieczny do uzasadnienia, bez dodawania niepotrzebnych wyjątków.

## J. Źródła doprecyzowań

- [NHGRI — Transcription](https://www.genome.gov/genetics-glossary/Transcription) i [Translation](https://www.genome.gov/genetics-glossary/Translation): rozróżnienie syntezy RNA i syntezy polipeptydu.
- [NHGRI — Intron](https://www.genome.gov/genetics-glossary/Intron): intron jest obecny w pierwotnym transkrypcie, ale usuwany z dojrzałego mRNA.
- [NHGRI — RNA Fact Sheet](https://www.genome.gov/about-genomics/educational-resources/fact-sheets/ribonucleic-acid-fact-sheet): alternatywny splicing, funkcjonalne RNA i odwrotna transkrypcja.
