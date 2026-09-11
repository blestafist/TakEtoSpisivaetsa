## 1. Definicja i stopień wielomianu

W zadaniach 8.1 oraz 8.5 wprowadzane są podstawowe pojęcia:

- **Współczynniki liczbowe** – liczby stojące przy zmiennych $x$ (np. w wielomianie $W(x) = -5x^4 + 5x^2 - 4x + 3$ współczynnikami są $-5, 5, -4, 3$).
    
- **Stopień wielomianu (oznaczany jako $\text{st}(W)$)** – to najwyższa potęga zmiennej $x$, która występuje w wielomianie z niezerowym współczynnikiem.
    

### Zasada porządkowania wielomianu:

Aby poprawnie określić stopień lub wykonywać działania, wielomian należy najpierw uporządkować (zredukować wyrazy podobne i zapisać potęgi od najwyższej do najniższej).

- **Przykład z zeszytu (8.5 d):** Postać początkowa: $W(x) = -4x + 6 + 2x - 8x^3 + 4x^5$
    
    Po uporządkowaniu: $W(x) = 4x^5 - 8x^3 - 2x + 6 \implies \text{st}(W) = 5$.
    

## 2. Dzielenie wielomianów i Schemat Hornera

W zadaniach 8.112, 8.115 i pokrewnych wykonujecie dzielenie wielomianu $W(x)$ przez dwumian liniowy $(x - c)$. W zeszycie stosujesz **Schemat Hornera** – szybką metodę tabelaryczną.

### Wzór na dzielenie z resztą:

$$W(x) = P(x) \cdot Q(x) + R(x)$$

Gdzie:

- $W(x)$ – dzielna (wielomian główny),
    
- $P(x)$ – dzielnik (np. dwumian $x - c$),
    
- $Q(x)$ – iloraz (wynik dzielenia, o stopień niższy od $W(x)$),
    
- $R(x)$ – reszta z dzielenia (liczba). Jeśli $R(x) = 0$, wielomian jest **podzielny** przez dany dwumian.
    

### Algorytm Schematu Hornera (na przykładzie podpunktu a):

Dzielimy $(3x^4 - 4x^3 - 8x^2 + 7x + 2) : (x - 2)$.

1. Miejsce zerowe dzielnika: $x - 2 = 0 \implies x = 2$ (wypisywane po lewej stronie tabeli).
    
2. W nagłówku tabeli wypisujemy po kolei współczynniki wielomianu (pamiętając o wpisaniu $0$, jeśli brakuje jakiejś potęgi, jak w podpunkcie b).
    
3. Pierwszy współczynnik przepisujemy na dół. Każdy kolejny obliczamy wzorem: $\text{krok} = (\text{miejsce zerowe} \cdot \text{liczba z dołu}) + \text{liczba z góry}$.
    
4. Ostatnia liczba na dole to **reszta z dzielenia** ($R$).
    

## 3. Twierdzenie Bezouta i szukanie parametru $m$

W zadaniu 8.119 pojawia się kluczowe twierdzenie matematyczne:

### Twierdzenie Bezouta:

> Reszta z dzielenia wielomianu $W(x)$ przez dwumian $(x - c)$ jest równa wartości tego wielomianu dla argumentu $c$.
> 
> $$R = W(c)$$

- **Zastosowanie w zadaniu 8.119:** Wielomian $W(x) = m^2x^8 - 5x^4 - 3m$ dzielony przez $(x - 1)$ daje resztę $R = 4$.
    
    **Zasada rozwiązania:** Podstawiamy $x = 1$ do wielomianu i przyrównujemy do $4$:
    
    $$W(1) = 4 \implies m^2(1)^8 - 5(1)^4 - 3m = 4 \implies m^2 - 3m - 5 = 4 \implies m^2 - 3m - 4 = 0$$
    
    Do rozwiązania tego równania kwadratowego użyliście **Wzorów Viète’a**:
    
    $$\begin{cases} m_1 + m_2 = 3 \\ m_1 \cdot m_2 = -4 \end{cases} \implies m_1 = 4, \quad m_2 = -1$$
    

## 4. Metoda współczynników nieoznaczonych

Ta metoda została użyta m.in. w zadaniach 8.94 i 8.96, gdy wielomiany są sobie równe (lub dzielą się bez reszty), ale mają ukryte parametry $a$ i $b$.

### Zasada działania metody:

1. Zapisujemy równość wielomianów (np. wynikającą z mnożenia dzielnika przez iloraz).
    
2. Wymnażamy nawiasy po prawej stronie i porządkujemy wyrażenia.
    
