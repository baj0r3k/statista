    Statista - Aplikacja do obliczania podstawowych statystyk

Opis projektu

Statista to prosta aplikacja stworzona w Pythonie z wykorzystaniem biblioteki Tkinter. Umożliwia użytkownikowi obliczanie podstawowych miar statystycznych, takich jak:

    *Średnia arytmetyczna (zwykła, ważona, liczona na podstawie wartości i liczności)

    *Odchylenie standardowe (dla różnych wariantów danych)

    *Asymetria

    *Mediana

    *Współczynnik zmienności

    *Wartość oczekiwana i wariancja w rachunku prawdopodobieństwa

Aplikacja pozwala na szybkie wprowadzenie danych w postaci liczb oddzielonych przecinkami oraz ich natychmiastowe przetworzenie.

Wymagania

Do uruchomienia aplikacji wymagane jest:

Python 3.8 lub nowszy

Biblioteka Tkinter

Biblioteka NumPy


Instalacja

Sklonuj repozytorium

git clone https://github.com/twoje_repo/statista.git
cd statista

statista/
│── SGH_Statystyka_wzory/
│   ├── averages.py       # Funkcje do obliczania średnich
│   ├── variances.py      # Funkcje wariancji i wartości oczekiwanej
│   ├── asymetry.py       # Funkcje dotyczące asymetrii
│   ├── mediana.py        # Funkcja do obliczania mediany
│   ├── statista.py       # Główny plik aplikacji 
│── README.md             # Opis projektu


Sposób działania

Uruchom aplikację.

Wprowadź dane liczbowe oddzielone przecinkami w odpowiednich polach tekstowych.

Wybierz odpowiednią funkcję statystyczną poprzez kliknięcie przycisku.

Wynik zostanie wyświetlony w oknie dialogowym.


Przykłady użycia

*Obliczenie średniej arytmetycznej: Wpisz wartości w pierwszej luce 10, 20, 30, 40 i kliknij xj.

*Obliczenie mediany: Wpisz w pierwszej luce 5, 10, 15, 20, 25 i kliknij mediana.

*Obliczenie wartości oczekiwanej: Wpisz 1,2,3 jako wartości oraz 0.2,0.5,0.3 jako prawdopodobieństwa, a następnie kliknij E(x)