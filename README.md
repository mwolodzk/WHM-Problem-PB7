# WHM-Problem-PB7
Zastosowanie symulowanego wyżarzania do rozwiązywania problemu przydziału w grafie ważonym.

## Cel projektu
Celami projektowymi są 
* zbadanie złożoności obliczeniowej algorytmu symulowanego wyżarzania, 
* zbadanie efektywności algorytmu w znajdowaniu optimum dla różnych zakresów parametru temperatury wyżarzania,
* porównanie różnych algorytmów schładzania, w tym schładzania jednorodnego i niejednorodnego,
* przeanalizowanie różnych sposobów aktualizacji temperatury (schematu schładzania),
* wizualizacja przebiegu dochodzenia algorytmu do rozwiązania.


## Opis problemu
Na rys. 1 został przedstawiony graf składający się z dwóch podgrafów: lewego oraz prawego.
Przydział w takim grafie jest połączeniem każdego węzła w grafie lewym z jednym węzłem w grafie prawym przy czym dopuszczalne jest by do każdego węzła dochodziła tylko jedna krawędź.  
W postawionym problemie wagi krawędzi (z każdego węzła grafu lewego do każdego węzła grafu prawego) są wybierane w sposób losowy.
Celem problemu jest znalezienie takiego przydziału, w którym suma wag krawędzi grafu jest najmniejsza.

## Schemat metody rozwiązania problemu
1. Wylosowanie rozwiązania
2. Modyfikacja istniejącego rozwiązania poprzez znalezienie rozwiązania w pobliżu istniejącego (np. poprzez zamianę jednej krawędzi)
3. Ewaluacja nowego rozwiązania.
4. Jeśli rozwiązanie jest lepsze od poprzedniego to wybieramy te rozwiązanie. Jeśli jest gorsze wybieramy jest z pewnym prawdopodobieństwem w zależności od temperatury.
5. Aktualizujemy temperaturę (co jedną (schładzanie jednorodne) lub co kilka iteracji (schładzanie niejednorodne))

Na rys. 2. został przedstawiony przykładowy przebieg dochodzenia algorytmu symulowanego wyżarzania do rozwiązania. Na początku rozwiązania gorsze przyjmujemy z większym prawdopodobieństwem, co pozwala na wybór zbocza z minimum globalnym. Wraz z trwaniem algorytmu prawdopodobieństwo wyboru gorszego rozwiązania maleje i znajdowane jest minimum w wybranym już zboczu funkcji. 


### Więcej na ― [`Sprawozdanie z etapu pierwszego`](https://docs.google.com/document/d/1WYCxnshAwNDnHHsAOg-h27Iu1ziimTfWvYYE1A3wL8E/edit?usp=sharing)

### Sprawdź też [stronę wiki](https://github.com/mwolodzk/WHM-Problem-PB7/wiki) tego projektu.
