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
import klasyDoswiadczenia
import copy
from random import seed, gauss, uniform
import math
import itertools
import numpy as np
import matplotlib.pyplot as plt
import time




class symulator():



    def __init__(self,doswiadczenie):
        """
        Konstruktor Symulacji.
         * Bierze Rozwiazany graf wazony tworzy kopie i na niej operuje - usuwa krawedzie itd.
        """

        self.MojeDoswiadczenie=doswiadczenie


        self.x=doswiadczenie.stworzRozwiazanyGrafWazony()

        self.temperatura=self.MojeDoswiadczenie.temperaturaPoczatkowa

        self.k1= self.MojeDoswiadczenie.k1

    def testowanie(self):

        print "testowanie"


        print self.x.liczbaLewychWierzcholkow

    def NoweRozwiazanie(self):    
    
        print "NoweRozwiazanie"



    def ZamienKrawedz(self):



        koszt1 = self.x.obliczKosztRozwiazania()
        NrKrawedz1= int(uniform(0, self.x.liczbaLewychWierzcholkow))

        LewyWierzcholekKrawedz1=self.x.krawedzie[NrKrawedz1].numerWierzcholkaLewego


        PrawyWierzcholekKrawedz1=self.x.krawedzie[NrKrawedz1].numerWierzcholkaPrawego



        NrKrawedz2=int(uniform(0, self.x.liczbaLewychWierzcholkow))


        while(NrKrawedz2==NrKrawedz1):
            NrKrawedz2 = int(uniform(0, self.x.liczbaLewychWierzcholkow))






        LewyWierzcholekKrawedz2=self.x.krawedzie[NrKrawedz2].numerWierzcholkaLewego
        PrawyWierzcholekKrawedz2=self.x.krawedzie[NrKrawedz2].numerWierzcholkaPrawego


        self.x.krawedzie.remove(self.x.krawedzie[NrKrawedz1])


        if NrKrawedz2>NrKrawedz1:
            self.x.krawedzie.remove(self.x.krawedzie[NrKrawedz2-1])
        else:
            self.x.krawedzie.remove(self.x.krawedzie[NrKrawedz2])


        KrawedzDoDodania1=self.x.krawedzGrafuWazonego(LewyWierzcholekKrawedz1,PrawyWierzcholekKrawedz2)
        KrawedzDoDodania2=self.x.krawedzGrafuWazonego(LewyWierzcholekKrawedz2,PrawyWierzcholekKrawedz1)

        self.x.krawedzie.append(KrawedzDoDodania1)
        self.x.krawedzie.append(KrawedzDoDodania2)

        koszt2 = self.x.obliczKosztRozwiazania()



        if koszt2>koszt1:

            RzutMoneta=uniform(0,1)

            if self.temperatura>0.001:
                Prawdopodobienstwo=1/(1+(math.e)**((koszt2-koszt1)/(self.temperatura)))
            else:
                Prawdopodobienstwo=0



            self.PrzebiegPrawdopodobienstwa.append(Prawdopodobienstwo)

            if RzutMoneta>Prawdopodobienstwo:
                self.x.krawedzie.remove(KrawedzDoDodania1)
                self.x.krawedzie.remove(KrawedzDoDodania2)

                KrawedzStara1=self.x.krawedzGrafuWazonego(LewyWierzcholekKrawedz1,PrawyWierzcholekKrawedz1)
                KrawedzStara2=self.x.krawedzGrafuWazonego(LewyWierzcholekKrawedz2,PrawyWierzcholekKrawedz2)

                self.x.krawedzie.append(KrawedzStara1)

                self.x.krawedzie.append(KrawedzStara2)


        self.PrzebiegPrawdopodobienstwa.append(0)
    def AktualizujParametry(self):


        self.temperatura=self.MojeDoswiadczenie.ustalTemperature(self.temperatura)



    def RysujGraf(self):


        krawedzieLewePosortowane = sorted(self.x.krawedzie, key = lambda krawedz: krawedz.numerWierzcholkaLewego)
        print "Rozwiązanie to"
        for krawedz in krawedzieLewePosortowane:
            numerWierzcholkaLewego = krawedz.numerWierzcholkaLewego
            print str(krawedz.numerWierzcholkaLewego+1) + " --(" + str(self.x.podajWageKrawedzi(numerWierzcholkaLewego)) + \
                ")--> " + str(krawedz.numerWierzcholkaPrawego+1)

    def ZnajdzRozwiazanie(self):

        start = time.time()
        self.PrzebiegKosztu=[]

        self.PrzebiegKosztu.append(self.x.obliczKosztRozwiazania())

        self.IloscIteracji=0

        IteracjaJednorodny=1


        self.PrzebiegTemperatury =[]

        self.PrzebiegTemperatury.append(self.temperatura)

        self.PrzebiegPrawdopodobienstwa = []




        while(self.temperatura>self.MojeDoswiadczenie.temperaturaKoncowa):


            self.ZamienKrawedz()

            if IteracjaJednorodny%self.k1==0:

                self.AktualizujParametry()




            self.IloscIteracji=self.IloscIteracji+1

            IteracjaJednorodny=IteracjaJednorodny+1



            self.PrzebiegKosztu.append(self.x.obliczKosztRozwiazania())
            self.PrzebiegTemperatury.append(self.temperatura)

        end = time.time()
        self.CzasWykonania = end - start

        self.KosztWynikowy = self.PrzebiegKosztu[-1]


        #fig, ax2 = plt.subplots()
        #line1, = ax2.plot(range(len(self.PrzebiegKosztu)), self.PrzebiegKosztu, '--*')

        #ax2.legend(loc='lower right')
        #plt.show()

        if self.x.liczbaLewychWierzcholkow<10:
            self.RoznicaKosztu = self.KosztWynikowy-self.OptymalnyKoszt




    def RysujRozwiazania(self):


        if self.x.liczbaLewychWierzcholkow<10:

            stuff = range(self.x.liczbaLewychWierzcholkow)

            RozwiazaniePoczatkowe=[self.x.znajdzKrawedzLewyWierzcholek(q).numerWierzcholkaPrawego for q in range(len(stuff))]




            koszty=[]

            XX = list(itertools.permutations(stuff))
            OtoczenieKoszt = [[0 for x in range(2)] for y in range(len(XX))]
            WW=0
            for permutacja in XX:

                licznik=0


                KosztPermutacji=sum([self.x.wierzcholkiLewe[q].wagi[permutacja[q]] for q in range(len(stuff))])



                koszty.append(KosztPermutacji)

                for YY in range(len(permutacja)):
                    if RozwiazaniePoczatkowe[YY]!=permutacja[YY]:
                        licznik=licznik+1

                OtoczenieKoszt[WW][0]=licznik
                OtoczenieKoszt[WW][1]=KosztPermutacji
                WW=WW+1


            self.OptymalnyKoszt=min(koszty)



            a = [item[0] for item in OtoczenieKoszt]
            b = [item[1] for item in OtoczenieKoszt]


            #fig, ax = plt.subplots()
            #line1, = ax.plot(a,b,'*')

            #ax.legend(loc='lower right')


            #plt.show()