3. **Główna zasada:** Dwa wielomiany są równe wtedy i tylko wtedy, gdy ich współczynniki przy odpowiednich potęgach $x$ są dokładnie takie same.
    
4. Tworzymy układ równań i wyznaczamy szukane zmienne $a$ i $b$.
    

- **Przykład z zadania 8.96:** Po wymnożeniu nawiasów $(-3x + 5)(x^2 - 4x + 6)$ porównujecie wynik ze współczynnikami wielomianu głównego $W(x) = -3x^3 + (3a+b)x^2 - (4a+9b)x + 30$.
    
    Dzięki temu powstaje układ równań:
    
    $$\begin{cases} 3a + b = 17 \\ -(4a + 9b) = -33 \end{cases}$$
    
    Który rozwiązujecie metodą podstawiania ($b = 17 - 3a$).
    

## 5. Wyznaczanie reszty w postaci wielomianu (Zadanie 8.130)

Gdy dzielimy wielomian przez wyrażenie stopnia drugiego (np. przez trójmian kwadratowy), reszta nie musi być pojedynczą liczbą.

### Reguła stopnia reszty:

> Reszta z dzielenia $R(x)$ musi mieć stopień **ściśle niższy** niż stopień dzielnika $P(x)$.
> 
> Jeśli dzielnik jest stopnia 2 ($\text{st} = 2$), to reszta jest wielomianem co najwyżej stopnia 1, czyli zapisujemy ją w postaci ogólnej:
> 
> $$R(x) = ax + b$$

### Metoda rozwiązania:

1. Zapisujemy równanie: $W(x) = (x^2 + 3x + 2) \cdot Q(x) + (ax + b)$.
    
2. Dzielnik rozkładamy na czynniki: $x^2 + 3x + 2 = (x + 1)(x + 2)$, skąd mamy dwa miejsca zerowe: $x = -1$ oraz $x = -2$.
    
3. Podstawiamy te punkty do równania – dzięki temu człon z $Q(x)$ się zeruje, a my otrzymujemy układ równań z niewiadomymi $a$ i $b$:
    
    $$\begin{cases} W(-2) = 8 \implies -2a + b = 8 \\ W(-1) = -4 \implies -a + b = -4 \end{cases}$$
    
4. Rozwiązując ten układ (w zeszycie poprzez podstawienie $b = 8 + 2a$), otrzymujecie:
    
    $$a = -12, \quad b = -16$$
    
    **Ostateczny wzór na resztę:** $R(x) = -12x - 16$.


## 6. Wzory skróconego mnożenia (stopnia 3.)

W zadaniach 8.49, 8.53 oraz na początku nowej partii (zdjęcie 9) kluczowe stały się wzory na sześcian sumy/różnicy oraz sumę/różnicę sześcianów.

- **Sześcian sumy:** $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
    
- **Sześcian różnicy:** $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$
    
- **Suma sześcianów:** $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$
    
- **Różnica sześcianów:** $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$
    

### Zasada stosowania:

Używacie ich zarówno do rozwijania wyrażeń (np. $(2 + a)^3$ w zadaniu 8.53), jak i do szybkiego zwijania równań, jak w zadaniu 8.220 (e), gdzie wyrażenie $64x^3 + (x+5)^3$ zostało rozłożone jako suma sześcianów, gdzie $a = 4x$, a $b = x+5$.

## 7. Metoda wyłączania wspólnego czynnika przed nawias (Grupowanie wyrazów)

To absolutna podstawa przy rozkładaniu wielomianów na czynniki (zadania 8.198, 8.201).

### Zasada działania (Grupowanie):

Gdy masz wielomian czteromianowy (np. stopnia 3), łączysz wyrazy w pary, wyciągasz z każdej pary coś wspólnego, a potem wyciągasz cały powtarzający się nawias.

- **Przykład z zadania 8.201 (b):**
    
    $$7x^3 + 2x^2 - 21x - 6 = 0$$
    
    Z pierwszej pary $(7x^3 + 2x^2)$ wyłączamy $x^2$, z drugiej $(-21x - 6)$ wyłączamy $-3$:
    
    $$x^2(7x + 2) - 3(7x + 2) = 0 \implies (7x + 2)(x^2 - 3) = 0$$
    
    Na koniec korzystacie ze wzoru na różnicę kwadratów ($a^2 - b^2$):
    
    $$(7x + 2)(x - \sqrt{3})(x + \sqrt{3}) = 0$$
    

## 8. Twierdzenie o pierwiastkach wymiernych wielomianu

