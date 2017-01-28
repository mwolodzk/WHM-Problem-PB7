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
    
    def __init__(self, temperaturaPoczatkowa = 30000, temperaturaKoncowa = 0.1, schematSchladzania = "Boltzmanna", wersja = "jednorodna",decyzja="tak",iloscWierzcholkowLewych = 5,k1=3,a=0.5):
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
        self.schematSchladzania = schematSchladzania
        self.wersjaAlgorytmu = wersja
        self.iloscWierzcholkowLewych = iloscWierzcholkowLewych
        self.iloscWierzcholkowPrawych = iloscWierzcholkowLewych
        self.zakresWag = [0, 10]
        self.k2 = 1
        self.k1 = k1
        self.decyzja=decyzja
        self.a=a
        
    def _czyWczytacGrafZPliku(self):
        "Ustala, czy losowo generować graf, czy odczytać strukturę grafu ważonego z pliku."
        decyzja = str(raw_input("Czy wczytać strukturę grafu ważonego z pliku: "))
        if decyzja == "tak" or decyzja == "t":
            return True
        else:
            return "nie"
    
    def ustalTemperature(self,temp):
        """
        Zmienia obecną temperaturę zgodnie z wybranym schematem schładzania. Ustala parametry schematów schładzania.
        Akceptowane schematy schładzania to --
        1. Boltzmanna (Logarytmiczny),
        2. Cauchy'ego (Liniowy),
        3. Geometryczny.
        """
        
        schemat=self.schematSchladzania


        
        if schemat == "Boltzmanna" or schemat == "Logarytmiczny":
            self.temperatura = temp * (1.0/log(1.8+self.k2))
            self.k2=self.k2+1
            return self.temperatura
        elif schemat == "Cauchy'ego" or schemat == "Liniowy":

            self.k2 = self.k2 + 1
            self.temperatura = temp * (1.0/self.k2)

            return self.temperatura
        elif schemat == "Geometryczny":

            self.temperatura = temp * (self.a ** self.k2)
            self.k2 = self.k2 + 1
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
        elif type(zakresWag[0]) != int or type(zakresWag[1]) != int:
            raise ValueError, "Niewłaściwy format wag " + str(zakresWag)
        else:
            self.zakresWag = zakresWag
    
    def stworzRozwiazanyGrafWazony(self):
        "Tworzy obiekt klasy rozwiazanyGrafWazony zgodnie z otrzymanymi danymi."
        liczbaWierzcholkow = self.iloscWierzcholkowLewych + self.iloscWierzcholkowPrawych
        #decyzjaOWczytaniu = self._czyWczytacGrafZPliku()
        decyzjaOWczytaniu = self.decyzja
        return graf.rozwiazanyGrafWazony(liczbaWierzcholkow, decyzjaOWczytaniu)
