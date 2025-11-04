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