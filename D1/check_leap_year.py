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