Gdy grupownaie nie działa (np. zadania 8.207, 8.112 f), szukacie pierwiastków za pomocą dzielników wyrazu wolnego.

### Reguła (Zapisana w zeszycie jako $D_z$):

> Jeśli wielomian o współczynnikach całkowitych ma pierwiaszek całkowity, to jest on jednym z dzielników wyrazu wolnego ($a_0$).

- **Zasada rozwiązania z zadania 8.207 (b):** Dla wielomianu $x^3 + 3x - 4 = 0$, wyraz wolny to $-4$. Dzielniki to $D_4 = \{ \pm 1, \pm 2, \pm 4 \}$.
    
    1. Sprawdzacie po kolei: $W(1) = 1^3 + 3(1) - 4 = 0$.
        
    2. Skoro $W(1) = 0$, to liczba $1$ jest pierwiastkiem.
        
    3. Następnie używacie **Schematu Hornera**, żeby podzielić wielomian przez $(x - 1)$ i obniżyć jego stopień do równania kwadratowego, które kończycie klasyczną deltą ($\Delta$).
        

## 9. Równania dwukwadratowe (Metoda podstawiania / Podstawienie zmiennej $t$)

W zadaniach 2.60 (b) oraz 8.220 (d) pojawia się specyficzny typ równania stopnia 4., w którym występują tylko potęgi parzyste ($x^4$ oraz $x^2$).

### Metoda podstawienia (Zmienna pomocnicza):

Wprowadzamy nową zmienną $t = x^2$, przy założeniu, że $t \ge 0$. Wtedy $x^4 = t^2$.

- **Przykład z zadania 8.220 (d):**
    
    $$x^4 - 9x^2 + 8 = 0 \implies t^2 - 9t + 8 = 0$$
    
    Rozwiązujecie zwykłe równanie kwadratowe z deltą, otrzymując: $t_1 = 8$ oraz $t_2 = 1$.
    
    Na koniec wracacie do zmiennej $x$:
    
    $$\begin{aligned} x^2 = 8 &\implies x = \sqrt{8} = 2\sqrt{2} \quad \lor \quad x = -2\sqrt{2} \\ x^2 = 1 &\implies x = 1 \quad \lor \quad x = -1 \end{aligned}$$
    

## 10. Przenoszenie na jedną stronę i szukanie wspólnego nawiasu

W zaawansowanych równaniach (zadanie 8.220 b, 8.224 a) zamiast wymnażać wszystko (co dałoby skomplikowane wyrażenia wyższych stopni), stosujecie sprytną zasadę przerzucania na lewą stronę i szukania wspólnego elementu.

- **Przykład z zadania 8.224 (a):**
    
    $$x^3(x^2 - 25) = 200x - 8x^3$$
    
    Po rozłożeniu prawej strony: $8x(25 - x^2)$, zauważacie, że nawias $(25 - x^2)$ to prawie to samo co $(x^2 - 25)$, tylko ze zmienionymi znakami: $-(5 - x)(5 + x)$.
    
    Dzięki sprowadzeniu do wspólnej postaci wyciągacie cały nawias $(x^2 - 25)$ przed nawias główny:
    
    $$(x^3 - 8x)(x^2 - 25) = 0$$
    
    Co daje natychmiastowe rozbicie na proste równania: $x(x^2 - 8) = 0 \implies x=0, x=\pm 2\sqrt{2}$ oraz $x^2 - 25 = 0 \implies x=\pm 5$.

### Krok 1: Wyznaczenie wszystkich pierwiastków (miejsc zerowych)

Przyrównaj każdy nawias (każdy czynnik) do zera i oblicz $x$. Jeśli w nawiasie znajduje się wyższa potęga (np. $x^2 - 4$ lub $x^3 - 1$), rozłóż ją do końca, aby znaleźć wszystkie ukryte miejsca zerowe.

- **Przykład z zadania d):** Nawias $(x^3 - 1) = 0$ daje pierwiastek $x = 1$. Z kolei $(x^2 - 4) = 0$ daje dwa pierwiastki: $x = 2$ oraz $x = -2$.
    

### Krok 2: Określenie krotności każdego pierwiastka

Policz, ile razy dany pierwiastek występuje w całym wyrażeniu, sumując potęgi nawiasów, z których pochodzi.

- **Krotność nieparzysta** (pierwiastek występuje 1, 3, 5... razy): w tym punkcie wykres **przebija** oś $X$ (przechodzi na drugą stronę).
    
