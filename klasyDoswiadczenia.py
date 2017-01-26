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
import matplotlib.pyplot as plt
import numpy as np
from numpy import log
from operator import truediv

class doswiadczenie:

    """
    Zarządza przeprowadzanym doświadczeniem lub serią doświadczeń, komunikując się z blokami wykonawczymi. 
    Tworzy warstwę komunikacji z użytkownikiem programu. W kontekście problemu PB7 do jego obowiązków należy ―

    * proszenie o podanie nazwy pliku z kompletnym grafem ważonym,
    * ustalanie czy losowo generować graf, czy odczytać strukturę z pliku,
    * ustalanie parametrów symulowanego wyżarzania — temperaturę, ….
    * ustalanie rodzaju algorytmu schładzania, w tym schładzania jednorodnego i niejednorodnego,
    * ustalanie schematu schładzania,
    * ustalanie zakresu temperatury wyżarzania,
    * określanie rozmiaru grafu ważonego ― ilość wierzchołków lewego podgrafu, ilość wierzchołkow prawego podgrafu
    * określanie dopuszczalnego zakresu wag krawędzi grafu ważonego,

    """
    
    def __init__(self, temperaturaPoczatkowa = 300, temperaturaKoncowa = 0, wersja = "jednorodna"):
        """
        Konstruktor doświadczenia.
         * Ustala temperatury początkową i końcową.
         * Wybranie domyślnego schematu schładzania.
         * Ustala wersję algorytmu -- jednorodną lub niejednorodną.
         * Ustala domyślną ilość wierzchołków lewego i prawego podgrafu.
         * Ustala domyślny zakres wag grafu ważonego.
         * Ustala wartość parametru schematu schładzania "k2" na 1.
        """
        self.temperaturaPoczatkowa = temperaturaPoczatkowa
        self.temperaturaKoncowa = temperaturaKoncowa
        self.schematSchladzania = "Boltzmanna"
        self.wersjaAlgorytmu = wersja
        self.iloscWierzcholkowLewych = 10
        self.iloscWierzcholkowPrawych = 10
        self.zakresWag = [0, 10]
        self.k2 = 1
        
        self.parametryDoswiadczenia = {
            'temperaturaPoczatkowa': self.temperaturaPoczatkowa,
            'temperaturaKoncowa': self.temperaturaKoncowa,
            'schematSchladzania': self.schematSchladzania,
            'wersjaAlgorytmu': self.wersjaAlgorytmu,
            'iloscWierzcholkowLewych': self.iloscWierzcholkowLewych,
            'iloscWierzcholkowPrawych': self.iloscWierzcholkowPrawych,
            'zakresWag': self.zakresWag,
            }
        
    def _czyWczytacGrafZPliku(self):
        "Ustala, czy losowo generować graf, czy odczytać strukturę grafu ważonego z pliku."
        decyzja = str(raw_input("Czy wczytać strukturę grafu ważonego z pliku: "))
        if decyzja == "tak" or decyzja == "t":
            return True
        else:
            return False
    
    def T(self, schemat):
        """
        Zmienia obecną temperaturę zgodnie z wybranym schematem schładzania. Ustala parametry schematów schładzania.
        Akceptowane schematy schładzania to --
        1. Boltzmanna (Logarytmiczny),
        2. Cauchy'ego (Liniowy),
        3. Geometryczny.
        """
        print "Wybrany schemat schładzania to " + str(schemat)
        self.parametryDoswiadczenia['schematSchladzania'] = schemat
        if schemat == "Boltzmanna" or schemat == "Logarytmiczny":
            self.temperatura = self.temperaturaPoczatkowa * (1.0/log(self.k2))
            return self.temperatura
        elif schemat == "Cauchy'ego" or schemat == "Liniowy":
            self.temperatura = self.temperaturaPoczatkowa * (1.0/k2)
            return self.temperatura
        elif schemat == "Geometryczny":
            self.a = 0.5
            print "Ustawiam wartość parametru \"a\" na " + str(self.a)
            self.temperatura = self.temperaturaPoczatkowa * (self.a ** self.k2)
            return self.temperatura
        else:
            raise ValueError, "Nie ma takiego schematu schładzania " + str(schemat)
            return None

    def ustalenieGenerowanegoGrafu(self, iloscWierzcholkowLewych, iloscWierzcholkowPrawych, zakresWag):
        "Określa rozmiar grafu ważonego, określa dopuszczalny zakres wag krawędzi."
        self.iloscWierzcholkowLewych = int(iloscWierzcholkowLewych)
        self.iloscWierzcholkowPrawych = int(iloscWierzcholkowPrawych)
        if len(zakresWag) != 2:
            raise ValueError, "Niewłaściwy format wag " + str(zakresWag)
        elif type(zakresWag[0]) != int or type(zakresWag[1]) != int:
            raise ValueError, "Niewłaściwy format wag " + str(zakresWag)
        else:
            self.zakresWag = zakresWag
            
        self.parametryDoswiadczenia['iloscWierzcholkowLewych'] = self.iloscWierzcholkowLewych
        self.parametryDoswiadczenia['iloscWierzcholkowPrawych'] = self.iloscWierzcholkowPrawych
        self.parametryDoswiadczenia['zakresWag'] = self.zakresWag
    
    def stworzRozwiazanyGrafWazony(self):
        "Tworzy obiekt klasy rozwiazanyGrafWazony zgodnie z otrzymanymi danymi."
        liczbaWierzcholkow = self.iloscWierzcholkowLewych + self.iloscWierzcholkowPrawych
        decyzjaOWczytaniu = self._czyWczytacGrafZPliku()
        return graf.rozwiazanyGrafWazony(liczbaWierzcholkow, decyzjaOWczytaniu)
        
    def rozwiazProblem(self):
        "Rozwiązuje problem przydziału w grafie ważonym metodą symulowanego wyżarzania. Używa parametry doświadczenia z obiektu klasy ,,doswiadczenie''"
        # należy uzupełnić kodem wyołującym algorytm symulowanego wyżarzania
        
    def analizujWynikiAlgorytmu(self):
        "Analizuje wyniki rozwiązywania problemu przydziału w grafie ważonym za pomocą symulowanego wyżarzania."
        analiza = analizatorWynikow(self.parametryDoswiadczenia)
        analiza.analizuj()
        
