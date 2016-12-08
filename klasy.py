#!/usr/bin/python

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

    def __init__(self):
        # domyślnie stwarzam graf o domyślnej liczbie wierzchołków
        # i losowych wagach.
        
    def __init__(self, _liczbaLewychWierzcholkow):
        # konstruktor grafu o podanej liczbie wierzchołków i
        # losowych wagach.
        
    liczbaLewychWierzcholkow = 20   # domyśla liczebność
    wierzcholkiLewe = []            # lista wszystkich wierzchołków lewego podgrafu
    
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
        
        plikZGrafemWazonym = open(sciezkaPliku)
        if plikZGrafemWazonym.closed:
            # Dopisać rzucany wyjątek
        
    def __generujGrafWazony(self, _liczbaLewychWierzcholkow):
        "Generacja grafu ważonego do problemu przydziału w grafie ważonym."
        
    def __losujWagiWierzcholka(self, _wierzcholek):
        "Losuje wagi dla wybranego wierzcholka."
    
    def getWierzcholkiLewe(self):
        "Zwraca listę obiektów klasy ,,Wierzchołek'' lewego podgrafu."
        
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
        
        wagi = set()            # lista wag wszystkich krawędzi 
        numerPorzadkowy = -1    # numer porządkowy wierzchołka
        
        def getNumerPorzadkowy(self):
            "Zwraca numer porządkowy wierzchołka."
            
        def getWaga(self, numerWagi):
            "Zwraca numer n-tej wagi wierzchołka lub zwraca błąd, że wagi nie ma."
            
            
class rozwiazanyGrafWazony(grafWazony):
    
    """
    Klasa pochodna od Grafu ważonego. Reprezentuje dowolne rozwiązanie problemu przydziału w grafie ważonym.

    * ma jedno rozwiązanie problemu przydziału w grafie ważonym,
    * posiada obiekty klasy Krawędź grafu ważonego tworzących jendo rozwiązanie,
    """
    
    def __init__(self):
        # domyślnie stwarzam graf o domyślnej liczbie wierzchołków
        # i losowych wagach oraz losowym rozwiązaniu.
        
    def __init__(self, _liczbaLewychWierzcholkow):
        # konstruktor grafu o podanej liczbie wierzchołków i
        # losowych wagach.
        
    krawedzie = [];   # lista wszystkich krawędzi rozwiązanego problemu przydziału
                      # w grafie ważonym
        
    def __generujRozwiazanie(self):
        "Utworzenie jednego poprawnego rozwiązania problemu przydziału w grafie ważonym."
        
    def getKrawedzie(self):
        "Zwraca listę krawędzi rozwiązanego problemu przydziału w grafie ważonym."
            
    class krawedzGrafuWazonego:
        
        """
        Klasa składowa Grafu ważonego, która stanowi element rozwiązania problemu przydziału w grafie ważonym.

        * posiada numer wierzchołka lewego podgrafu, z którego wychodzi,
        * ma numer wagi z listy obiektu klasy Wierzchołek lewego podgrafu, któremu odpowiada,
        """
        
        def __init__(self, _numerWierzcholkaLewego, _numerWagi):
            # ustalenie numeru wierzchołka z lewego podgrafu i 
            # do którego wierzchołka w prawego podgrafu prowadzi
            
        numerWierzcholkaPrawego = -1   # numer porządkowy wierzchołka z prawego podgrafu,
                                       # do którego krawędź się odnosi
        numerWierzcholkaLewego = -1    # numer porządkowy wierzchołka z lewego podgrafu,
                                       # do którego krawędź się odnosi
            
