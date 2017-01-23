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
import matplotlib.pyplot as plt
import numpy as np
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
        
        self.parametryDoswiadczenia = {
            'temperaturaPoczatkowa': self.temperaturaPoczatkowa,
            'temperaturaKoncowa': self.temperaturaKoncowa,
            'schematSchladzania': self.schematSchladzania,
            'wersjaAlgorytmu': self.wersjaAlgorytmu,
            'iloscWierzcholkowLewych': self.iloscWierzcholkowLewych,
            'iloscWierzcholkowPrawych': self.iloscWierzcholkowPrawych,
            'zakresWag': zakresWag,
            }
        
    def _czyWczytacGrafZPliku(self):
        "Ustala, czy losowo generować graf, czy odczytać strukturę grafu ważonego z pliku."
        decyzja = str(raw_input("Czy wczytać strukturę grafu ważonego z pliku: "))
        if decyzja == "tak" or decyzja == "t":
            return True
        else
            return False
    
    def T(self, schemat = self.schematSchladzania):
        """
        Zmienia obecną temperaturę zgodnie z wybranym schematem schładzania. Ustala parametry schematów schładzania.
        Akceptowane schematy schładzania to --
        1. Boltzmanna (Logarytmiczny),
        2. Cauchy'ego (Liniowy),
        3. Geometryczny.
        """
        print "Wybrany schemat schładzania to " + str(schemat)
        self.parametryDoswiadczenia['schematSchladzania'] = schemat
        if schemat == "Boltzmanna" or schemat == "Logarytmiczny":
            self.temperatura = self.temperaturaPoczatkowa * (1.0/log(self.k2))
            return self.temperatura
        elif schemat == "Cauchy'ego" or schemat == "Liniowy":
            self.temperatura = self.temperaturaPoczatkowa * (1.0/k2)
            return self.temperatura
        elif schemat == "Geometryczny":
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
        elif type(zakresWag[0]) != int or type(zakresWag[1]) != int:
            raise ValueError, "Niewłaściwy format wag " + str(zakresWag)
        else:
            self.zakresWag = zakresWag
            
        self.parametryDoswiadczenia['iloscWierzcholkowLewych'] = self.iloscWierzcholkowLewych
        self.parametryDoswiadczenia['iloscWierzcholkowPrawych'] = self.iloscWierzcholkowPrawych
        self.parametryDoswiadczenia['zakresWag'] = self.zakresWag
    
    def stworzRozwiazanyGrafWazony(self):
        "Tworzy obiekt klasy rozwiazanyGrafWazony zgodnie z otrzymanymi danymi."
        liczbaWierzcholkow = self.iloscWierzcholkowLewych + self.iloscWierzcholkowPrawych
        decyzjaOWczytaniu = self._czyWczytacGrafZPliku()
        return graf.rozwiazanyGrafWazony(liczbaWierzcholkow, decyzjaOWczytaniu)
        
    def rozwiazProblem(self):
        "Rozwiązuje problem przydziału w grafie ważonym metodą symulowanego wyżarzania. Używa parametry doświadczenia z obiektu klasy ,,doswiadczenie''"
        # należy uzupełnić kodem wyołującym algorytm symulowanego wyżarzania
        
    def analizujWynikiAlgorytmu(self):
        "Analizuje wyniki rozwiązywania problemu przydziału w grafie ważonym za pomocą symulowanego wyżarzania."
        analiza = analizatorWynikow(self.parametryDoswiadczenia)
        analiza.analizuj()
        
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
    
    def __init__(self, parametryDoswiadczenia, daneZSymulatora = None):
        """
        Konstruktor Analizatora Wyników. Otrzymuje
         * parametryDoswiadczenia – słownik (dictionary) zawierający parametry doświadczenia
         * daneZSymulatora – ...
        """
        # Warto od razu pobrać dane doświadczenia od sterownika doświadczeniem – klasa doswiadczenie
        self.parametryDoswiadczenia = parametryDoswiadczenia
        self.temperaturaPoczatkowa = parametryDoswiadczenia['temperaturaPoczatkowa']
        self.temperaturaKoncowa = parametryDoswiadczenia['temperaturaKoncowa']
        self.iloscWierzcholkowLewych = parametryDoswiadczenia['iloscWierzcholkowLewych']
        self.iloscWierzcholkowPrawych = parametryDoswiadczenia['iloscWierzcholkowPrawych']
        self.zakresWag = parametryDoswiadczenia['zakresWag']
        
    def analizuj(self):
        """
        Dokonuje analizy zastosowania symulowanego wyżarzania do rozwiązywania problemu przydziału w 
        grafie ważonym. 
        """
        # Tutaj pojawi się kod całej analizy. Warto wykorzystać funkcje składowe klasy.
        
        # Graficzna reprezentacja analizy
        self._przedstawGraficznie()
        
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
        self.wizualizatorWynikow(dane,"Rozw")   # ,,dane'' przesłane w dowolnej formie, dostosuj kod klasy wizualizatorWynikow
        self.wizualizatorWynikow(dane)          # ,,dane'' przesłane w dowolnej formie, dostosuj kod klasy wizualizatorWynikow
        
        
    class wizualizatorWynikow:
    
        """
        Nakładka na analizatora wyników, która umożliwia przedstawienie graficznie wyników
        działania algorytmu symulowanego wyżarzania i uzyskanych z jego pomocą rozwiązań problemu PB7.

        * przedstawia graficznie proces dochodzenia algorytmu do rozwiązania,
        * tworzy wykresy złożoności obliczeniowej algorytmu w zależności od jego parametrów.
        
        """
    
        def __init__(self, dane, wykresy=None):
            """
            Konstruktor Wizualizatora Wyników. Przyjmuję, że domyślnie wszystkie wykresy analityczne są rysowane.
            Wykresy powinny być przekazane w formie wiązki (tuple). Dostępne wykresy to
             * O(n) -- wykres złożoności obliczeniowej algorytmu symulowanego wyżarzania w zależności od jego parametrów,
             * E(T) -- wykres efektywności algorytmu w znajdowaniu optimum dla różnych zakresów parametru temperatury wyżarzania.
             * A(J,NJ) -- graficzne porównanie algorytmów schładzania – jednorodnego (J) i niejednorodnego (NJ).
             * Sch -- graficzna analiza różnych sposobów aktualizacji temperatury (schematów schładzania).
             * Rozw -- wizualizacja przebiegu dochodzenia algorytmu do rozwiązania.
            """
            self.wykresy = wykresy
            self.dane = dane
            
            if self.wykresy == None:
                plt.figure(); _rysujWykresZlozonosciObliczeniowej()
                plt.figure(); _rysujWykresT()
                plt.figure(); _rysujPorownanieAlgorytmow()
                plt.figure(); _rysujPorownanieSchematowSchladzania()
            if "O(n)" in self.wykresy:
                plt.figure(); _rysujWykresZlozonosciObliczeniowej()
            if "E(T)" in self.wykresy:
                plt.figure(); _rysujWykresT()
            if "A(J,NJ)" in self.wykresy:
                plt.figure(); _rysujPorownanieAlgorytmow()
            if "Sch" in self.wykresy:
                plt.figure(); _rysujPorownanieSchematowSchladzania()
            if "Rozw" in self.wykresy:
                plt.figure(); _rysujDochodzenieDoRozwiazania()
                
            show()
            
        def _rysujWykresZlozonosciObliczeniowej(self):
            "Rysuje wykres złożoności obliczeniowej O(n) algorytmu symulowanego wyżarzania w zależności od jego parametrów."
            iloscIteracji = self.dane... # wstawić ilość iteracji algorytmu ze struktury ,,dane''
            zlozonosc = self.dane...     # tutaj trzeba wstawić odpowiednie pole ze sruktury ,,dane''
            
            n = np.arange(0, iloscKrokow, 1) # zmienna OX
            O = np.asarray(zlozonosc)        # zamiana na typ array, poręczny do rysowania wykresów, oś OY
            
            plt.plot(n,O)                    # rysowanie wykresu 
            
            plt.title('Złożoność obliczeniowa O(n)')
            plt.ylabel('O(n)')
            plt.xlabel('n')
            
        def _rysujWykresT(self):
            "Rysuje wykres efektywności algorytmu E(T) w znajdowaniu optimum dla różnych zakresów parametru temperatury wyżarzania."
            T = self.dane...    # wstawić zakresy temperatur z pola struktury ,,dane''
            E = self.dane...    # wstawić efektywności algorytmu z pola struktury ,,dane''
            
            T = np.asarray(T)   # zamiana na typ array, oś OX
            E = np.asarray(E)   # zamiana na typ array, oś OY
            
            plt.plot(T,E)       # rysowanie wykresu
            
            plt.title('Efektywność algorytmu w zależności od temperatury')
            plt.ylabel('Efektywność')
            plt.xlabel('T')
                      
        def _rysujPorownanieAlgorytmow(self):
            "Przedstawia graficznie porównanie algorytmów schładzania – jednorodnego (J) i niejednorodnego (NJ)."
            J = self.dane...    # wstawić dane o efektywności algorytmu jednorodnego z pola struktury ,,dane''
            NJ = self.dane...   # wstawić dane o efektywności algorytmu niejednorodnego z pola struktury ,,dane''
            
            ind = (0,1)              # indeksy algorytmów, 0 – jednorodny, 1 – niejednorodny
            Y = (J,NJ)               # oś OY
            
            plt.bar(ind,Y)
            
            plt.title('Schładzanie jednorodne (J) i niejednorodne (NJ)')
            plt.ylabel('Efektywność')
            plt.xticks(ind, ('jednorodne','niejednorodne'))
            
        def _rysujPorownanieSchematowSchladzania(self):
            "Przedstawia graficznie analizę różnych sposobów aktualizacji temperatury (schematów schładzania)."
            schematy = self.dane...    # wstawić przebadane schematy schładzania z pola struktury ,,dane''
            E = self.dane...            # wstawić dane o efektywności schematów schładzania z pola struktury ,,dane''
            
            ind = np.arange(len(schematy)) # indeksy schematów schładzania
            E = np.asarray(E)               # efektywności kolejnych algorytmów
            
            plt.bar(ind,E)
            
            plt.title('Efektywność schematów schładzania')
            plt.ylabel('Efektywność')
            plt.xticks(ind, schematy)      # zakładam, że zmienna ,,algorytmy'' to lista lub wiązka z nazwami schematów schładzania
            
        def _rysujDochodzenieDoRozwiazania(self):
            "Wizualizacja przebiegu dochodzenia algorytmu do rozwiązania."
            iloscIteracji = self.dane...    # wstawić ilość iteracji wykonanych przez algorytm
            fE = self.dane...               # wstawić funkcję oceny rozwiązania ze struktury ,,dane''
            
            x = np.arange(iloscIteracji)    # oś OX
            y = np.asarray(fE)              # oś OY
            
            plt.plot(x,y)                   # rysowanie wykresu
            
            plt.title('Dochodzenie algorytmu do rozwiązania')
            plt.ylabel('Funkcja oceny')
            plt.xlabel('Iteracja')
        
    
    