class analizatorWynikow:

    """
    Umożliwia badanie i porównywanie rozwiązań problemu PB7 oraz badanie algorytmu symulowanego wyżarzania. 
    Wykonaną analizę przedstawia graficznie wizualizator wyników.

    * oblicza złożoność obliczeniową algorytmu symulowanego wyżarzania,
    * bada efektywność algorytmu w znajdowaniu optimum dla różnych zakresów parametru wyżarzania,
    * zapamiętuje rozwiązania uzyskane z algorytmu symulowanego wyżarzania,
    * zapamiętuje wyniki działania algorytmu symulowanego wyżarzania,
    * porównuje różne algorytmy schładzania,
    
    """
    
    def __init__(self, parametryDoswiadczenia):
        """
        Konstruktor Analizatora Wyników. Otrzymuje
         * parametryDoswiadczenia – słownik (dictionary) zawierający parametry doświadczenia
        """
        # Warto od razu pobrać dane doświadczenia od sterownika doświadczeniem – klasa doswiadczenie
        self.parametryDoswiadczenia = parametryDoswiadczenia
        self.temperaturaPoczatkowa = parametryDoswiadczenia['temperaturaPoczatkowa']
        self.temperaturaKoncowa = parametryDoswiadczenia['temperaturaKoncowa']
        self.iloscWierzcholkowLewych = parametryDoswiadczenia['iloscWierzcholkowLewych']
        self.iloscWierzcholkowPrawych = parametryDoswiadczenia['iloscWierzcholkowPrawych']
        self.zakresWag = parametryDoswiadczenia['zakresWag']
        
        self.daneDoswiadczenia = [] # lista słowników zawierających dane z kolejnego doświadczenia
        self.wyniki = []            # lista słowników zawierających wyniki analizy podanych doświadczeń
        
    def analizuj(self, daneZSymulatora):
        """
        Dokonuje analizy zastosowania symulowanego wyżarzania do rozwiązywania problemu przydziału w 
        grafie ważonym. 
        """
        # pobranie danych z symulatora
        self.dane.append(daneZSymulatora)
        
        # analiza danych
        wynikiAnalizy = {}
        wynikiAnalizy['efektywnoscAlgorytmu'] = self._badajEfektywnoscAlgorytmu(self.dane)
        wynikiAnalizy['zlozonosc'] = self._obliczZlozonoscObliczeniowa(self.dane)
        wynikiAnalizy['zlozonoscCzasowa'] = wynikiAnalizy['zlozonosc'][0]
        wynikiAnalizy['zlozonoscPamieciowa'] = wynikiAnalizy['zlozonosc'][1]
        wynikiAnalizy['porownanieSchematow'] = self._porownajSchematySchladzania(self.dane)
        
        # zapisanie wyników danych
        self.wyniki.append(wynikiAnalizy)
        
        # graficzna reprezentacja analizy
        self.wizualizatorWynikow(self.dane[0],"Rozw")    # ,,dane'' przesłane w dowolnej formie, dostosuj kod klasy wizualizatorWynikow
        self.wizualizatorWynikow(wynikiAnalizy)          # ,,dane'' przesłane w dowolnej formie, dostosuj kod klasy wizualizatorWynikow
        #self._przedstawGraficznie(self.wyniki)
        
    def _badajEfektywnoscAlgorytmu(self, daneZDoswiadczen):
        """
        Zbadanie efektywności algorytmu w znajdowaniu optimum dla różnych zakresów parametru wyżarzania i różnych temperatur.
        Potrzebuje:
         * oceny optymalnych rozwiązań dla różnych zakresów parametru wyżarzania,
         * ilość iteracji algorytmu potrzebna do osiągnięcia optymalnego rozwiązania dla przebadanych
           wartości zakresu temperatur przeprowadzonego algorytmu,
         * wartości parametru wyżarzania, dla których obliczone były funkcje oceny
        Zwraca wiązkę o postaci
        ( efektywnoscTemperaturowa, efektywnoscParametryczna ), co się przekłada na
        ( (średnia ocena na T, T) , (średnia ocena na parametr wyżarzania, parametr) )
        ( ([f1,f2,...],[T1,T2,...] , ([f1,f2,...],[a1,a2,...]) )
        """
        # uporządkowanie danych
        fEmin = []; iteracje = []; T = []; a = []
        for daneDoswiadczenia in daneZDoswiadczen:
            fEmin.append(daneDoswiadczenia['fEmin'])
            iteracje.append(daneDoswiadczenia['iteracje'])
            a.append(daneDoswiadczenia['a'])
            T.append(daneDoswiadczenia['Tmax'])
        
        # obliczenie efektywności
        fEminNaT = map(truediv, fEmin, T)
        fEminNaA = map(truediv, fEmin, a)
        
        efektywnoscTemperaturowa = (fEminNaT, T)
        efektywnoscParametryczna = (fEminNaA, a)
        
        # zwrócenie wartości    
        efektywnoscAlgorytmu = (efektywnoscTemperaturowa, efektywnoscParametryczna)
        return efektywnoscAlgorytmu       
        
    def _obliczZlozonoscObliczeniowa(self, daneZDoswiadczen):
        """
        Oblicza złozonosc obliczeniową algorytmu symulowanego wyżarzania.
        Potrzebuje:
         * ilość iteracji algorytmu symulowanego wyżarzania potrzebna do osiągnięcia
           optymalnego rozwiązania,
         * ilość czasu wykonywania algorytmu symulowanego wyżarzania,
         * ilość rozwiązań pośrednich przed uzyskaniem rozwiązania optymalnego.
        Obliczana jest złożoność czasowa i pamięciowa algorytmu.
        Zwraca wiązkę o postaci
        ( (złożoność czasowa), (złożoność pamięciowa) ), co się przekłada na
        ( ([t1,t2,...], [it1,it2,...]), ([pos1,pos2,...],[it1,it2,...]) )
        """
        # uporządkowanie danych
        iteracje = []; t = []; iloscPosrednich = []
        for daneDoswiadczenia in daneZDoswiadczen:
            iteracje.append(daneDoswiadczenia['iteracje'])
            t.append(daneDoswiadczenia['t'])
            iloscPosrednich.append(daneDoswiadczenia['iloscPosrednich'])
            
        # obliczenie złożoności
        czasNaIteracje = map(truediv, t, iteracje)
        rozwiazaniaNaIteracje = map(truediv, iloscPosrednich, iteracje)
        
        # zwrócenie złożoności
        zlozonoscCzasowa = (czasNaIteracje, iteracje)
        zlozonoscPamieciowa = (rozwiazaniaNaIteracje, iteracje)
        zlozonosc = (zlozonoscCzasowa, zlozonoscPamieciowa)
        return zlozonosc
        
