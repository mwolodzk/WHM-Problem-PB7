#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Zastosowanie symulowanego wyżarzania do rozwiązywania problemu przydziału w grafie ważonym.
"""

import klasyDoswiadczenia as kD


if __name__ == '__main__':
    #temperaturaPoczatkowa = 0
    #temperaturaKoncowa = 300
    d1 = doswiadczenie()
    d1.stworzRozwiazanyGrafWazony()
    
    # Wersja jednorodna algorytmu
    d1.schematSchladzania = 'Boltzmanna'
    d1.stworzRozwiazanyGrafWazony()
    d1.rozwiazProblem()
    d1.analizujWynikiAlgorytmu()
    
