#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Testuje poprawność struktury danych rozwiązanego problemu przydziału w grafie ważonym.
"""

import klasyGrafuWazonego

def testujTworzenieRozwiazanegoGrafuWazonego():
    
    badanaKlasa = klasyGrafuWazonego.rozwiazanyGrafWazony()
    print "Typ badanej klasy to: " + str(badanaKlasa)
    
    print "Ilość lewych wierzchołków wynosi " + str(badanaKlasa.liczbaLewychWierzcholkow)
    print "Ilość prawych wierzchołków wynosi " + str(badanaKlasa.liczbaPrawychWierzcholkow)
    assert badanaKlasa.liczbaLewychWierzcholkow == badanaKlasa.liczbaPrawychWierzcholkow, "Graf niesymetryczny! "
    
    wagiZPoprzedniego = [0]
    for wierzcholek in badanaKlasa.wierzcholkiLewe:
        print "Numer wierzcholka lewego: " + str(wierzcholek.numerPorzadkowy)
        print "Jego wagi to: " + str(wierzcholek.wagi)
        assert wagiZPoprzedniego[0] != wierzcholek.wagi[0], "Wagi [0] są identyczne. Coś nie tak z generacją wag!"
        wagiZPoprzedniego = wierzcholek.wagi
    
    krawedzieLewePosortowane = sorted(badanaKlasa.krawedzie, key = lambda krawedz: krawedz.numerWierzcholkaLewego)
    print "Losowe rozwiązanie to"
    for krawedz in krawedzieLewePosortowane:
        print str(krawedz.numerWierzcholkaLewego+1) + " --> " + str(krawedz.numerWierzcholkaPrawego+1)
        
    print "Waga krawędzi z 5-ego wierzchołka wynosi " + str(badanaKlasa.podajWageKrawedzi(5))
    print "Waga krawędzi do 4-ego wierzchołka wynosi " + str(badanaKlasa.podajWageKrawedzi(4, 'P'))
    print "Przekazanie przez obiekt klasy wierzchołek  " + str(badanaKlasa.podajWageKrawedzi(badanaKlasa.wierzcholkiLewe[5]))
    
    print "Całkowity koszt rozwiązania wynosi " + str(badanaKlasa.obliczKosztRozwiazania())
    
    print "Wczytywanie grafu ważonego z pliku tekstowego."
    badanaKlasa = klasyGrafuWazonego.rozwiazanyGrafWazony(wczytacPlik = "tak")
    assert badanaKlasa.wierzcholkiLewe, "Krawędzie grafu nie zostały wczytane!"
    
    wagiZPoprzedniego = [0]
    for wierzcholek in badanaKlasa.wierzcholkiLewe:
        print "Numer wierzcholka lewego: " + str(wierzcholek.numerPorzadkowy)
        print "Jego wagi to: " + str(wierzcholek.wagi)
        assert wagiZPoprzedniego[0] != wierzcholek.wagi[0], "Wagi [0] są identyczne. Coś nie tak z generacją wag!"
        wagiZPoprzedniego = wierzcholek.wagi
    
    krawedzieLewePosortowane = sorted(badanaKlasa.krawedzie, key = lambda krawedz: krawedz.numerWierzcholkaLewego)
    print "Losowe rozwiązanie to"
    for krawedz in krawedzieLewePosortowane:
        numerWierzcholkaLewego = krawedz.numerWierzcholkaLewego
        print str(krawedz.numerWierzcholkaLewego+1) + " --(" + str(badanaKlasa.podajWageKrawedzi(numerWierzcholkaLewego)) + \
              ")--> " + str(krawedz.numerWierzcholkaPrawego+1)

if __name__ == '__main__':
    testujTworzenieRozwiazanegoGrafuWazonego()