#    def _zapamietajRozwiazanie(self, daneZDoswiadczenia):
#        "Zapamiętuje rozwiązanie i koszty uzyskania rozwiązania z algorytmu symulowanego wyżarzania."
        
        
    def _porownajSchematySchladzania(self, daneZDoswiadczen):
        """
        Porównuje zastosowane schematy schładzania.
        Zwraca wiązkę o postaci:
        (
         [fE min. średnie Boltzmann, fE min. Liniowy, fE min. Geometryczny],
         [średnie iteracje Boltzmann, ś. iteracje Liniowy, ś. iteracje Geometryczny],
         [ilość schematów Boltzmanna, # Liniowych, # Geometrycznych]
        )
        """
        # uporządkowanie danych
        schematy = [0,0,0]; fEmin = [0,0,0]; iteracje = [0,0,0]; 
        for daneDoswiadczenia in daneZDoswiadczen:
            schemat = daneDoswiadczenia['schemat']
            ktory = 0 if schemat == 'Boltzmanna' or schemat == 'Logarytmiczny' else -1
            ktory = 1 if schemat == "Cauchy'ego" or schemat == 'Liniowy' else -1
            ktory = 2 if schemat == 'Geometryczny' else -1
            if ktory == -1:
                raise ValueError, "Podana niepoprawna nazwa schematu schładzania – " + str(schemat)
            schematy[ktory] += 1
            fEmin[ktory] += daneDoswiadczenia['fEmin']
            iteracje[ktory] += daneDoswiadczenia['iteracje']
        
        # obliczenie wartości miarodajnych
        fEminAvg = map(truediv, fEmin, schematy)
        iteracjeAvg = map(truediv, iteracje, schematy)
        porownanie = (fEminAvg, iteracjeAvg, schematy)
        
        return porownanie
        
    def _przedstawGraficznie(self, dane):
        "Przedstawienie graficzne wyników analizy."
        self.wizualizatorWynikow(dane,"Rozw")   # ,,dane'' przesłane w dowolnej formie, dostosuj kod klasy wizualizatorWynikow
        self.wizualizatorWynikow(dane)          # ,,dane'' przesłane w dowolnej formie, dostosuj kod klasy wizualizatorWynikow
        
        
    class wizualizatorWynikow:
    
        """
        Nakładka na analizatora wyników, która umożliwia przedstawienie graficznie wyników
        działania algorytmu symulowanego wyżarzania i uzyskanych z jego pomocą rozwiązań problemu PB7.

        * przedstawia graficznie proces dochodzenia algorytmu do rozwiązania,
        * tworzy wykresy złożoności obliczeniowej algorytmu w zależności od jego parametrów.
        
        """
    
        def __init__(self, dane, wykresy=None):
            """
            Konstruktor Wizualizatora Wyników. Przyjmuję, że domyślnie wszystkie wykresy analityczne są rysowane.
            Wykresy powinny być przekazane w formie wiązki (tuple). Dostępne wykresy to
             * O(n) -- wykres złożoności obliczeniowej algorytmu symulowanego wyżarzania w zależności od jego parametrów,
             * E(T) -- wykres efektywności algorytmu w znajdowaniu optimum dla różnych zakresów parametru temperatury wyżarzania.
             * A(J,NJ) -- graficzne porównanie algorytmów schładzania – jednorodnego (J) i niejednorodnego (NJ).
             * Sch -- graficzna analiza różnych sposobów aktualizacji temperatury (schematów schładzania).
             * Rozw -- wizualizacja przebiegu dochodzenia algorytmu do rozwiązania.
            Dane potrzebne do rysowania wykresów:
             * ilość
            """
            self.wykresy = wykresy
            self.dane = dane
            
            if self.wykresy == None:
                plt.figure(); _rysujWykresZlozonosciObliczeniowej()
                plt.figure(); _rysujWykresT()
                # plt.figure(); _rysujPorownanieAlgorytmow()
                plt.figure(); _rysujPorownanieSchematowSchladzania()
            if "O(n)" in self.wykresy:
                plt.figure(); _rysujWykresZlozonosciObliczeniowej()
            if "E(T)" in self.wykresy:
                plt.figure(); _rysujWykresT()
            if "A(J,NJ)" in self.wykresy:
                plt.figure(); _rysujPorownanieAlgorytmow()
            if "Sch" in self.wykresy:
                plt.figure(); _rysujPorownanieSchematowSchladzania()
            if "Rozw" in self.wykresy:
                plt.figure(); _rysujDochodzenieDoRozwiazania()
                
            show()
            
        def _rysujWykresZlozonosciObliczeniowej(self):
            "Rysuje wykres złożoności obliczeniowej O(n) algorytmu symulowanego wyżarzania w zależności od jego parametrów."
            # Przyjąłem format danych: 
            # ( (złożoność czasowa), (złożoność pamięciowa) ), co się przekłada na
            # ( ([t1,t2,...], [it1,it2,...]), ([pos1,pos2,...],[it1,it2,...]) )
            zlozonoscCzasowa = self.dane['zlozonoscCzasowa']
            zlozonoscPamieciowa = self.dane['zlozonoscPamieciowa']
            
            nt = np.asarray(zlozonoscCzasowa[0][1])
            Ot = np.asarray(zlozonoscCzasowa[0][0])
            
            nm = np.asarray(zlozonoscPamieciowa[1][1])
            Om = np.asarray(zlozonoscPamieciowa[1][0])
            
            plt.title('Złożoność obliczeniowa O(n)')
            plt.subplot(211)
            plt.plot(nt,Ot)                    # rysowanie wykresu 
            plt.ylabel('Średni czas na iterację.')
            plt.xlabel('Ilość iteracji')
            
            plt.subplot(221)
            plt.plot(nm,Om)
            plt.ylabel('Średnia ilość rozwiązań na iterację.')
            plt.xlabel('Ilość iteracji')
            
        def _rysujWykresT(self):
            "Rysuje wykres efektywności algorytmu E(T) w znajdowaniu optimum dla różnych zakresów parametru temperatury wyżarzania."
            # Przyjąłem dane w formacie
            # ( efektywnoscTemperaturowa, efektywnoscParametryczna ), co się przekłada na
            # ( (średnia ocena na T, T) , (średnia ocena na parametr wyżarzania, parametr) )
            # ( ([f1,f2,...],[T1,T2,...] , ([f1,f2,...],[a1,a2,...]) )
            efektywnoscParametryczna = self.dane['efektywnoscAlgorytmu'][1]
            
            a = np.asarray(efektywnoscParametryczna[1])    # zamiana na typ array, oś OX
            fE = np.asarray(efektywnoscParametryczna[0])   # zamiana na typ array, oś OY
            
            plt.plot(a,fE)       # rysowanie wykresu
            
            plt.title('Efektywność algorytmu w zależności od parametru wyżarzania')
            plt.ylabel('Średnia ocena na parametr')
            plt.xlabel('Parametr wyżarzania')
                      
        def _rysujPorownanieAlgorytmow(self):
            "Przedstawia graficznie porównanie algorytmów schładzania – jednorodnego (J) i niejednorodnego (NJ)."
            J = self.dane['nazwaKlucza']    # wstawić dane o efektywności algorytmu jednorodnego z pola struktury ,,dane''
            NJ = self.dane['nazwaKlucza']   # wstawić dane o efektywności algorytmu niejednorodnego z pola struktury ,,dane''
            
            ind = (0,1)              # indeksy algorytmów, 0 – jednorodny, 1 – niejednorodny
            Y = (J,NJ)               # oś OY
            
            plt.bar(ind,Y)
            
            plt.title('Schładzanie jednorodne (J) i niejednorodne (NJ)')
            plt.ylabel('Efektywność')
            plt.xticks(ind, ('jednorodne','niejednorodne'))
            
        def _rysujPorownanieSchematowSchladzania(self):
            "Przedstawia graficznie analizę różnych sposobów aktualizacji temperatury (schematów schładzania)."
            # Przyjąłem dane w formacie
            #(
            # [fE min. średnie Boltzmann, fE min. Liniowy, fE min. Geometryczny],
            # [średnie iteracje Boltzmann, ś. iteracje Liniowy, ś. iteracje Geometryczny],
            # [ilość schematów Boltzmanna, # Liniowych, # Geometrycznych]
            #)
            porownanie = self.dane['porownanieSchematow']
            fE = porownanie[0]
            it = porownanie[1]
            N = porownanie[2]
            ind = range(3)
            
            plt.title('Efektywność schematów schładzania')
            subplot(311)
            plt.bar(ind,fE)
            plt.ylabel('Średnia ocena na ilość zastosowanych schematów')
            plt.xticks(ind, ('Boltzmanna', 'Liniowy', 'Geometryczny'))
            
            subplot(312)
            plt.bar(ind,it)
            plt.ylabel('Średnia ilość iteracji na ilość zastosowanych schematów')
            plt.xticks(ind, ('Boltzmanna', 'Liniowy', 'Geometryczny'))
            
            subplot(313)
            plt.bar(ind,N)
            plt.ylabel('Ilość zastosowanych schematów')
            plt.xticks(ind, ('Boltzmanna', 'Liniowy', 'Geometryczny'))
            
        def _rysujDochodzenieDoRozwiazania(self):
            "Wizualizacja przebiegu dochodzenia algorytmu do rozwiązania."
            # Przyjąłem dane jako słownik zawierający wiązkę z liczbą iteracji 
            # i funkcją oceny dla poszczególnych iteracji algorytmu
            iloscIteracji = self.dane['iteracje']    # wstawić ilość iteracji wykonanych przez algorytm
            fE = self.dane['fE']                     # wstawić funkcję oceny rozwiązania ze struktury ,,dane''
            
            x = np.arange(iloscIteracji)    # oś OX
            y = np.asarray(fE)              # oś OY
            
            plt.plot(x,y)                   # rysowanie wykresu
            
            plt.title('Dochodzenie algorytmu do rozwiązania')
            plt.ylabel('Funkcja oceny')
            plt.xlabel('Iteracja')
        
    
    
