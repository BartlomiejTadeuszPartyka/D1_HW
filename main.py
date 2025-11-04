# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (niech program zapyta o kierunek konwersji)
def convert_temperatures() -> None:
    """Converts temperatures between degrees Celsius and Fahrenheit, as prompted by the user."""
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
def calculate_circle_area() -> None:
    """Calculates circle area based on user-defined radius. Shows calculations step by step."""
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
def draw_rectangle() -> None:
    """Draws a simple rectangle as per user's instructions."""
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
def convert_binary() -> None:
    """Converts numbers between decimal and binary, as prompted by the user."""
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
def check_leap_year() -> None:
    """Checks if the year is a leap year."""
    print("~~Sprawdź, czy dany rok jest rokiem przestępnym~~")
    while True:
        print("Podaj rok do sprawdzenia lub wpisz 'E', aby wyjść")
        year = input(">>> ")
        if year.isdigit():
            year = int(year)
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"Rok {year} jest rokiem przestępnym")
            else:
                print(f"Rok {year} nie jest rokiem przestępnym")
        else:
            break

# 6. Napisz program do wyliczania silni dla zadanej liczby
def factorial_calculator() -> None:
    """A simple factorial calculator."""
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
def change_calculator(amount: float) -> None:
    """A simple function to optimise change.
    :param amount: amount to change
    :type amount: float"""
    print("~~Optymalna maszynka do rozmieniania~~")
    coins =  {"500": 0,
                "200": 0,
                "100": 0,
                "50": 0,
                "20": 0,
                "10": 0,
                "5": 0,
                "2": 0,
                "1": 0}
    print("Potrzebujesz następujących monet:")
    amount = int(round(amount, 2) * 100)
    for coin in coins:
        temp = amount % int(coin)
        coins[coin] = (amount - temp) / int(coin)
        amount = temp
        print(f"\t{int(coin)/100}: {coins[coin]}")


# 8. Program rysujący piramidę o określonej wysokości, np dla 3
#         #
#       ###
#     #####
def draw_pyramid() -> None:
    """Draw a simple pyramid with user-defined height"""
    print("~~Narysuj sobie piramidkę~~")
    while True:
        print("Podaj liczbę pięter lub wpisz 'E', aby wyjść")
        height = input(">>> ")
        if height.isalpha():
            break
        else:
            height = int(height)
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

def nested_depth_level(lst) -> int:
    """Checks if a list is nested and returns values:
    0 - not a list
    1 - a non-nested list
    2 - a nested list
    :param lst: list to check
    :type lst: list
    :return: nesting depth"""
    for item in lst:
        if isinstance(item, list):
            if any(isinstance(subitem, list) for subitem in item):
                return 2  # więcej niż jeden poziom
            else:
                return 1  # tylko jeden poziom
    return 0  # brak zagnieżdżenia


def longest_sublist_length(lst) -> int:
    """Returns length of longest sublist or 0 if list is not nested.
    :param lst: list to check
    :type lst: list
    :return: length of the longest sublist"""
    sublists = [item for item in lst if isinstance(item, list)]
    if not sublists:
        return 0
    return max(len(sublist) for sublist in sublists)


def format_string(cell_content: str) -> str:
    """Formats a string according to requirements
    :param cell_content: cell content to be formatted
    :type cell_content: str
    :return: formatted cell content"""
    if len(cell_content) > 30:
        return cell_content[:27] + "..."
    else:
        return cell_content.ljust(30)


def draw_horizontal_line(n_columns: int) -> None:
    """Draws a horizontal line
    :param n_columns: number of columns in the table
    :type n_columns: int
    :return: None"""
    HORIZONTAL_LINE = "+" + "-" * 34
    print(HORIZONTAL_LINE * n_columns + "+")


def draw_row(content: list) -> None:
    """Draws a row with contents
    :param content: content to be put into cells, each item is printed in a separate cell
    :type content: list
    :return: None"""
    VERTICAL_LINE = "|  "
    row = ""
    for cell in content:
        cell = format_string(str(cell))
        row += VERTICAL_LINE + cell + "  "
    row += "|"
    print(row)


def draw_table(content: list) -> None:
    """
    Prints list's content as a table.
    :param content: A list containing the table's content.
                    In case of a nested list, each sub-list is treated as a row.
    :return: None
    """
    print("~~Narysuj sobie tabelę~~")
    nesting_level = nested_depth_level(content)

    if nesting_level == 0:
        # Jednowierszowa tabela
        columns_number = len(content)
        draw_horizontal_line(columns_number)
        draw_row(content)
        draw_horizontal_line(columns_number)

    elif nesting_level == 1:
        # Tabela wielowierszowa
        rows_number = len(content)
        columns_number = longest_sublist_length(content)

        draw_horizontal_line(columns_number)
        for row_index in range(rows_number):
            row = content[row_index]
            # Dopełnij brakujące komórki pustymi stringami
            padded_row = row + [""] * (columns_number - len(row))
            draw_row(padded_row)
            draw_horizontal_line(columns_number)

    else:
        print("Uwaga! Twoja lista ma zbyt wiele poziomów zagnieżdżenia. Sprawdź poprawność swoich danych.")


def main():
    draw_table([[1, 2, 3], [4, ''], [7, "Dłuuuuuuuuuuuuugi tekst", "Jeszcze dłuuuuuuuuuuuuższy tekst"]])

if __name__ == "__main__":
    main()
