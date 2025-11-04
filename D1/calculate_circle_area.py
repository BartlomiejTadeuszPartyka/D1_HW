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