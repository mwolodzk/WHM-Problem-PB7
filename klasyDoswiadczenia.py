#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Klasy służące do rozwiązania problemu przydziału w grafie ważonym
z zastosowaniem symulowanego wyżarzania
Klasy zawarte w pliku ―
 * doswiadczenie,
 * analizator_wynikow,
  * wizualizator_wynikow,
"""

import klasyGrafuWazonego as graf
from numpy import log

class doswiadczenie:

    """
    Zarządza przeprowadzanym doświadczeniem lub serią doświadczeń, komunikując się z blokami wykonawczymi. 
    Tworzy warstwę komunikacji z użytkownikiem programu. W kontekście problemu PB7 do jego obowiązków należy ―

    * proszenie o podanie nazwy pliku z kompletnym grafem ważonym,
    * ustalanie czy losowo generować graf, czy odczytać strukturę z pliku,
    * ustalanie parametrów symulowanego wyżarzania — temperaturę, ….
    * ustalanie rodzaju algorytmu schładzania, w tym schładzania jednorodnego i niejednorodnego,
    * ustalanie schematu schładzania,
    * ustalanie zakresu temperatury wyżarzania,
    * określanie rozmiaru grafu ważonego ― ilość wierzchołków lewego podgrafu, ilość wierzchołkow prawego podgrafu
    * określanie dopuszczalnego zakresu wag krawędzi grafu ważonego,

    """
    
    def __init__(self, temperaturaPoczatkowa = 300, temperaturaKoncowa = 0, wersja = "jednorodna"):
        """
        Konstruktor doświadczenia.
         * Ustala temperatury początkową i końcową.
         * Wybranie domyślnego schematu schładzania.
         * Ustala wersję algorytmu -- jednorodną lub niejednorodną.
         * Ustala domyślną ilość wierzchołków lewego i prawego podgrafu.
         * Ustala domyślny zakres wag grafu ważonego.
         * Ustala wartość parametru schematu schładzania "k2" na 1.
        """
        self.temperaturaPoczatkowa = temperaturaPoczatkowa
        self.temperaturaKoncowa = temperaturaKoncowa
        self.schematSchladzania = "Boltzmanna"
        self.wersjaAlgorytmu = wersja
        self.iloscWierzcholkowLewych = 10
        self.iloscWierzcholkowPrawych = 10
        self.zakresWag = [0, 10]
        self.k2 = 1
        
    def _czyWczytacGrafZPliku(self):
        "Ustala, czy losowo generować graf, czy odczytać strukturę grafu ważonego z pliku."
        decyzja = str(raw_input("Czy wczytać strukturę grafu ważonego z pliku: "))
        if decyzja == "tak" or decyzja == "t":
            return True
        else
            return False
    
    def schematSchladzania(self, schemat = self.schematSchladzania):
        """
        Zmienia obecną temperaturę zgodnie z wybranym schematem schładzania. Ustala parametry schematów schładzania.
        Akceptowane schematy schładzania to --
        1. Boltzmanna (Logarytmiczny),
        2. Cauchy'ego (Liniowy),
        3. Geometryczny.
        """
        print "Wybrany schemat schładzania to " + str(schemat)
        if schemat == "Boltzmanna" or schemat == "Logarytmiczny":
            self.temperatura = self.temperaturaPoczatkowa * (1.0/log(self.k2))
            return self.temperatura
        else if schemat == "Cauchy'ego" or schemat == "Liniowy":
            self.temperatura = self.temperaturaPoczatkowa * (1.0/k2)
            return self.temperatura
        else if schemat == "Geometryczny":
            self.a = 0.5
            print "Ustawiam wartość parametru \"a\" na " + str(self.a)
            self.temperatura = self.temperaturaPoczatkowa * (self.a ** self.k2)
            return self.temperatura
        else:
            raise ValueError, "Nie ma takiego schematu schładzania " + str(schemat)
            return None

    def ustalenieGenerowanegoGrafu(self, iloscWierzcholkowLewych, iloscWierzcholkowPrawych, zakresWag):
        "Określa rozmiar grafu ważonego, określa dopuszczalny zakres wag krawędzi."
        self.iloscWierzcholkowLewych = int(iloscWierzcholkowLewych)
        self.iloscWierzcholkowPrawych = int(iloscWierzcholkowPrawych)
        if len(zakresWag) != 2:
            raise ValueError, "Niewłaściwy format wag " + str(zakresWag)
        else if type(zakresWag[0]) != int or type(zakresWag[1]) != int:
            raise ValueError, "Niewłaściwy format wag " + str(zakresWag)
        else:
            self.zakresWag = zakresWag
    
    def stworzRozwiazanyGrafWazony(self):
        "Tworzy obiekt klasy rozwiazanyGrafWazony zgodnie z otrzymanymi danymi."
        liczbaWierzcholkow = self.iloscWierzcholkowLewych + self.iloscWierzcholkowPrawych
        decyzjaOWczytaniu = self._czyWczytacGrafZPliku()
        return graf.rozwiazanyGrafWazony(liczbaWierzcholkow, decyzjaOWczytaniu)
        
class analizatorWynikow:

    """
    Umożliwia badanie i porównywanie rozwiązań problemu PB7 oraz badanie algorytmu symulowanego wyżarzania. 
    Wykonaną analizę przedstawia graficznie wizualizator wyników.

    * oblicza złożoność obliczeniową algorytmu symulowanego wyżarzania,
    * bada efektywność algorytmu w znajdowaniu optimum dla różnych zakresów parametru wyżarzania,
    * zapamiętuje rozwiązania uzyskane z algorytmu symulowanego wyżarzania,
    * zapamiętuje wyniki działania algorytmu symulowanego wyżarzania,
    * porównuje różne algorytmy schładzania,
    
    """
    
    def __init__(self):
        "Konstruktor Analizatora Wyników."
        
    def analizuj(self):
        """
        Dokonuje analizy zastosowania symulowanego wyżarzania do rozwiązywania problemu przydziału w 
        grafie ważonym. 
        """
        
    def _badajEfektywnoscAlgorytmu(self):
        "Zbadanie efektywności algorytmu w znajdowaniu optimum dla różnych zakresów parametru wyżarzania."
        
    def _obliczZlozonoscObliczeniowa(self):
        "Oblicza zlozonosc obliczeniową algorytmu symulowanego wyżarzania."
        
    def _zapamietajRozwiazanie(self):
        "Zapamiętuje rozwiązanie uzyskane z algorytmu symulotwanego wyżarzania."
        
    def _porownajAlgorytmySchladzania(self, algorytm1, algorytm2):
        "Porównuje podane algorytmy schładzania ..."
        
    def _przedstawGraficznie(self):
        "Przedstawienie graficzne wyników analizy."
        
        
    class wizualizatorWynikow:
    
        """
        Nakładka na analizatora wyników, która umożliwia przedstawienie graficznie wyników
        działania algorytmu symulowanego wyżarzania i uzyskanych z jego pomocą rozwiązań problemu PB7.

        * przedstawia graficznie proces dochodzenia algorytmu do rozwiązania,
        * tworzy wykresy złożoności obliczeniowej algorytmu w zależności od jego parametrów.
        
        """
    
        def __init__(self):
            "Konstruktor Wizualizatora Wyników."
            
        def _rysujWykresZlozonosciObliczeniowej(self):
            "Rysuje wykres złożoności obliczeniowej algorytmu symulowanego wyżarzania w zależności od jego parametrów."
            
        def _rysujWykresT(self):
            "Rysuje wykres efektywności algorytmu w znajdowaniu optimum dla różnych zakresów parametru temperatury wyżarzania."
            
        def _rysujPorownanie(self):
            "Przedstawia graficznie porównanie różnych algorytmów schładzania."
            
        def _rysujDochodzenieDoRozwiazania(self):
            "Wizualizacja przebiegu dochodzenia algorytmu do rozwiązania."
        
    
    
