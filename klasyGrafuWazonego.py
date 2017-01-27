#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Klasy stanowiące strukturę danych reprezentującą problem przydziału w grafie ważonym.
Klasy zawarte w pliku ―
 * grafWazony,
  * wierzcholekLewegoPodgrafu,
 * rozwiazanyGrafWazony,
  * krawedzGrafuWazonego.
"""

import re
from random import seed, gauss, uniform
from Tkinter import Tk
from tkFileDialog import askopenfilename

class grafWazony:

    """
    Tworzy i przechowuje graf ważony do rozwiązania problemu przydziału w grafie ważonym.

    * generuje lewy podgraf,
    * tworzy kompletną listę krawędzi między każdym z wierzchołków w podgrafie lewym i każdym wierzchołkiem w podgrafie prawym,
    * dobiera losowe wartości wag wszystkich krawędzi,
    * posiada listę wierzchołków, jako obiekty klasy Wierzchołek lewego podgrafu
      (https://github.com/mwolodzk/WHM-Problem-PB7/wiki/Wierzcho%C5%82ek-lewego-podgrafu),
      
    Atrybuty klasy grafWazony:
    * wierzcholkiLewe ― lista wszystkich wierzchołków lewego podgrafu
    * liczbaLewychWierzcholkow ― ilość wierzchołków z lewego podgrafu
    * liczbaPrawychWierzcholkow ― ilość wierzchołków z prawego podgrafu
    
    Parametry konstruktora klasy grafWazony:
    * liczbaWierzcholkow = 40: rozmiar grafu. Zakładam, że graf musi być zawsze symetryczny, czyli liczba ta musi być parzysta
    * wczytacPlik = "nie": wpisz "tak", jeśli chcesz wczytać graf z pliku tekstowego 
                           w formacie podanym po wywołaniu metody strukturaPlikuZGrafemWazonym()
    
    Metody klasy grafWazony:
    * strukturaPlikuZGrafemWazonym() ― wyświetlenie struktury grafu ważonego zapisanego w pliku tekstowym i przyjmowanym przez klasę.
    """
    
    _ziarno = 576                  # ziarno dla generatora liczb losowych
        
    def __init__(self, liczbaWierzcholkow = 40, wczytacPlik = "nie"):
        # konstruktor grafu o podanej liczbie wierzchołków i 
        # wagach pobranych z pliku lub wygenerowanych losowo
        self.wierzcholkiLewe = []       # lista wszystkich wierzchołków lewego podgrafu
        seed(grafWazony._ziarno)       # ustawienie ziarna przy wywołaniu konstruktora klasy
        self.sciezkaPlikuZGrafem = "/home/michal/Pobrane/googledrive backup ― 29 may 2016/Politechnika/Studia doktorskie/Sem. IV/WHM/Projekt/Etap III/WHM-Problem-PB7/przykladowyGrafWazony.txt"
        
        if liczbaWierzcholkow%2 == 0:
            self.liczbaLewychWierzcholkow = liczbaWierzcholkow/2
            self.liczbaPrawychWierzcholkow = liczbaWierzcholkow/2
        else:
            raise IndexError, "Liczba wierzchołków musi być parzysta, a podałeś " + str(liczbaWierzcholkow)
            
        if wczytacPlik == "nie":
            self._generujGrafWazony()
        else:
            self._wczytajGrafZPliku(self.sciezkaPlikuZGrafem)
    
    def strukturaPlikuZGrafemWazonym(self):
        print """
        Wczytanie grafu ważonego z pliku o strukturze --
        
        <liczba wierzchołków w lewym podgrafie> 
           p1  p2  p3  .... pn
        l1 w11 w12 w13 .... w1n 
        l2 w21 w22 .....
        ...     ........
        ln wn1 wn2    ..... wnn 
        
        gdzie ln to n-ty wierzchołek z lewego podgrafu,
              pn to n-ty wierzchołek z prawego podgrafu.
        """
    
    def _wczytajGrafZPliku(self,sciezkaPliku=None):
        """
        Wczytanie grafu ważonego z pliku o strukturze --
        
        <liczba wierzchołków w lewym podgrafie> 
           p1  p2  p3  .... pn
        l1 w11 w12 w13 .... w1n 
        l2 w21 w22 .....
        ...     ........
        ln wn1 wn2    ..... wnn 
        
        gdzie ln to n-ty wierzchołek z lewego podgrafu,
              pn to n-ty wierzchołek z prawego podgrafu.
        """        
        Tk().withdraw()   # nie wyświetlaj pełnego GUI 
        if sciezkaPliku == None:
            sciezkaPliku = askopenfilename()   # pokaż okienko wyboru pliku i zwróć wybraną ścieżkę
        else:
            sciezkaPliku = "/home/michal/Pobrane/googledrive backup ― 29 may 2016/Politechnika/Studia doktorskie/Sem. IV/WHM/Projekt/Etap III/WHM-Problem-PB7/przykladowyGrafWazony.txt"
        
        with open(sciezkaPliku) as plikZGrafemWazonym:
            self.liczbaLewychWierzcholkow = int(plikZGrafemWazonym.readline())
            for wiersz in plikZGrafemWazonym:
                if wiersz.startswith('l'):
                    listaWagZWiersza = re.findall('[0-9.]+', wiersz)
                    listaWagZWiersza = [float(i) for i in listaWagZWiersza]
                    if len(listaWagZWiersza) != (self.liczbaLewychWierzcholkow + 1):
                        raise IOError, "Bledny odczyt wiersza: " + str(wiersz)
                    
                    numerWierzcholka = listaWagZWiersza[0]
                    wierzcholek = self.wierzcholekLewegoPodgrafu(numerWierzcholka,\
                                                                 listaWagZWiersza[1:])
                    self.wierzcholkiLewe.append(wierzcholek)
                    self.liczbaPrawychWierzcholkow = len(listaWagZWiersza[1:])
        
        plikZGrafemWazonym.close()
    
    def _generujGrafWazony(self):
        "Generacja grafu ważonego do problemu przydziału w grafie ważonym."
        for numerWierzcholka in range(self.liczbaLewychWierzcholkow):
            wylosowaneWagi = self._losujWagi()
            wierzcholek = self.wierzcholekLewegoPodgrafu(numerWierzcholka, wylosowaneWagi)
            self.wierzcholkiLewe.append(wierzcholek)
            self.liczbaPrawychWierzcholkow = len(wylosowaneWagi)
        self.liczbaLewychWierzcholkow = len(self.wierzcholkiLewe)
        
    def _losujWagi(self):
        "Losuje tyle wag, ile jest wierzchołków w prawym podgrafie"
        # gauss(5,2.3) # średnia powinna być przynajmniej dwa razy większa od wariancji
                       # dla dużej pewności (> 5%), że wagi będą dodatnie
                       # patrz https://en.wikipedia.org/wiki/Normal_distribution#Quantile_function
        wagi = [gauss(5,2.3) for indeks in range(self.liczbaPrawychWierzcholkow)]
        return wagi
    
    def _losujWagiWierzcholka(self, wierzcholek):
        "Losuje wagi dla wybranego wierzcholka."
        # gauss(5,2.3) # średnia powinna być przynajmniej dwa razy większa od wariancji
                       # dla dużej pewności (> 5%), że wagi będą dodatnie
                       # patrz https://en.wikipedia.org/wiki/Normal_distribution#Quantile_function
        for indeks in range(len(wierzcholek.wagi)):
            wierzcholek.wagi[indeks] = gauss(5,2.3)
    
#    def getWierzcholkiLewe(self):
#        "Zwraca listę obiektów klasy ,,Wierzchołek'' lewego podgrafu."
#        return wierzcholkiLewe
        
    class wierzcholekLewegoPodgrafu:
        
        """
        Klasa składowa Grafu ważonego, która przechowuje część struktury problemu przydziału w grafie ważonym.

        * ma swój numer porządkowy w grafie ważonym,,
        * posiada listę wag do wszystkich wierzchołków z prawego podgrafu,
        * potrafi zakomunikować swój numer porządkowy w grafie ważonym,
        * potrafi podać dowolną wagę ze swojej listy wag,
        
        Atrybuty klasy wierzcholekLewegoPodgrafu:
        * numerPorzadkowy ― numer porządkowy wierzchołka
        * wagi ― lista wag wszystkich krawędzi 
        """
        
        def __init__(self, _numerPorzadkowy, _listaWag):
            # utworzenie wierzcholka z numerem porządkowym i
            # ustaleniem wszystkich wag. Sprawdzenie czy 
            # numerPorzadkowy to liczba naturalna większa od 0
            self.numerPorzadkowy = _numerPorzadkowy   # numer porządkowy wierzchołka
            self.wagi = _listaWag                     # lista wag wszystkich krawędzi 
        
        
#        def getNumerPorzadkowy(self):
#            "Zwraca numer porządkowy wierzchołka."
#            
#        def getWaga(self, numerWagi):
#            "Zwraca numer n-tej wagi wierzchołka lub zwraca błąd, że wagi nie ma."
#            
#        def getWagi(self):
#            "Zwraca listę wag wierzchołka."
#            return __wagi
#            
#        def setWaga(self, numerWagi, waga):
#            "Ustawia n-tą wage wierzchołka, lub zwraca błąd jeśli wskaźnik na wagę wykracza poza listę wag."
#            _wagi[numerWagi] = waga
            
            
class rozwiazanyGrafWazony(grafWazony):
    
    """
    Klasa pochodna od Grafu ważonego. Reprezentuje dowolne rozwiązanie problemu przydziału w grafie ważonym.

    * ma jedno rozwiązanie problemu przydziału w grafie ważonym,
    * posiada obiekty klasy Krawędź grafu ważonego, tworzących jedno rozwiązanie,
    * potrafi podać wagę dowolnej krawędzi rozwiązania
    
    Atrybuty klasy rozwiazanyGrafWazony:
    * krawedzie ― lista wszystkich krawędzi rozwiązanego problemu przydziału w grafie ważonym
    * wierzcholkiLewe ― lista wszystkich wierzchołków lewego podgrafu
    * liczbaLewychWierzcholkow ― ilość wierzchołków z lewego podgrafu
    * liczbaPrawychWierzcholkow ― ilość wierzchołków z prawego podgrafu
    
    Parametry konstruktora klasy grafWazony:
    * liczbaWierzcholkow = 40: rozmiar grafu. Zakładam, że graf musi być zawsze symetryczny, czyli liczba ta musi być parzysta
    * wczytacPlik = "nie": wpisz "tak", jeśli chcesz wczytać graf z pliku tekstowego 
                           w formacie podanym po wywołaniu metody strukturaPlikuZGrafemWazonym()
    
    Metody klasy rozwiazanyGrafWazony:
    * znajdzKrawedzLewyWierzcholek(self, identyfikator) ― Zwraca obiekt typu krawędź, wychodzącej z wierzchołka lewego podgrafu o podanym identyfikatorze.
    * znajdzKrawedzPrawyWierzcholek(self, identyfikator) ― Zwraca obiekt typu krawędź, prowadzącą do wierzchołka prawego podgrafu o podanym identyfikatorze.
    * podajWageKrawedzi(self, identyfikator, lewyCzyPrawy = 'L') ― Podaje wagę krawędzi rozwiązania problemu przydziału w grafie ważonym. 
    * obliczKosztRozwiazania(self) ― Oblicza koszt obecnego rozwiązania
    """
        
    def __init__(self, liczbaWierzcholkow = 40, wczytacPlik = "nie"):
        # konstruktor rozwiązanego problemu przydziału w grafie  
        # o podanej liczbie wierzchołków i wagach pobranych z pliku lub wygenerowanych losowo
        self.wierzcholkiLewe = []       # lista wszystkich wierzchołków lewego podgrafu
        self.krawedzie = []             # lista wszystkich krawędzi rozwiązanego problemu przydziału
                                        # w grafie ważonym
        seed(grafWazony._ziarno)       # ustawienie ziarna przy wywołaniu konstruktora klasy                                
        
        if liczbaWierzcholkow%2 == 0:
            self.liczbaLewychWierzcholkow = liczbaWierzcholkow/2
            self.liczbaPrawychWierzcholkow = liczbaWierzcholkow/2
        else:
            raise IndexError, "Liczba wierzchołków musi być parzysta, a podałeś " + str(liczbaWierzcholkow)
            
        if wczytacPlik == "nie":
            self._generujGrafWazony()
        else:
            self._wczytajGrafZPliku()
        
        self._generujRozwiazanie()
        
    def znajdzKrawedzLewyWierzcholek(self, identyfikator):
        """
        Zwraca obiekt typu krawędź, wychodzącej z wierzchołka lewego podgrafu o podanym identyfikatorze.
        Identyfikatorem może być ― 
        * numer lewego wierzchołka,
        * obiekt typu wierzcholekLewegoPodgrafu, 
        """
        if type(identyfikator) is int:
            krawedzie = [krawedz for krawedz in self.krawedzie\
                                 if krawedz.numerWierzcholkaLewego == identyfikator]
            return krawedzie[0]
        elif type(identyfikator) is type(self.wierzcholkiLewe[0]):
            numerWierzcholkaLewego = identyfikator.numerPorzadkowy
            krawedzie = [krawedz for krawedz in self.krawedzie\
                                 if krawedz.numerWierzcholkaLewego == numerWierzcholkaLewego]
            return krawedzie[0]
        else:
            raise TypeError, "Brak wierzchołka o podanym identyfikatorze \"" + str(identyfikator) + "\""
                    
    def znajdzKrawedzPrawyWierzcholek(self, identyfikator):
        """
        Zwraca obiekt typu krawędź, prowadzącą do wierzchołka prawego podgrafu o podanym identyfikatorze.
        Identyfikatorem może być ― 
        * numer prawego wierzchołka, 
        """
        if type(identyfikator) is int:
            krawedzie = [krawedz for krawedz in self.krawedzie\
                                 if krawedz.numerWierzcholkaPrawego == identyfikator]
            return krawedzie[0]
        else:
            raise TypeError, "Brak wierzchołka o podanym identyfikatorze \"" + str(identyfikator) + "\""
            
    def podajWageKrawedzi(self, identyfikator, lewyCzyPrawy = 'L'):
        """
        Podaje wagę krawędzi rozwiązania problemu przydziału w grafie ważonym. 
        Identyfikatorem może być ― 
        * numer lewego wierzchołka,
        * numer prawego wierzchołka, 
        * obiekt typu wierzcholekLewegoPodgrafu, 
        """
        if lewyCzyPrawy == 'L':
            krawedz = self.znajdzKrawedzLewyWierzcholek(identyfikator)
        elif lewyCzyPrawy == 'P':
            krawedz = self.znajdzKrawedzPrawyWierzcholek(identyfikator)
        else:
            raise TypeError, "Brak wierzchołka o podanym identyfikatorze \"" + str(identyfikator) + "\""
            
        numerWierzcholkaLewego = krawedz.numerWierzcholkaLewego
        wierzcholekLewy = self.wierzcholkiLewe[numerWierzcholkaLewego]
        return wierzcholekLewy.wagi[krawedz.numerWierzcholkaPrawego]
    
    def obliczKosztRozwiazania(self):
        "Oblicza koszt obecnego rozwiązania"
        koszt = 0.0
        for krawedz in self.krawedzie:
            lewyWierzcholek = self.wierzcholkiLewe[krawedz.numerWierzcholkaLewego]
            wagaKrawedzi = lewyWierzcholek.wagi[krawedz.numerWierzcholkaPrawego]
            koszt += wagaKrawedzi
        return koszt
        
    def _generujRozwiazanie(self):
        """
        Utworzenie jednego poprawnego rozwiązania problemu przydziału w grafie ważonym.
        
        Zakłada się przy tym, że graf jest symetryczny, czyli ilość wierzchołków z 
        prawego podgrafu równa jest ilość wierzchołków z prawego podgrafu.
        """
        listaIndeksowLewychWierzcholkow = range(self.liczbaLewychWierzcholkow)
        listaIndeksowPrawychWierzcholkow = range(self.liczbaPrawychWierzcholkow)
        
        for iterator in range(self.liczbaLewychWierzcholkow):
            NrWylosowanegoLewegoWierzcholka = listaIndeksowLewychWierzcholkow\
                [int(uniform(0, len(listaIndeksowLewychWierzcholkow)))]
            NrWylosowanegoPrawegoWierzcholka = listaIndeksowPrawychWierzcholkow\
                [int(uniform(0, len(listaIndeksowPrawychWierzcholkow)))]
            
            #waga = self.wierzcholkiLewe[NrWylosowanegoLewegoWierzcholka].\
            #            wagi[NrWylosowanegoPrawegoWierzcholka]
            krawedz = self.krawedzGrafuWazonego(NrWylosowanegoLewegoWierzcholka,\
                                                NrWylosowanegoPrawegoWierzcholka)
            self.krawedzie.append(krawedz)
            listaIndeksowLewychWierzcholkow.remove(NrWylosowanegoLewegoWierzcholka)
            listaIndeksowPrawychWierzcholkow.remove(NrWylosowanegoPrawegoWierzcholka)
            
    class krawedzGrafuWazonego:
        
        """
        Klasa składowa Grafu ważonego, która stanowi element rozwiązania problemu przydziału w grafie ważonym.

        * posiada numer wierzchołka lewego podgrafu, z którego wychodzi,
        * ma numer wagi z listy obiektu klasy Wierzchołek lewego podgrafu, któremu odpowiada,
        
        Atrybuty klasy krawedzGrafuWazonego:
        * numerWierzcholkaPrawego ― numer porządkowy wierzchołka z prawego podgrafu, do którego krawędź się odnosi
        * numerWierzcholkaLewego ― numer porządkowy wierzchołka z lewego podgrafu, do którego krawędź się odnosi
        """
        
        def __init__(self, numerWierzcholkaLewego, numerWagi):
            # ustalenie numeru wierzchołka z lewego podgrafu i 
            # do którego wierzchołka w prawego podgrafu prowadzi
            self.numerWierzcholkaPrawego = numerWagi              # numer porządkowy wierzchołka z prawego podgrafu,
                                                                  # do którego krawędź się odnosi
            self.numerWierzcholkaLewego = numerWierzcholkaLewego  # numer porządkowy wierzchołka z lewego podgrafu,
                                                                  # do którego krawędź się odnosi
            
            
