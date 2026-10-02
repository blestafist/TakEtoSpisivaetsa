# Genetyka molekularna — materiały GPTML

Opracowanie zakresu z załączonego `bio.pdf`: 19 stron skanu, strony podręcznika 6–24,
tematy 1.1–1.3. Język materiałów i odpowiedzi: polski, zgodnie z zadaniami źródłowymi
i konwencją biologicznych GPTML w repozytorium.

## Pliki i użycie

| Plik | Zastosowanie |
|---|---|
| [BIO_GENETYKA_MOLEKULARNA_GPTML.md](../BIO_GENETYKA_MOLEKULARNA_GPTML.md) | Połączony, samodzielny materiał do przekazania modelowi; zawiera również instrukcję solvera |
| [01_GEN_DNA_RNA_GPTML.md](01_GEN_DNA_RNA_GPTML.md) | Gen, DNA/RNA, chromatyna, replikacja, komplementarność i obliczenia |
| [02_KOD_GENETYCZNY_GPTML.md](02_KOD_GENETYCZNY_GPTML.md) | Cechy kodu, wszystkie 64 kodony, kierunki nici, translacja i zadania odwrotne |
| [03_EKSPRESJA_GENOW_GPTML.md](03_EKSPRESJA_GENOW_GPTML.md) | Transkrypcja, splicing, translacja, modyfikacje i regulacja ekspresji |
| [BIO_GENETYKA_SOLVER_PROMPT.md](BIO_GENETYKA_SOLVER_PROMPT.md) | Krótka instrukcja do używania osobno z wybranym plikiem tematycznym |
| [build_gptml.py](build_gptml.py) | Powtarzalne złożenie tematów w jeden plik; `--check` wykrywa nieaktualny wynik |

Do pełnego zakresu użyj pliku połączonego. Do pojedynczej tematyki użyj odpowiedniego
modułu wraz z instrukcją solvera. Treści te są materiałem odniesienia w kontekście
modelu; nie oznaczają przeprowadzonego fine-tuningu ani pomiaru bezbłędności modelu.

Po zmianie tematu uruchom w tym katalogu:

```bash
python3 build_gptml.py
python3 build_gptml.py --check
```

## Pokrycie źródła

Numer PDF jest pozycją strony w załączniku; numer podręcznika to numer wydrukowany
na zdjęciu. Wszystkie strony zostały obejrzane, w tym schematy i kolorowe oznaczenia.

| PDF | Podręcznik | Zakres | Miejsce opracowania |
|---|---|---|---|
| 1–2 | 6–7 | Gen, związek z cechami, budowa i informacje w genach | 01, A |
| 3 | 8 | Nukleotyd DNA, sekwencja, komplementarność | 01, B i D |
| 4 | 9 | Funkcje DNA, histony, chromatyna, chromosom i chromatyda | 01, A i C |
| 5 | 10 | Replikacja, polimeraza DNA, mitoza i mejoza | 01, C |
| 6 | 11 | Budowa i rodzaje RNA, antykodon | 01, B; 02, D2 |
| 7 | 12 | Przykład liczbowy i 3 polecenia kontrolne | 01, D i E1–E4 |
| 8 | 13 | Kod genetyczny, nici DNA, START/STOP, fragment sekwencji | 02, A, C i E1 |
| 9 | 14 | Sześć cech kodu i schematy | 02, A |
| 10 | 15 | Tabela kodu i odczyt DNA→mRNA→polipeptyd | 02, B, D1 i E2 |
| 11 | 16 | Zadanie odwrotne i 3 polecenia kontrolne | 02, D3 i E3–E6 |
| 12 | 17 | Ekspresja genów i miejsca biosyntezy | 03, A–B |
| 13 | 18 | Transkrypcja, polimeraza RNA i obróbka pre-mRNA | 03, C |
| 14 | 19 | Etapy translacji, rola tRNA i rybosomu | 03, D |
| 15 | 20 | Właściwości białka, regulacja, 4 polecenia kontrolne | 03, D–F |
| 16–17 | 21–22 | Powtórzenie wszystkich trzech tematów | 01–03 |
| 18 | 23 | Zadania końcowe 1–7 | 01, E7; 03, G1–G2 |
| 19 | 24 | Zadania końcowe 8–12 | 03, G3; 02, E7–E10 |

## Doprecyzowania i odczyt skanu

Wprowadzono wyraźne rozróżnienie genu kodującego białko i genu kodującego funkcjonalne
RNA, eksonu i sekwencji ulegającej translacji, liczby chromosomów i ilości DNA,
matrycy i nici kodującej oraz START/STOP i sygnałów transkrypcji. Replikacja poprzedza
mejozę I, a nie oba podziały. Zapisano reguły dla kierunków 5′/3′, których szkolne
rysunki w skanie zwykle nie oznaczają. Dodatki ponad skan są oznaczone jako
uzupełnienia lub doprecyzowania; nie zastępują odpowiedzi wymaganej w prostym zadaniu.

Na s. 16 przykładowy łańcuch ma sześć aminokwasów, chociaż opis odpowiedzi mówi
o pięciu. W materiale poprawiono liczbę zgodnie z sekwencją. Na s. 23, zad. 7, OCR
nie zachowuje kolorów intronów. Granice odczytano z powiększonego kolorowego skanu
i zapisano jawnie w tabeli w module 03, G2, aby model nie musiał odgadywać kolorów.

Klucz dotyczy konkretnych danych ze skanu. Materiał nie przyjmuje, że zadanie o tym
samym numerze w innej wersji ma tę samą odpowiedź. Źródłowego PDF i jego zdjęć nie
dołączono do repozytorium; zamieszczono własne opracowanie i niezbędne dane zadań.

## Sprawdzenie materiału

Weryfikacja obejmuje komplet 64 różnych kodonów i zgodność ich znaczeń z tabelą
standardową NCBI, wszystkie sekwencje przykładów i klucza, obliczenia procentowe
i liczbowe, długości po splicingu, poprawność odpowiedzi do zadań schematycznych,
zgodność połączonego pliku ze źródłami oraz lokalne odnośniki. Nie przeprowadzono
ewaluacji na modelach zewnętrznych; przykłady zabezpieczające służą też do takiej
późniejszej ewaluacji.

Linki do źródeł NHGRI i NCBI znajdują się na końcu odpowiednich tematów. Głównym
źródłem zakresu, zadań i przykładów pozostaje załączony skan.
