#!/usr/bin/python


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
        
    def __generujGrafWazony(self, _liczbaLewychWierzcholkow):
        "Generacja grafu ważonego do problemu przydziału w grafie ważonym."
        
    def __losujWagiWierzcholka(self, _wierzcholek):
        "Losuje wagi dla wybranego wierzcholka."
    
    
