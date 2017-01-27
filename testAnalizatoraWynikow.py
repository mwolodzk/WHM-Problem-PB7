#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Badanie analizatora i wizualizatora wyników
"""

import klasyDoswiadczenia as d
from random import randint, sample, uniform

def losujDane():
    iteracje = randint(1,50)
    fE = tuple([uniform(0,10) for x in range(10)])
    fEmin = min(fE)
    schemat = sample(('Boltzmann','Liniowy','Geometryczny'), 1)[0]
    a = uniform(0.001,0.5)
    t = uniform(1.0,20.0)
    iloscPosrednich = randint(5,100)
    Tmax = randint(100,300)
    wersja = sample(('J','NJ'), 1)[0]
    
    return {
        'iteracje': iteracje,
        'fE': fE,
        'fEmin': fEmin,
        'schemat': schemat,
        'a': a,
        't': t,
        'iloscPosrednich': iloscPosrednich,
        'Tmax': Tmax,
        'wersja': wersja
        }
        
if __name__ == '__main__':

    d1 = d.doswiadczenie()
    d1.ustalenieGenerowanegoGrafu(5,5,(0,5))
    a1 = d.analizatorWynikow(d1.parametryDoswiadczenia)
    
    print "Ile doświadczeń chcesz wyrysować? "; ile = input()
    
    for i in range(ile):
        a1.analizuj(losujDane())   

    
