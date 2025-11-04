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
