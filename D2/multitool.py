# 15. Stworzenie "programu nakładki" na dotychczasowe programiki.
#    Po wyborze danego programu z "menu" uruchomi się odpowiedni i po wykonaniu danej operacji zapyta czy wykonać inny program.
#    Sugeruje by każdy podprogram był oddzielną funkcją a może nawet modułem.
#    Miejmy na uwadze to by w przyszłości ten program rozwijać podpinając kolejny "podprogram" - powinno to być najprostsze jak się da (np tylko zmiana menu i jakiegoś jednego ifa?:) )
#    Przypominam, że np funkcje można przypisywać do zmiennych.
#
# 16. Dodajcie do multitoola licznik uruchomienia każdego podprogramu i samego multitoola. Dane możecie zapisać w dowolnym pliku CSV/pickle/Excel.
#      Do menu dodajcie pozycję/podprogramik "S - Statystyki" który w przyjaznej formie przedstawi wszystkie statystyki.

from D1.convert_temperatures import convert_temperatures
from D1.calculate_circle_area import calculate_circle_area
from D1.draw_rectangle import draw_rectangle
from D1.convert_binary import convert_binary
from D1.check_leap_year import check_leap_year
from D1.factorial_calculator import factorial_calculator
from D1.change_calculator import change_calculator
from D1.draw_pyramid import draw_pyramid
from D2.diary import Diary
from D2.print_csv import print_csv
from D2.pentago import Pentago
import pickle
import os


class Multitool:
    def __init__(self):
        self.stats_file = "../data/D2/ex16/multitool_stats.pkl"
        self._load_stats()
        self.subroutines = [
            ("Convert temperatures (C->F, F->C)", convert_temperatures),
            ("Calculate circle area", calculate_circle_area),
            ("Draw rectangles", draw_rectangle),
            ("Convert binary -> decimal, decimal -> binary", convert_binary),
            ("Check leap year", check_leap_year),
            ("Calculate factorial", factorial_calculator),
            ("Calculate optimal change", self.change_wrapper),
            ("Draw pyramids", draw_pyramid),
            ("Take a look at my diary", self.diary_wrapper),
            ("Print CSV in console", print_csv),
            ("Play pentago", self.pentago_wrapper)
        ]

    @staticmethod
    def change_wrapper():
        change_calculator(float(input("Enter amount to change: ")))

    @staticmethod
    def diary_wrapper():
        Diary().mainloop()

    @staticmethod
    def pentago_wrapper():
        Pentago().mainloop()

    def _load_stats(self):
        """Wczytuje statystyki z pliku pickle lub tworzy nowe."""
        os.makedirs(os.path.dirname(self.stats_file), exist_ok=True)
        try:
            with open(self.stats_file, 'rb') as f:
                data = pickle.load(f)
                self.main_runs = data.get('main_runs', 0)
                self.sub_runs = data.get('sub_runs', [0] * 11)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            self.main_runs = 0
            self.sub_runs = [0] * 11

        # Zwiększ licznik uruchomień programu
        self.main_runs += 1
        self.save_stats()

    def save_stats(self):
        """Zapisuje statystyki do pliku pickle."""
        data = {
            'main_runs': self.main_runs,
            'sub_runs': self.sub_runs
        }
        with open(self.stats_file, 'wb') as f:
            pickle.dump(data, f)

    def mainloop(self):
        while True:
            print(f"\n=== Main Menu (Program run #{self.main_runs}) ===")
            print("What do you want to do?")
            for i, (desc, _) in enumerate(self.subroutines, 1):
                print(f"\t{i}. {desc} [runs: {self.sub_runs[i - 1]}]")

            choice = input(">>> ")
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(self.subroutines):
                    self.sub_runs[idx] += 1
                    self.save_stats()
                    self.subroutines[idx][1]()
                else:
                    print("Invalid choice!")
            except (ValueError, IndexError):
                print("Invalid input!")