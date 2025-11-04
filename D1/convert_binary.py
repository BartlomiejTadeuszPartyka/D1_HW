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