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