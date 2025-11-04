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
