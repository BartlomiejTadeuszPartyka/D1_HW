from math import ceil

# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (niech program zapyta o kierunek konwersji)
def convert_temperatures():
    print("~~Konwerter temperatur~~")
    while True:
        print("\nDostępne opcje:\n\t1. Stopnie Celsjusza do stopni Fahrenheita\n\t2. Stopnie Fahrenheita do stopni Celsjusza\n\t3. Wyjście")
        option = int(input(">>>"))
        if option == 1:
            temp_celsius = float(input("Podaj temperaturę w st. Celsjusza: "))
            temp_fahrenheit = temp_celsius * 1.8 + 32
            print(f"To będzie {temp_fahrenheit} w st. Fahrenheita")
        elif option == 2:
            temp_fahrenheit = float(input("Podaj temperaturę w st. Fahrenheita: "))
            temp_celsius = (temp_fahrenheit - 32) * 5 / 9
            print(f"To będzie {temp_celsius} w st. Celsjusza")
        elif option == 3:
            break
        else:
            print(f"Podano błędną instrukcję: {option}. Spróbuj ponownie.")

# 2. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)
def calculate_circle_area():
    PI = 3.14
    print("~~Program do obliczania pola koła~~")
    while True:
        print("Podaj promień koła lub wpisz 'E', żeby wyjść")
        option = input(">>>")
        if option.isdigit():
            option = float(option)
            print("Wzór na pole koła: P = Πr^2")
            print(f"Obliczmy r^2:\n\t{option}^2 = {option ** 2}")
            print(f"Obliczmy pole:\n\tA = Π*{option ** 2} ≈ {PI * option ** 2}")
            print(f"Pole koła o promieniu r = {option} jest równe w przybliżeniu {PI * option ** 2}")
        else:
            break

# 3. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +---+
#     |       |
#     |       |
#     +---+
def draw_rectangle():
    while True:
        width = int(input("\nPodaj szerokość prostokąta: "))
        height = int(input("Podaj wysokość prostokąta: "))

        print("+" + "-" * (width - 2) + "+")
        for i in range(height):
            print("|" + " " * (width - 2) + "|")
        print("+" + "-" * (width - 2) + "+")

        print("\n\nCzy chcesz narysować kolejny prostokąt? (T/N)")
        option = input(">>>")
        if option == "N":
            break

# 4. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny i odwrotnie (niech program zapyta o kierunek konwersji)
def convert_binary():
    print("~~Konwerter systemu dwójkowego~~")
    while True:
        print("\nDostępne opcje:\n\t1. System dziesiątkowy do systemu dwójkowego\n\t2. System dwójkowy do systemu dziesiątkowego\n\t3. Wyjście")
        option = int(input(">>> "))
        if option == 1:
            decimal = int(input("Podaj liczbę do konwersji: "))
            binary = bin(decimal)[2:]
            print(f"{decimal} w systemie dwójkowym to {binary}")
        elif option == 2:
            binary = input("Podaj liczbę do konwersji: ")
            decimal = int(binary, 2)
            print(f"{binary} w systemie dziesiątkowym to {decimal}")
        elif option == 3:
            print("Na razie!")
            break
        else:
            print(f"Podano błędną instrukcję: {option}. Spróbuj ponownie.")

# 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym.
def check_leap_year():
    print("~~Sprawdź, czy dany rok jest rokiem przestępnym~~")
    while True:
        print("Podaj rok do sprawdzenia lub wpisz 'E', aby wyjść")
        year = int(input(">>> "))
        if year.isdigit():
            if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
                print(f"Rok {year} jest rokiem przestępnym")
            else:
                print(f"Rok {year} nie jest rokiem przestępnym")
        else:
            break

# 6. Napisz program do wyliczania silni dla zadanej liczby
def factorial_calculator():
    print("~~Kalkulator silni~~")
    while True:
        print("Podaj liczbę, której silnię chcesz obliczyć lub wpisz 'E', aby wyjść")
        operand = input(">>> ")
        result = 1
        if operand.isdigit():
            for i in range(1, int(operand)+1):
                result *= i
            print(f"{operand}! = {result}")
        else:
            break

# 7. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.
def change_calculator():
    print("~~Optymalna maszynka do rozmieniania~~")
    while True:
        print("Podaj liczbę, którą chcesz rozmienić lub wpisz 'E', aby wyjść")
        amount = input(">>> ")
        five_zloty = 0
        two_zloty = 0
        one_zloty = 0
        fifty_grosz = 0
        twenty_grosz = 0
        ten_grosz = 0
        five_grosz = 0
        two_grosz = 0
        one_grosz = 0
        if amount.isalpha():
            break
        else:
            amount = int(ceil(float(amount) * 100))
            # pieciozlotowki
            temp = amount % 500
            five_zloty = (amount - temp) / 500
            amount = temp
            # dwuzlotowki
            temp = amount % 200
            two_zloty = (amount - temp) / 200
            amount = amount
            # jednozlotowki
            temp = amount % 100
            one_zloty = (amount - temp) / 100
            amount = temp
            #50-groszówki
            temp = amount % 50
            fifty_grosz = (amount - temp) / 50
            amount = temp
            #  20-groszówki
            temp = amount % 20
            twenty_grosz = (amount - temp) / 20
            amount = temp
            # 10-groszówki
            temp = amount % 10
            ten_grosz = (amount - temp) / 10
            amount = temp
            # pięciogroszówki
            temp = amount % 5
            five_grosz = (amount - temp) / 5
            amount = temp
            # dwugroszówki
            temp = amount % 2
            two_grosz = (amount - temp) / 2
            amount = temp
            # jednogroszówki
            temp = amount % 1
            one_grosz = (amount - temp) / 1
            amount = temp
            print(f"Potrzebujesz następujących monet\n\t5: {five_zloty}\n\t2: {two_zloty}\n\t1: {one_zloty}\n\t0.50: {fifty_grosz}\n\t0.20: {twenty_grosz}\n\t0.10: {ten_grosz}\n\t0.05: {five_grosz}\n\t0.02: {two_grosz}\n\t0.01: {one_grosz}")

# 8. Program rysujący piramidę o określonej wysokości, np dla 3
#         #
#       ###
#     #####
def draw_pyramid():
    print("~~Narysuj sobie piramidkę~~")
    while True:
        print("Podaj liczbę pięter lub wpisz 'E', aby wyjść")
        height = input(">>> ")
        if height.isalpha():
            break
        else:
            height = int(height)
            base_width = (height * 2) - 1
            for i in range(1, height+1):
                placeholder = ' ' * (height - i)
                hashes = '#' * (2 * i -1)
                print(placeholder + hashes)


# 9. Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn


def main():
    draw_pyramid()

if __name__ == "__main__":
    main()
