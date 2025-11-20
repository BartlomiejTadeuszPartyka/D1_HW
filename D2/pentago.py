# 14. Zaskocz mnie :) Wymyśl swój własny program. Coś co np rozwiązuje Twój realny problem z pracy czy z życia codziennego.
#      Postarajcie się wymyśleć taki programik w którym użyjecie jak najwięcej poznanych rzeczy, np: łapanie wyjątków, pętle, operacje na plikach, korzystanie z nowych instalowanych z zewnątrz modułów etc.
#      Możecie też używać czegoś czego nie było na zajęciach (np kolorowanie tekstu w konsoli) a znaleźliście w internecie - byle byście rozumieli napisany kod :)
#      Przykłady: "zmieniacz - zmiana nazw wielu plików na raz", "kalambury - generator haseł", "enigma - szyfrowanie, odszyfrowywanie tekstu"...
#      Liczę na waszą inwencję, programy nie muszą być użyteczne - mogą być po prostu zabawne :)

import re
import os
from random import randint, choice


class Pentago:
    def __init__(self):
        self.quarter_1 = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.quarter_2 = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.quarter_3 = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.quarter_4 = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.board = {
            "A": self.quarter_1,
            "B": self.quarter_2,
            "C": self.quarter_3,
            "D": self.quarter_4
        }
        self.header = "      A           B"
        self.top_border = "╔═══╤═══╤═══╦═══╤═══╤═══╗"
        self.qrt_border = "╟───┼───┼───╫───┼───┼───╢"
        self.mid_border = "╠═══╪═══╪═══╬═══╪═══╪═══╣"
        self.btm_border = "╚═══╧═══╧═══╩═══╧═══╧═══╝"
        self.footer = "      C           D"
        self.symbols = {"player": "x", "cpu": "o"}

    def print_row(self, row_index):
        if row_index > 2:
            temp = row_index - 3
            left_quarter = "C"
            right_quarter = "D"
        else:
            temp = row_index
            left_quarter = "A"
            right_quarter = "B"
        print(f"║ "
              f"{self.board[left_quarter][temp][0]} │ {self.board[left_quarter][temp][1]} │ {self.board[left_quarter][temp][2]} ║ "
              f"{self.board[right_quarter][temp][0]} │ {self.board[right_quarter][temp][1]} │ "
              f"{self.board[right_quarter][temp][2]} ║")

    def print_board(self):
        print(self.header)
        print(self.top_border)
        self.print_row(0)
        print(self.qrt_border)
        self.print_row(1)
        print(self.qrt_border)
        self.print_row(2)
        print(self.mid_border)
        self.print_row(3)
        print(self.qrt_border)
        self.print_row(4)
        print(self.qrt_border)
        self.print_row(5)
        print(self.btm_border)
        print(self.footer)

    @staticmethod
    def rotate_quarter(matrix, direction):
        # Obrót w prawo: transpozycja + odwrócenie wierszy
        if direction == "r":
            return [list(reversed(col)) for col in zip(*matrix)]

        # Obrót w lewo: transpozycja + odwrócenie kolumn
        if direction == "l":
            return [list(col) for col in zip(*matrix)][::-1]

    def validate_move(self, move) -> bool:
        qrt = move[0]
        row = int(move[1])
        col = int(move[2])
        if self.board[qrt][row][col] == " ":
            return True
        else:
            return False

    def check_for_win(self):
        result = False
        allowed = "".join(re.escape(s) for s in self.symbols.values())
        pattern = fr'([{allowed}])\1{{4}}'
        rows = [
            "".join(self.board["A"][0] + self.board["B"][0]),
            "".join(self.board["A"][1] + self.board["B"][1]),
            "".join(self.board["A"][2] + self.board["B"][2]),
            "".join(self.board["C"][0] + self.board["D"][0]),
            "".join(self.board["C"][1] + self.board["D"][1]),
            "".join(self.board["C"][2] + self.board["D"][2])
            ]

        columns = [
            self.board["A"][0][0] + self.board["A"][1][0] + self.board["A"][2][0] + self.board["C"][0][0] + self.board["C"][1][0] + self.board["C"][2][0],
            self.board["A"][0][1] + self.board["A"][1][1] + self.board["A"][2][1] + self.board["C"][0][1] + self.board["C"][1][1] + self.board["C"][2][1],
            self.board["A"][0][2] + self.board["A"][1][2] + self.board["A"][2][2] + self.board["C"][0][2] + self.board["C"][1][2] + self.board["C"][2][2],
            self.board["B"][0][0] + self.board["B"][1][0] + self.board["B"][2][0] + self.board["D"][0][0] + self.board["D"][1][0] + self.board["D"][2][0],
            self.board["B"][0][1] + self.board["B"][1][1] + self.board["B"][2][1] + self.board["D"][0][1] + self.board["D"][1][1] + self.board["D"][2][1],
            self.board["B"][0][2] + self.board["B"][1][2] + self.board["B"][2][2] + self.board["D"][0][2] + self.board["D"][1][2] + self.board["D"][2][2]
        ]

        across = [
            self.board["A"][0][1] + self.board["A"][1][2] + self.board["B"][2][0] + self.board["D"][0][1] + self.board["D"][1][2],
            self.board["A"][1][0] + self.board["A"][2][1] + self.board["C"][0][2] + self.board["D"][1][0] + self.board["D"][2][1],
            self.board["B"][0][1] + self.board["B"][1][0] + self.board["A"][2][2] + self.board["C"][0][1] + self.board["C"][1][0],
            self.board["B"][1][2] + self.board["B"][2][1] + self.board["D"][0][0] + self.board["C"][1][2] + self.board["C"][2][1],
            self.board["A"][0][0] + self.board["A"][1][1] + self.board["A"][2][2] + self.board["D"][0][0] + self.board["D"][1][1] + self.board["D"][2][2],
            self.board["B"][0][2] + self.board["B"][1][1] + self.board["B"][2][0] + self.board["C"][0][2] + self.board["C"][1][1] + self.board["C"][2][0],
        ]

        temp_list = rows + columns + across

        for text in temp_list:
            match = re.search(pattern, text)
            if match:
                result = True
                break
        return result

    def parse_move(self, quarter, field, entity):
        temp = field
        if field == 1:
            field = "20"
        elif field == 2:
            field = "21"
        elif field == 3:
            field = "22"
        elif field == 4:
            field = "10"
        elif field == 5:
            field = "11"
        elif field == 6:
            field = "12"
        elif field == 7:
            field = "00"
        elif field == 8:
            field = "01"
        elif field == 9:
            field = "02"

        move = quarter + field

        if self.validate_move(move):
            print(f"Putting '{self.symbols[entity]}' into {quarter}{temp}")
            self.board[move[0]][int(move[1])][int(move[2])] = self.symbols[entity]
            return True
        else: return False

    def player_move(self):
        while True:
            quarter = input("Choose a quarter (A-D): ").upper()[0] # mikro-zabezpieczenie - pod uwagę jest brany tylko pierwszy znak
            field = int(input("Select field (1-9, like on a numpad): ")[0])
            if self.parse_move(quarter, field, "player"):
                self.print_board()
                break
            else:
                print("Invalid input")
        rot = input("Choose rotation direction (R/L): ").lower()
        if rot == "r":
            rot = "right"
        elif rot == "l":
            rot = "left"
        self.board[quarter] = self.rotate_quarter(self.board[quarter], rot[0])
        print(f"Rotating quarter {quarter} {rot}.")

    def cpu_move(self):
        while True:
            quarter = choice(["A", "B", "C", "D"])
            field = randint(1, 9)
            if self.parse_move(quarter, field, "cpu"):
                self.print_board()
                break
        rot = choice(["right", "left"])
        self.board[quarter] = self.rotate_quarter(self.board[quarter], rot[0])
        print(f"Rotating quarter {quarter} {rot}.")

    def mainloop(self):
        while True:
            os.system('cls') # uwaga, działa tylko w terminalu
            self.print_board()
            self.player_move()
            if self.check_for_win():
                winner = "sz!"
                break
            self.cpu_move()
            if self.check_for_win():
                winner = " komputer!"
                break

        print(f"\n\n\n\n\n\n\n\n\n\nBrawo! Wygrywa{winner}\n\n")
        self.print_board()