- **Krotność parzysta** (pierwiastek występuje 2, 4, 6... razy): w tym punkcie wykres **odbija się** od osi $X$ (zostaje po tej samej stronie).
    

> **Przykład z zadania d):**
> 
> Pierwiastek $x = 1$ pojawia się w $(1-x)^5$ (5 razy) oraz w $(x^3-1)$ (1 raz). Łącznie: $5 + 1 = 6$ razy $\rightarrow$ **krotność parzysta** (wykres się odbije).

### Krok 3: Ustalenie znaku po prawej stronie (skąd zacząć rysować)

Musisz dowiedzieć się, czy Twój „wężyk” zaczyna się od prawej strony od góry (wartości dodatnie), czy od dołu (wartości ujemne).

**Prosty trik:** Pomnóż przez siebie znaki stojące przed najwyższymi potęgami $x$ w każdym nawiasie, pamiętając o potędze samego nawiasu.

- _W zadaniu d):_ W nawiasie $(1-x)^5$ przed $x$ stoi minus. Minus podniesiony do potęgi 5-tej daje **minus**. W pozostałych nawiasach przed $x$ są plusy. Minus $\cdot$ plus $\cdot$ plus $\cdot$ plus = **minus**. Zaczynamy więc rysować **od prawej strony od dołu**.
    

### Krok 4: Rysowanie wężyka

1. Zaznacz wszystkie odnalezione pierwiastki na osi $X$.
    
2. Zacznij prowadzić linię od prawej strony (od góry lub od dołu – zgodnie z Krokiem 3).
    
3. Idąc w lewą stronę, przechodź przez kolejne punkty:
    
    - Jeśli pierwiastek jest **nieparzystej** krotności – przebijaj oś.
        
    - Jeśli pierwiastek jest **parzystej** krotności – odbijaj od osi.
        

### Krok 5: Odczytanie i zapisanie rozwiązania

Spójrz na znak początkowej nierówności:

- Jeśli znak to $\ge 0$ lub $> 0$, wybierasz przedziały, gdzie wężyk znajduje się **nad osią** $X$ (włącznie z miejscami zerowymi dla $\ge$).
    
- Jeśli znak to $\le 0$ lub $< 0$, wybierasz przedziały, gdzie wężyk znajduje się **pod osią** $X$ (włącznie z miejscami zerowymi dla $\le$).
    

## Analiza przykładu b) (Zdjęcie nr 2)

Przeledźmy ten schemat na drugim zadaniu z Twojego zeszytu:

$$(2x - 4)(5 - x)(x - 2)(x^2 + 1) \le 0$$

1. **Szukanie miejsc zerowych:**
    
    - $2x - 4 = 0 \rightarrow x = 2$
        
    - $5 - x = 0 \rightarrow x = 5$
        
    - $x - 2 = 0 \rightarrow x = 2$
        
    - $x^2 + 1 = 0 \rightarrow$ brak pierwiastków rzeczywistych (kwadrat liczby powiększony o 1 nigdy nie będzie zerem).
        
2. **Określenie krotności:**
    
    - Pierwiastek $x = 2$ pojawił się 2 razy $\rightarrow$ **krotność parzysta** (odbicie).
        
    - Pierwiastek $x = 5$ pojawił się 1 raz $\rightarrow$ **krotność nieparzysta** (przebicie).
        
3. **Znak na końcu:**
    
    Przed $x$ w nawiasie $(5-x)$ stoi minus. Wynik całego mnożenia znaków będzie ujemny. Wykres startuje **z prawej strony od dołu**.
    
4. **Szkicowanie (od prawej do lewej):**
    
    - Dochodzimy do liczby $5$: krotność 1 (nieparzysta) $\rightarrow$ linia **przebija** oś i idzie w górę.
        
    - Dochodzimy do liczby $2$: krotność 2 (parzysta) $\rightarrow$ linia dotyka osi i **odbija się** z powrotem w górę.
        
5. **Odczytanie wyniku dla znaku $\le 0$ (pod osią lub na niej):**
    
    - Wykres jest pod osią dla $x$ od $5$ do $+\infty$, czyli: $x \in \langle 5, +\infty)$.
        
    - Ponieważ nierówność jest słaba ($\le$), musimy uwzględnić też miejsca, gdzie wielomian się zeruje. Punkt $x = 2$ leży dokładnie na osi, więc musimy go „dorzucić” do rozwiązania.
        

**Ostateczny wynik:** $x \in \langle 5, +\infty) \cup \{2\}$ — dokładnie tak, jak masz poprawnie zapisane na dole strony!