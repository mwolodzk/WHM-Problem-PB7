#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Testuje poprawność struktury danych rozwiązanego problemu przydziału w grafie ważonym.
"""

import klasyGrafuWazonego as graf
import klasySymulator
import klasyDoswiadczenia
import time
import matplotlib.pyplot as plt

def testujSymulacje():


#######################################################
#


    Doswiadczenie1 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=500, temperaturaKoncowa=0.01,
                                                         schematSchladzania="Logarytmiczny", wersja="jednorodna",
                                                         decyzja="nie", iloscWierzcholkowLewych=9, k1=1,a=0.5)

    Symulacja1 = klasySymulator.symulator(Doswiadczenie1)

    Symulacja1.RysujRozwiazania()
    Symulacja1.ZnajdzRozwiazanie()


    Doswiadczenie2 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=500, temperaturaKoncowa=0.01,
                                                 schematSchladzania="Liniowy", wersja="jednorodna",
                                                 decyzja="nie", iloscWierzcholkowLewych=9, k1=1, a=0.5)

    Symulacja2 = klasySymulator.symulator(Doswiadczenie2)

    Symulacja2.RysujRozwiazania()
    Symulacja2.ZnajdzRozwiazanie()


    Doswiadczenie3 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=500, temperaturaKoncowa=0.01,
                                                  schematSchladzania="Geometryczny", wersja="jednorodna",
                                                  decyzja="nie", iloscWierzcholkowLewych=9, k1=1, a=0.5)

    Symulacja3 = klasySymulator.symulator(Doswiadczenie3)

    Symulacja3.RysujRozwiazania()
    Symulacja3.ZnajdzRozwiazanie()



    fig1 = plt.figure(1)

    plt.plot(range(len(Symulacja1.PrzebiegKosztu)),Symulacja1.PrzebiegKosztu,'b',label="Logarytmiczny")
    plt.plot(range(len(Symulacja2.PrzebiegKosztu)),Symulacja2.PrzebiegKosztu,'r',label="Liniowy")
    plt.plot(range(len(Symulacja3.PrzebiegKosztu)),Symulacja3.PrzebiegKosztu,'g',label="Geometryczny")
    plt.legend()

    plt.ylabel("Wartosc funkcji kosztu")
    plt.xlabel("Iteracja")

    plt.savefig('foo1_1.png')


    fig1 = plt.figure(2)

    plt.plot(range(len(Symulacja1.PrzebiegTemperatury)), Symulacja1.PrzebiegTemperatury, 'b', label="Logarytmiczny")
    plt.plot(range(len(Symulacja2.PrzebiegTemperatury)), Symulacja2.PrzebiegTemperatury, 'r', label="Liniowy")
    plt.plot(range(len(Symulacja3.PrzebiegTemperatury)), Symulacja3.PrzebiegTemperatury, 'g', label="Geometryczny")
    plt.legend()

    plt.ylabel("Temperatura")
    plt.xlabel("Iteracja")

    plt.savefig('foo1_2.png')

    fig1 = plt.figure(3)

    plt.plot(range(len(Symulacja1.PrzebiegPrawdopodobienstwa)), Symulacja1.PrzebiegPrawdopodobienstwa, 'b', label="Logarytmiczny")
    plt.plot(range(len(Symulacja2.PrzebiegPrawdopodobienstwa)), Symulacja2.PrzebiegPrawdopodobienstwa, 'r', label="Liniowy")
    plt.plot(range(len(Symulacja3.PrzebiegPrawdopodobienstwa)), Symulacja3.PrzebiegPrawdopodobienstwa, 'g', label="Geometryczny")
    plt.legend()

    plt.ylabel("Prawdopodobienstwo")
    plt.xlabel("Iteracja")

    plt.savefig('foo1_3.png')







#######################################################
#

    Doswiadczenie1 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=500, temperaturaKoncowa=0.01,
                                                      schematSchladzania="Logarytmiczny", wersja="jednorodna",
                                                      decyzja="nie", iloscWierzcholkowLewych=9, k1=8, a=0.5)

    Symulacja1 = klasySymulator.symulator(Doswiadczenie1)

    Symulacja1.RysujRozwiazania()
    Symulacja1.ZnajdzRozwiazanie()

    Doswiadczenie2 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=500, temperaturaKoncowa=0.01,
                                                      schematSchladzania="Liniowy", wersja="jednorodna",
                                                      decyzja="nie", iloscWierzcholkowLewych=9, k1=8, a=0.5)

    Symulacja2 = klasySymulator.symulator(Doswiadczenie2)

    Symulacja2.RysujRozwiazania()
    Symulacja2.ZnajdzRozwiazanie()

    Doswiadczenie3 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=500, temperaturaKoncowa=0.01,
                                                      schematSchladzania="Geometryczny", wersja="jednorodna",
                                                      decyzja="nie", iloscWierzcholkowLewych=9, k1=8, a=0.5)

    Symulacja3 = klasySymulator.symulator(Doswiadczenie3)

    Symulacja3.RysujRozwiazania()
    Symulacja3.ZnajdzRozwiazanie()

    fig1 = plt.figure(4)

    plt.plot(range(len(Symulacja1.PrzebiegKosztu)), Symulacja1.PrzebiegKosztu, 'b', label="Logarytmiczny")
    plt.plot(range(len(Symulacja2.PrzebiegKosztu)), Symulacja2.PrzebiegKosztu, 'r', label="Liniowy")
    plt.plot(range(len(Symulacja3.PrzebiegKosztu)), Symulacja3.PrzebiegKosztu, 'g', label="Geometryczny")
    plt.legend()

    plt.ylabel("Wartosc funkcji kosztu")
    plt.xlabel("Iteracja")

    plt.savefig('foo2_1.png')

    fig1 = plt.figure(5)

    plt.plot(range(len(Symulacja1.PrzebiegTemperatury)), Symulacja1.PrzebiegTemperatury, 'b', label="Logarytmiczny")
    plt.plot(range(len(Symulacja2.PrzebiegTemperatury)), Symulacja2.PrzebiegTemperatury, 'r', label="Liniowy")
    plt.plot(range(len(Symulacja3.PrzebiegTemperatury)), Symulacja3.PrzebiegTemperatury, 'g', label="Geometryczny")
    plt.legend()

    plt.ylabel("Temperatura")
    plt.xlabel("Iteracja")

    plt.savefig('foo2_2.png')

    fig1 = plt.figure(6)

    plt.plot(range(len(Symulacja1.PrzebiegPrawdopodobienstwa)), Symulacja1.PrzebiegPrawdopodobienstwa, 'b',
             label="Logarytmiczny")
    plt.plot(range(len(Symulacja2.PrzebiegPrawdopodobienstwa)), Symulacja2.PrzebiegPrawdopodobienstwa, 'r', label="Liniowy")
    plt.plot(range(len(Symulacja3.PrzebiegPrawdopodobienstwa)), Symulacja3.PrzebiegPrawdopodobienstwa, 'g',
             label="Geometryczny")
    plt.legend()

    plt.ylabel("Prawdopodobienstwo")
    plt.xlabel("Iteracja")

    plt.savefig('foo2_3.png')





#####################################################3
#



    lista1 = []
    x = 0


    for k in range(50, 50000, 100):
        Doswiadczenie = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=k, temperaturaKoncowa=0.01,
                                                     schematSchladzania="Logarytmiczny", wersja="jednorodna",
                                                     decyzja="nie", iloscWierzcholkowLewych=20, k1=1, a=0.5)

        Symulacja1 = klasySymulator.symulator(Doswiadczenie)
        Symulacja1.RysujRozwiazania()
        Symulacja1.ZnajdzRozwiazanie()

        lista1.append(Symulacja1.KosztWynikowy)



    fig1 = plt.figure(7)

    plt.plot(range(50, 50000, 100), lista1, 'b',
             label="Logarytmiczny")

    plt.legend()

    plt.ylabel("Wartosc funkcji kosztu")
    plt.xlabel("Temperatura poczatkowa")

    plt.savefig('foo3_1.png')


    lista2 = []
    x = 0

    for k in range(1, 1000, 10):
        Doswiadczenie = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=k/500,
                                                         schematSchladzania="Logarytmiczny", wersja="jednorodna",
                                                         decyzja="nie", iloscWierzcholkowLewych=20, k1=1, a=0.5)

        Symulacja1 = klasySymulator.symulator(Doswiadczenie)
        Symulacja1.RysujRozwiazania()
        Symulacja1.ZnajdzRozwiazanie()

        lista2.append(Symulacja1.KosztWynikowy)

    fig1 = plt.figure(8)

    plt.plot([xx / 500.0 for xx in range(1, 1000, 10)], lista2, 'b*',
             label="Logarytmiczny")

    plt.legend()

    plt.ylabel("Wartosc funkcji kosztu")
    plt.xlabel("Temperatura koncowa")

    plt.savefig('foo3_2.png')


#####################################################3
#

    lista3 = []
    lista4 = []
    lista5 = []


    lista6 = []
    lista7 = []
    lista8 = []


    lista9 = []
    lista10 = []
    lista11 = []




    x = 0

    for k in range(1, 100, 1):
        Doswiadczenie1 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=0.01,
                                                         schematSchladzania="Logarytmiczny", wersja="jednorodna",
                                                         decyzja="nie", iloscWierzcholkowLewych=20, k1=k, a=0.5)

        Symulacja1 = klasySymulator.symulator(Doswiadczenie1)
        Symulacja1.RysujRozwiazania()
        Symulacja1.ZnajdzRozwiazanie()

        lista3.append(Symulacja1.KosztWynikowy)
        lista6.append(Symulacja1.IloscIteracji)
        lista9.append(Symulacja1.CzasWykonania)



        Doswiadczenie2 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=0.01,
                                                         schematSchladzania="Liniowy", wersja="jednorodna",
                                                         decyzja="nie", iloscWierzcholkowLewych=20, k1=k, a=0.9)

        Symulacja2 = klasySymulator.symulator(Doswiadczenie2)
        Symulacja2.RysujRozwiazania()
        Symulacja2.ZnajdzRozwiazanie()



        lista4.append(Symulacja2.KosztWynikowy)
        lista7.append(Symulacja2.IloscIteracji)
        lista10.append(Symulacja2.CzasWykonania)



        Doswiadczenie3 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=0.01,
                                                         schematSchladzania="Geometryczny", wersja="jednorodna",
                                                         decyzja="nie", iloscWierzcholkowLewych=20, k1=k, a=0.5)

        Symulacja3 = klasySymulator.symulator(Doswiadczenie3)
        Symulacja3.RysujRozwiazania()
        Symulacja3.ZnajdzRozwiazanie()

        lista5.append(Symulacja3.KosztWynikowy)
        lista8.append(Symulacja3.IloscIteracji)
        lista11.append(Symulacja3.CzasWykonania)



    fig1 = plt.figure(9)

    plt.plot(range(1, 100, 1), lista3, 'b',
             label="Logarytmiczny")


    plt.plot(range(1, 100, 1), lista4, 'r',
             label="Liniowy")

    plt.plot(range(1, 100, 1), lista5, 'g',
             label="Geometryczny")



    plt.legend()

    plt.ylabel("Wartosc funkcji kosztu")
    plt.xlabel("Parametr k1 - co ile iteracji aktualizujemy Temperature")

    plt.savefig('foo3_3.png')


    fig1 = plt.figure(10)

    plt.plot(range(1, 100, 1), lista6, '*b',
             label="Logarytmiczny")

    plt.plot(range(1, 100, 1), lista7, '-r',
             label="Liniowy")

    plt.plot(range(1, 100, 1), lista8, '+g',
             label="Geometryczny")

    plt.legend()

    plt.ylabel("Ilosc iteracji")
    plt.xlabel("Parametr k1 - co ile iteracji aktualizujemy Temperature")

    plt.savefig('foo3_4.png')


    fig1 = plt.figure(11)

    plt.plot(range(1, 100, 1), lista9, '*b',
             label="Logarytmiczny")

    plt.plot(range(1, 100, 1), lista10, '-r',
             label="Liniowy")

    plt.plot(range(1, 100, 1), lista11, '+g',
             label="Geometryczny")

    plt.legend()

    plt.ylabel("Czas trwania algorytmu")
    plt.xlabel("Parametr k1 - co ile iteracji aktualizujemy Temperature")

    plt.savefig('foo3_5.png')





###################################################


    lista12 = []
    lista13 = []
    lista14 = []

    x = 0


    Doswiadczenie1 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=0.01,
                                                      schematSchladzania="Logarytmiczny", wersja="jednorodna",
                                                      decyzja="nie", iloscWierzcholkowLewych=9, k1=k, a=0.5)

    Symulacjaa = klasySymulator.symulator(Doswiadczenie1)
    Symulacjaa.RysujRozwiazania()



    for k in range(1, 100, 1):
        Doswiadczenie1 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=0.01,
                                                          schematSchladzania="Logarytmiczny", wersja="jednorodna",
                                                          decyzja="nie", iloscWierzcholkowLewych=9, k1=k, a=0.5)


        Symulacja1 = klasySymulator.symulator(Doswiadczenie1)
        Symulacja1.OptymalnyKoszt=Symulacjaa.OptymalnyKoszt
        Symulacja1.ZnajdzRozwiazanie()


        lista12.append((Symulacja1.KosztWynikowy-Symulacjaa.OptymalnyKoszt))

        Doswiadczenie2 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=0.01,
                                                          schematSchladzania="Liniowy", wersja="jednorodna",
                                                          decyzja="nie", iloscWierzcholkowLewych=9, k1=k, a=0.9)

        Symulacja2 = klasySymulator.symulator(Doswiadczenie2)
        Symulacja2.OptymalnyKoszt = Symulacjaa.OptymalnyKoszt
        Symulacja2.ZnajdzRozwiazanie()

        lista13.append((Symulacja2.KosztWynikowy-Symulacjaa.OptymalnyKoszt))

        Doswiadczenie3 = klasyDoswiadczenia.doswiadczenie(temperaturaPoczatkowa=3000, temperaturaKoncowa=0.01,
                                                          schematSchladzania="Geometryczny", wersja="jednorodna",
                                                          decyzja="nie", iloscWierzcholkowLewych=9, k1=k, a=0.5)

        Symulacja3 = klasySymulator.symulator(Doswiadczenie3)
        Symulacja3.OptymalnyKoszt = Symulacjaa.OptymalnyKoszt
        Symulacja3.ZnajdzRozwiazanie()


        lista14.append((Symulacja3.KosztWynikowy-Symulacjaa.OptymalnyKoszt))





    fig1 = plt.figure(12)

    plt.plot(range(1, 100, 1), lista12, '*b',
             label="Logarytmiczny")

    plt.plot(range(1, 100, 1), lista13, '-r',
             label="Liniowy")

    plt.plot(range(1, 100, 1), lista14, '+g',
             label="Geometryczny")

    plt.legend()

    plt.ylabel("Roznica Wyniku od Optimum")
    plt.xlabel("Parametr k - co ile iteracji aktualizujemy Temperature")

    plt.savefig('foo3_6.png')

if __name__ == '__main__':

    testujSymulacje()

    print "KONIEC2"
