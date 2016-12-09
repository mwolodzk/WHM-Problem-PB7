#!/usr/bin/python

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
    """
    
    __ziarno = 576                  # ziarno dla generatora liczb losowych
        
    def __init__(self, liczbaWierzcholkow = 40, sciezkaDoPlikuZGrafem = "brak"):
        # konstruktor grafu o podanej liczbie wierzchołków i 
        # wagach pobranych z pliku lub wygenerowanych losowo
        self.wierzcholkiLewe = []       # lista wszystkich wierzchołków lewego podgrafu
        
        if liczbaWierzcholkow%2 == 0:
            self.liczbaLewychWierzcholkow = liczbaWierzcholkow/2
            self.liczbaPrawychWierzcholkow = liczbaWierzcholkow/2
        else:
            self.liczbaLewychWierzcholkow = liczbaWierzcholkow/2 + 1
            self.liczbaPrawychWierzcholkow = liczbaWierzcholkow/2
            
        if sciezkaDoPlikuZGrafem == "brak":
            self.__generujGrafWazony()
        else:
            self.__wczytajGrafZPliku(sciezkaDoPlikuZGrafem)
    
    def __wczytajGrafZPliku(self, sciezka):
        """
        Wczytanie grafu ważonego z pliku o strukturze --
        
        <liczba wierzchołków w lewym podgrafie> 
           l1  l2  l3  .... ln
        p1 w11 w12 w13 .... w1n 
        p2 w21 w22 .....
        ...     ........
        pn wn1 wn2    ..... wnn 
        
        gdzie ln to n-ty wierzchołek z lewego podgrafu,
              pn to n-ty wierzchołek z prawego podgrafu.
        """        
        Tk().withdraw()   # nie wyświetlaj pełnego GUI 
        sciezkaPliku = askopenfilename()   # pokaż okienko wyboru pliku i zwróć wybraną ścieżkę
        
        with open(sciezkaPliku) as plikZGrafemWazonym:
            self.liczbaLewychWierzcholkow = int(plikZGrafemWazonym.readline())
            for wiersz in plikZGrafemWazonym:
                if wiersz.startswith('p'):
                    listaWagZWiersza = re.findall('[0-9.]+', wiersz)
                    listaWagZWiersza = [float(i) for i in listaWagZWiersza]
                    if len(listaWagZWiersza) != (self.liczbaLewychWierzcholkow + 1):
                        raise "Bledny odczyt wiersza z pliku", str(wiersz)
                    
                    numerWierzcholka = listaWagZWiersza[0]
                    wierzcholek = wierzcholekLewegoPodgrafu(numerWierzcholka,\
                                                            listaWagZWiersza[1:])
                    self.wierzcholkiLewe.append(wierzcholek)
                    self.liczbaPrawychWierzcholkow = len(listaWagZWiersza[1:])
        
        plikZGrafemWazonym.close()       
    
    def __generujGrafWazony(self):
        "Generacja grafu ważonego do problemu przydziału w grafie ważonym."
        for numerWierzcholka in range(self.liczbaLewychWierzcholkow):
            wylosowaneWagi = self.__losujWagi()
            wierzcholek = wierzcholekLewegoPodgrafu(numerWierzcholka, wylosowaneWagi)
            self.wierzcholkiLewe.append(wierzcholek)
            self.liczbaPrawychWierzcholkow = len(wylosowaneWagi)
        self.liczbaLewychWierzcholkow = len(wierzcholkiLewe)
        
    def __losujWagi(self):
        "Losuje tyle wag, ile jest wierzchołków w prawym podgrafie"
        seed(grafWazony.__ziarno)
        # gauss(5,2.3) # średnia powinna być przynajmniej dwa razy większa od wariancji
                       # dla dużej pewności (> 5%), że wagi będą dodatnie
                       # patrz https://en.wikipedia.org/wiki/Normal_distribution#Quantile_function
        wagi = [gauss(5,2.3) for indeks in range(self.liczbaPrawychWierzcholkow)]
        return wagi
    
    def __losujWagiWierzcholka(self, wierzcholek):
        "Losuje wagi dla wybranego wierzcholka."
        seed(grafWazony.__ziarno)
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
#            __wagi[numerWagi] = waga
            
            
class rozwiazanyGrafWazony(grafWazony):
    
    """
    Klasa pochodna od Grafu ważonego. Reprezentuje dowolne rozwiązanie problemu przydziału w grafie ważonym.

    * ma jedno rozwiązanie problemu przydziału w grafie ważonym,
    * posiada obiekty klasy Krawędź grafu ważonego, tworzących jedno rozwiązanie,
    """
        
    def __init__(self, liczbaWierzcholkow = 40, sciezkaDoPlikuZGrafem = "brak"):
        # konstruktor rozwiązanego problemu przydziału w grafie  
        # o podanej liczbie wierzchołków i wagach pobranych z pliku lub wygenerowanych losowo
        self.wierzcholkiLewe = []       # lista wszystkich wierzchołków lewego podgrafu
        self.krawedzie = []             # lista wszystkich krawędzi rozwiązanego problemu przydziału
                                        # w grafie ważonym
        
        if liczbaWierzcholkow%2 == 0:
            self.liczbaLewychWierzcholkow = liczbaWierzcholkow/2
            self.liczbaPrawychWierzcholkow = liczbaWierzcholkow/2
        else:
            self.liczbaLewychWierzcholkow = liczbaWierzcholkow/2 + 1
            self.liczbaPrawychWierzcholkow = liczbaWierzcholkow/2
            
        if sciezkaDoPlikuZGrafem == "brak":
            self.__generujGrafWazony()
        else:
            self.__wczytajGrafZPliku(sciezkaDoPlikuZGrafem)
        
        self.__generujRozwiazanie()
        
    def __generujRozwiazanie(self):
        """
        Utworzenie jednego poprawnego rozwiązania problemu przydziału w grafie ważonym.
        
        Zakłada się przy tym, że graf jest symetryczny, czyli ilość wierzchołków z 
        prawego podgrafu równa jest ilość wierzchołków z prawego podgrafu.
        """
        listaIndeksowLewychWierzcholkow = range(self.liczbaLewychWierzcholkow)
        listaIndeksowPrawychWierzcholkow = range(self.liczbaPrawychWierzcholkow)
        
        for iterator in range(liczbaLewychWierzcholkow):
            NrWylosowanegoLewegoWierzcholka = listaIndeksowLewychWierzcholkow\
                [int(uniform(0, len(listaIndeksowLewychWierzcholkow)))]
            NrWylosowanegoPrawegoWierzcholka = listaIndeksowPrawychWierzcholkow\
                [int(uniform(0, len(listaIndeksowPrawychWierzcholkow)))]
            
            krawedz = krawedzGrafuWazonego(NrWylosowanegoLewegoWierzcholka,\
                                           NrWylosowanegoPrawegoWierzcholka)
            listaIndeksowLewychWierzcholkow.remove(NrWylosowanegoLewegoWierzcholka)
            listaIndeksowPrawychWierzcholkow.remove(NrWylosowanegoPrawegoWierzcholka)
            
    class krawedzGrafuWazonego:
        
        """
        Klasa składowa Grafu ważonego, która stanowi element rozwiązania problemu przydziału w grafie ważonym.

        * posiada numer wierzchołka lewego podgrafu, z którego wychodzi,
        * ma numer wagi z listy obiektu klasy Wierzchołek lewego podgrafu, któremu odpowiada,
        """
        
        def __init__(self, numerWierzcholkaLewego, numerWagi):
            # ustalenie numeru wierzchołka z lewego podgrafu i 
            # do którego wierzchołka w prawego podgrafu prowadzi
            self.numerWierzcholkaPrawego = numerWagi              # numer porządkowy wierzchołka z prawego podgrafu,
                                                                  # do którego krawędź się odnosi
            self.numerWierzcholkaLewego = numerWierzcholkaLewego  # numer porządkowy wierzchołka z lewego podgrafu,
                                                                  # do którego krawędź się odnosi
            
            
