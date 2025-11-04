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
