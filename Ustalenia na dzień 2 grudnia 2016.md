### Michał ― 
 * stworzę klasę graf, żeby Łukasz mógł testować algorytm,
 * stworzyć klasę ,,Doświadczenie'',
 * utworzyć obiekt klasy graf ważony do testów w głównej pętli do testów,
 * ten graf ważony musi być ustalony,
 * usunąć klasę ,,generator grafów'' i jej funkcjonalność przenieśc do klasy ,,rozwiązany graf ważony''
 * ,,rozwiązany graf ważony'' powinien mieć możliwość generacji grafów z losowymi wagami lub czytać z pliku strukturę grafu i umieszczać ją w swojej strukturze danych,
 * stworzyć przykładowy plik ze strukturą grafu,
 * ,,Sterownik doświadczeniem'' zmienić na ,,Doświadczenie'',
 
### ,,Doświadczenie'' ―
  * pyta o nazwę pliki z gotowym grafem lub czy losowo generować graf,
 
### ,,Rozwiązany graf ważony'' posiada --
 * listę wierzchołków, jako obiekty klasy ,,Wierzchołek,
 * liczbę ,,Krawędzi'' tworzących jedno rozwiązanie,
 
### ,,Wierzchołek lewego podgrafu'' ―
 * ma swój numer porządkowy,
 * ma listę wag do wszystkich wierzchołków z prawego podgrafu,
 
### ,,Krawędź'' ―
 * ma numer ,,Wierzchołka lewego podgrafu'',
 * ma numer wagi z listy ,,Wierzchołka lewego podgrafu'' któremu odpowiada,
 
### Struktura grafu czytana z pliku ma postać 
Liczba wierzchołków w lewym podgrafie,
[macierz x na x z listą wag.]

