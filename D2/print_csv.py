# 11. Stwórz program który przyjmie w parametrze ścieżkę do dowolnego pliku (CSV lub Excel - jaki wolicie), który będzie zawierał dane tabelaryczne.
#    W pliku pierwszy wiersz będzie zawierał nazwy kolumn a pozostałe wiersze dane.
#    Ilość kolum i wierszy może być dowolna. Program ma narysować tabelę z danymi, analogicznie do wcześniejszego zadania na rysowanie tabeli.
#    Pamiętajmy by wydzielać części reużywalne do oddzielnych funkcji/modułów (np.: odczyt danych, przygotowanie danych, rysowanie tabeli).
#    Przykład:
#    +------------+------------+------------+
#    | klucz1     | klucz 2    | klucz 3    |
#    +------------+------------+------------+
#    | row 1 col1 | row 1 col2 | row 1 col3 |
#    +------------+------------+------------+
#    | row 2 col1 | row 2 col2 | row 2 col3 |
#    +------------+------------+------------+

import csv
import os
from D1.draw_table import draw_table

def get_data(file_name="data1.csv", file_path = r"C:\Users\bpartyka\PycharmProjects\ISA\D1_HW\data\D2\ex11"):
    full_path = os.path.join(file_path, file_name)

    data = []

    with open(full_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def print_csv():
    user_file = input("Enter file name: ")
    draw_table(get_data(file_name=user_file))
