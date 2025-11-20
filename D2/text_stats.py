import string

# 10. Napisz program, który poda statystki dowolnego tekstu pobranego z pliku, wypisze takie dane jak, np:
#    ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
#    Niech będzie możliwość wyboru tryb case sensitivity.
#    Niech program tworzy też plik ze statystyką swojej pracy. Czyli np:
#    "
#    Ilość uruchomień programu:
#    10
#    Przeanalizowanych znaków:
#    1223435991
#    Znalezionych wyrazów:
#    2399
#    Znalezionych liczb:
#    122
#    Znalezionych małych liter:
#    68923455
#    etc
#    "
#
#    Oczywiście dopuszalna jest ułomność takiego programu.
#    Dokładne policzenie ilość zdań nie jest trywialne ale może jakiś fajny algorytm uda się Wam wymyślić.
#    Rodzaje statystyk zostawiam waszej fantazji :)
#    Przydatny generator tekstu: http://lipsum.pl/

UPPER_CASE_COUNT = 0
LOWER_CASE_COUNT = 0
NUMBERS_COUNT = 0
WORDS_COUNT = 0
SENTENCES_COUNT = 0
PARAGRAPHS_COUNT = 0

try:
    with open(r"..\data\D2\ex10\sample_text.txt", "r") as text_file:
        text = text_file.read()
        mode = int(input("Wybierz tryb:\n\t1. Case sensitive\n\t2. Case insensitive\n>>> "))
        if mode == 1:
            print(text)

        elif mode == 2:
            pass
except FileNotFoundError:
    print("Nie znaleziono pliku. Sprawdź podaną ścieżkę.")