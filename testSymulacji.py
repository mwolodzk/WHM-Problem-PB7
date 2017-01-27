#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Testuje poprawność struktury danych rozwiązanego problemu przydziału w grafie ważonym.
"""

import klasyGrafuWazonego as graf
import klasySymulator
import klasyDoswiadczenia
import time


def testujSymulacje():

    Doswiadczenie=klasyDoswiadczenia.doswiadczenie()


    Symulacja1=klasySymulator.symulator(Doswiadczenie)


    Symulacja1.testowanie()
    Symulacja1.RysujGraf()
    koszt=Symulacja1.x.obliczKosztRozwiazania()
    print koszt
    Symulacja1.RysujRozwiazania()
    raw_input()

    Symulacja1.ZnajdzRozwiazanie()
    Symulacja1.RysujGraf()


    print "UZYSKANY KOSZT WYNOSI:"
    print Symulacja1.KosztWynikowy

    print "KOSZT OPTYMALNY WYNOSI:"

    print Symulacja1.OptymalnyKoszt



if __name__ == '__main__':

    testujSymulacje()

    #print "KONIEC1"
    #print "KONIEC2"
