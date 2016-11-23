using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projektowanie_sieci
{

    class Program
    {


        static void Main()
        {

            Projektuj _projektuj = new Projektuj();

            Console.WriteLine("Podaj pliki wejsciowe oddzielone spacja :");


            string b = Console.ReadLine();
            string[] tabodczyt1 = b.Split(' ');

            Console.WriteLine("Podaj odpowiadajace pliki wyjsciowe oddzielone spacja: ");
            string wyjscie = Console.ReadLine();
            string[] tabodczyt2 = wyjscie.Split(' ');

            int i = 0;

            // Dla każdej pary plik wejsciowy, plik wyjsciowy przeprowadzamy projektowanie

            for (; i < tabodczyt1.GetLength(0); i++)
            {

                _projektuj.projektujaca(tabodczyt1[i], tabodczyt2[i]);
            }




        }
    }

    class Projektuj
    {

        public void projektujaca(string _wejscie, string _wyjscie)
        {


            // Wczytujemy dane z pliku wejsciowego do Sieci(obiekt grafik)

            string wejscie = _wejscie;



            FileStream plik;
            string odczyt;
            plik = new FileStream(wejscie, FileMode.Open);
            StreamReader p = new StreamReader(plik);
            p.ReadLine();
            odczyt = p.ReadLine();
            string[] tabodczyt = odczyt.Split(' ');
            int _liczbawezlow = int.Parse(tabodczyt[2]);
            p.ReadLine();
            odczyt = p.ReadLine();
            tabodczyt = odczyt.Split(' ');
            int _liczbalaczy = int.Parse(tabodczyt[2]);
            p.ReadLine();

            Siec grafik = new Siec(_liczbalaczy, _liczbawezlow);
            int i = 0;
            for (; i < _liczbawezlow; i++)
            {

                grafik.zbior_wezlow[i] = new Wezel(i + 1);


            }

            odczyt = p.ReadLine();
            tabodczyt = odczyt.Split(' ');



            string decimalCharacter = System.Globalization.CultureInfo.InstalledUICulture.NumberFormat.NumberDecimalSeparator;



            int j = 0;
            while (tabodczyt[0]!= null && tabodczyt[0] != "")
            {

                grafik.zbior_laczy[j] = new Lacze(int.Parse(tabodczyt[0]), grafik.zbior_wezlow[int.Parse(tabodczyt[1]) - 1], grafik.zbior_wezlow[int.Parse(tabodczyt[2]) - 1], double.Parse(tabodczyt[3].Replace(".", decimalCharacter)), double.Parse(tabodczyt[4].Replace(".", decimalCharacter)));

                ++j;

                odczyt = p.ReadLine();
                if (odczyt != null)
                    tabodczyt = odczyt.Split(' ');
                else
                    break;


            }

            p.ReadLine();
            odczyt = p.ReadLine();
            tabodczyt = odczyt.Split(' ');
            int ile_zapotrzebowan = int.Parse(tabodczyt[2]);
            p.ReadLine();


            //wczytujemy zapotrzebowania


            zapotrzebowanie[] tabzapotrzebowan = new zapotrzebowanie[ile_zapotrzebowan];
            grafik.liczba_zapotrzebowan = ile_zapotrzebowan;
            j = 0;

            odczyt = p.ReadLine();
            tabodczyt = odczyt.Split(' ');


            while (tabodczyt[0] != null && tabodczyt[0] != "")
            {

                tabzapotrzebowan[j] = new zapotrzebowanie(int.Parse(tabodczyt[0]), grafik.zbior_wezlow[int.Parse(tabodczyt[1]) - 1], grafik.zbior_wezlow[int.Parse(tabodczyt[2]) - 1], double.Parse(tabodczyt[3].Replace(".", decimalCharacter)));

                odczyt = p.ReadLine();
                if (odczyt != null)
                    tabodczyt = odczyt.Split(' ');
                else
                    break;
                j++;



            }


            plik.Close();
            p.Close();

            // Koniec wczytywania



            // tworzymy Liste sciezek w grafie oraz Sciezki wraz z przeplywami ktore reazlizuja zapotrzebowanie 
            // (pierwszej sciezce(id) odpowiada pierwszy element na liście przepływów 
            grafik.wszystkie_sciezki = new List<Sciezka>();



            int v = 0;

            for (; v < grafik.liczba_zapotrzebowan; v++)
            {


                tabzapotrzebowan[v].id_sciezek = new List<int>();
                tabzapotrzebowan[v].przeplywy = new List<double>();


            }


            v = 0;



            //         Tutaj zaczynamy szukać ścieżek powiększających
            //         Dla każdego zapotrzebowania szukamy 200 razy sciezek powiekszajacyh, przerywamy gdy nie znajdujemy jej już lub gdy 
            //         zrealizowalismy zapotrzebowanie



            for (; v < grafik.liczba_zapotrzebowan; v++)
            {


                int x = 0;




                for (; x < 200; x++)
                {

                    //      wyznaczam przepustowości resisualne na laczach Sieci


                    i = 0;
                    for (; i < grafik.liczba_laczy; i++)
                    {

                        grafik.zbior_laczy[i].przepustowosc_resztkowa = grafik.zbior_laczy[i].przepustowosc - grafik.zbior_laczy[i].przeplyw;

                    }


                    poprawiania_etykiet znajdz_sciezke = new poprawiania_etykiet();



                    Sciezka sciezka_powiekszajaca = new Sciezka();
                    sciezka_powiekszajaca.id_lacz = new List<int>();


                    // Korzystajac z algorytmu poprawiania etykiet szukam najkrotszych sciezek(pod wzgledem specjalnej wagi)

                    sciezka_powiekszajaca.id_lacz = znajdz_sciezke.najkrotsza(tabzapotrzebowan[v].zrodlo.id, grafik, tabzapotrzebowan[v].ujscie.id);


                    if (sciezka_powiekszajaca.id_lacz.Count == 0)
                    {

                        break;



                    }

                    //wyznaczamy grubosc sciezki powiekszajacej

                    i = 0;
                    double min = 10000;
                    for (; i < sciezka_powiekszajaca.id_lacz.Count; i++)
                    {

                        if (grafik.zbior_laczy[sciezka_powiekszajaca.id_lacz[i] - 1].przepustowosc_resztkowa < min)
                        {

                            min = grafik.zbior_laczy[sciezka_powiekszajaca.id_lacz[i] - 1].przepustowosc_resztkowa;


                        }


                    }

                    // realizujemy tylko 1% grubosci sciezki by uchronic sie przed zapychaniem lacz 



                    min = 0.01 * min;



                    if (tabzapotrzebowan[v].rozmiar - tabzapotrzebowan[v].zrealizowano < min)
                    {

                        min = tabzapotrzebowan[v].rozmiar - tabzapotrzebowan[v].zrealizowano;


                    }

                    // znalezlismy sciezke powiekszajaca. Teraz trzeba uaktualnic przeplywy. Cofamy sie po sciezce i dodajemy przeplyw

                    i = 0;
                    for (; i < sciezka_powiekszajaca.id_lacz.Count; i++)
                    {

                        grafik.zbior_laczy[sciezka_powiekszajaca.id_lacz[i] - 1].przeplyw += min;

                    }


                    // Teraz trzeba sciezke powiekszajaca dodac do listy sciezek powiekszajacych dla zapotrzebowania 
                    // Najpierw sprawdzamy czy w Sieci(grafik) nie ma juz takiej sciezki


                    int l = 0;
                    int f;
                    int z = 0;

                    for (; l < grafik.wszystkie_sciezki.Count; l++)
                    {


                        if (grafik.wszystkie_sciezki[l].id_lacz.Count == sciezka_powiekszajaca.id_lacz.Count)
                        {
                            int y = 0;
                            bool bequal = true; ;

                            for (; y < grafik.wszystkie_sciezki[l].id_lacz.Count; y++)
                            {
                                if (grafik.wszystkie_sciezki[l].id_lacz[y] != sciezka_powiekszajaca.id_lacz[y])
                                {
                                    bequal = false;
                                    break;


                                }


                            }

                            if (bequal)
                            {

                                z = 2;
                                f = grafik.wszystkie_sciezki[l].id;
                                int o = 0;
                                for (; o < tabzapotrzebowan[v].id_sciezek.Count; o++)
                                {

                                    if (tabzapotrzebowan[v].id_sciezek[o] == f)
                                    {
                                        tabzapotrzebowan[v].przeplywy[o] += min;


                                    }


                                }


                            }

                        }
                    }



                    if (z == 0)
                    {

                        grafik.wszystkie_sciezki.Add(sciezka_powiekszajaca);

                        grafik.wszystkie_sciezki[grafik.wszystkie_sciezki.Count - 1].id = grafik.wszystkie_sciezki.Count;

                        tabzapotrzebowan[v].id_sciezek.Add(sciezka_powiekszajaca.id);
                        tabzapotrzebowan[v].przeplywy.Add(min);


                    }

                    // Powyzszy kod jest niestety bardzo zawily. Ustawia flage z na 2 jesli znalazl juz sciezke w zbiorze sciezek w Sieci(grafik)
                    // Wtedy juz nie jest ponowne jego dodawanie do grafiku. Dodaje przeplyw do tej sciezki. W przeciwnym razie z == 0 i dodajemy sciezke do grafiku 
                    // oraz zapotrzebowania


                    //uaktualnienie zrealizowanego przeplywu


                    tabzapotrzebowan[v].zrealizowano = tabzapotrzebowan[v].przeplywy.Sum();


                    if (tabzapotrzebowan[v].zrealizowano == tabzapotrzebowan[v].rozmiar)
                    {

                        break;

                    }


                }


            }


            // obliczamy koszt realizacji przeplywow

            double koszt = 0;
            int r = 0;
            for (; r < grafik.liczba_laczy; r++)
            {

                koszt += (grafik.zbior_laczy[r].koszt) * (grafik.zbior_laczy[r].przeplyw);

            }



            // Zapis do pliku





            FileStream fs = File.Create(_wyjscie);

            StreamWriter qw = new StreamWriter(fs);


            qw.WriteLine("# koszt rozwiazania");
            qw.Write("KOSZT = ");
            qw.WriteLine(koszt);
            qw.WriteLine();
            qw.WriteLine("# liczba uzytych sciezek");
            qw.Write("SCIEZKI = ");
            qw.WriteLine(grafik.wszystkie_sciezki.Count);
            qw.WriteLine("# kazda sciezka to id. sciezki i zbior id. laczy");
            i = 0;
            for (; i < grafik.wszystkie_sciezki.Count; i++)
            {
                qw.Write(grafik.wszystkie_sciezki[i].id);
                qw.Write(" ");
                j = 0;
                for (; j < grafik.wszystkie_sciezki[i].id_lacz.Count; j++)
                {

                    qw.Write(grafik.wszystkie_sciezki[i].id_lacz[j]);
                    qw.Write(" ");



                }
                qw.WriteLine();




            }
            qw.WriteLine();
            qw.WriteLine("# liczba zapotrzebowan");
            qw.Write("ZAPOTRZEBOWANIA = ");
            qw.WriteLine(ile_zapotrzebowan);
            qw.WriteLine("# kazde zapotrzebowanie to id. zapotrzebowania oraz zbior par: id. sciezki, pojemnosc zarezerwowana na sciezce");

            i = 0;
            for (; i < ile_zapotrzebowan; i++)
            {

                qw.Write(tabzapotrzebowan[i].id);
                qw.Write(" ");
                j = 0;
                for (; j < tabzapotrzebowan[i].id_sciezek.Count; j++)
                {
                    qw.Write(tabzapotrzebowan[i].id_sciezek[j]);
                    qw.Write(" ");
                    qw.Write(tabzapotrzebowan[i].przeplywy[j]);
                    qw.Write(" ");


                }
                qw.WriteLine();


            }

            qw.Close();
            fs.Close();



        }


    }



    class Wezel
    {
        public Wezel(int _id)
        {
            id = _id;


        }
        public int id;



    }
    class Lacze
    {
        public Lacze(int _id, Wezel _wezel_pocz, Wezel _wezel_konc, double _przepustowosc, double _koszt)
        {
            id = _id;
            wezel_pocz = _wezel_pocz;
            wezel_konc = _wezel_konc;
            przepustowosc = _przepustowosc;
            koszt = _koszt;
            przeplyw = 0;
            przepustowosc_resztkowa = 0;

        }


        public int id;
        public Wezel wezel_pocz;
        public Wezel wezel_konc;
        public double przepustowosc;
        public double koszt;
        public double przeplyw;
        public double przepustowosc_resztkowa;

    }
    class Sciezka
    {
        public int id;
        public List<int> id_lacz;

    }



    class Siec
    {

        public Siec(int _liczba_laczy, int _liczba_wezlow)
        {

            liczba_laczy = _liczba_laczy;
            liczba_wezlow = _liczba_wezlow;
            zbior_wezlow = new Wezel[_liczba_wezlow];
            zbior_laczy = new Lacze[_liczba_laczy];

        }

        public int liczba_laczy;
        public int liczba_wezlow;
        public Wezel[] zbior_wezlow;
        public Lacze[] zbior_laczy;
        public List<Sciezka> wszystkie_sciezki;
        public int liczba_zapotrzebowan;

    }

    class zapotrzebowanie
    {

        public int id;
        public Wezel zrodlo;
        public Wezel ujscie;
        public double rozmiar;
        public double zrealizowano;
        public List<int> id_sciezek;
        public List<double> przeplywy;

        public zapotrzebowanie(int _id, Wezel _zrodlo, Wezel _ujscie, double _rozmiar)
        {
            id = _id;
            zrodlo = _zrodlo;
            ujscie = _ujscie;
            rozmiar = _rozmiar;
            zrealizowano = 0;

        }

    }

    class poprawiania_etykiet
    {

        public List<int> najkrotsza(int vo, Siec _siec, int vt)
        {


            // Jest to wersja algorytmu poprawiania etykiet, szukajacych najkrotszej(wzgledem specjalnej wagi) sciezki


            double[] L = new double[_siec.liczba_wezlow];
            int[] P = new int[_siec.liczba_wezlow];     //tablica poprzednikow wierzcholka na najkrotszej sciezce
            for (int j = 0; j < _siec.liczba_wezlow; j++)

                if (_siec.zbior_wezlow[j].id == vo)
                {
                    L[j] = 0;
                }
                else
                {
                    L[j] = 100000.0;


                }


            Queue<Wezel> fifo = new Queue<Wezel>();
            fifo.Enqueue(_siec.zbior_wezlow[vo - 1]);
            while (fifo.Count != 0)
            {
                Wezel v = fifo.Dequeue();
                int i = 0;
                for (; i < _siec.liczba_laczy; i++)
                {
                    if ((_siec.zbior_laczy[i].wezel_pocz.id == v.id) && (_siec.zbior_laczy[i].przepustowosc_resztkowa != 0))
                    {
                        if (L[_siec.zbior_laczy[i].wezel_konc.id - 1] > L[v.id - 1] + (1 + (_siec.zbior_laczy[i].przeplyw / (_siec.zbior_laczy[i].przepustowosc_resztkowa)) * Math.Pow((_siec.zbior_laczy[i].koszt), 2)))
                        {
                            L[_siec.zbior_laczy[i].wezel_konc.id - 1] = L[v.id - 1] + (1 + (_siec.zbior_laczy[i].przeplyw / (_siec.zbior_laczy[i].przepustowosc_resztkowa)) * Math.Pow((_siec.zbior_laczy[i].koszt), 2));
                            P[_siec.zbior_laczy[i].wezel_konc.id - 1] = v.id;
                            fifo.Enqueue(_siec.zbior_laczy[i].wezel_konc);

                        }


                    }
                }



            }

            // Powyzej uzylismy specjalnej wagi (1 + (_siec.zbior_laczy[i].przeplyw / (_siec.zbior_laczy[i].przepustowosc_resztkowa)) * Math.Pow((_siec.zbior_laczy[i].koszt),2)
            // napoczatku przeplywy rownaja sie zero i kazde lacze ma wage 1 wiec algorytm wyszuka najkrotsza pod wzgledem ilosci laczy sciezke
            // potem bedzie znajdywal inne sciezki gdyz drugi czlon tej wagi bedzie sie zwiekszal, co chroni przed zapychaniem lacz
            // oraz minimalizuje koszt. 


            // korzystajac z tablicy poprzednikow tworzymy sciezke

            int z = vt;
            List<int> sciezka = new List<int>();
            while (z != 0)
            {
                sciezka.Insert(0, z);
                z = P[z - 1];

            }

            int a = 0;


            Sciezka _sciezka = new Sciezka();
            _sciezka.id_lacz = new List<int>();




            for (; a < sciezka.Count - 1; a++)
            {
                int j = 0;
                for (; j < _siec.liczba_laczy; j++)
                {
                    if ((_siec.zbior_laczy[j].wezel_pocz.id == sciezka[a]) && (_siec.zbior_laczy[j].wezel_konc.id == sciezka[a + 1]))
                    {

                        _sciezka.id_lacz.Add(_siec.zbior_laczy[j].id);

                    }

                }


            }
            // zwraca najkrotsza sciezke 

            return _sciezka.id_lacz;
        }



    }

}






