# 12. Napisz program który będzie pamiętnikiem. Niech posiada opcje:
#    - dodawania wpisu do pamiętnika pod określną datą DONE
#    - wyświetlanie wszystkich wpisów z pamiętnika DONE
#    - wyświetlanie wszystkich wpisów dla określonej daty DONE
#    - przeglądanie pojedyńczych wpisów z pamiętnika, opcja: "następny", "poprzedni"

import os
import json
import re
from datetime import datetime
from random import randint

BOLD = '\x1b[1m'
DIM = '\x1b[2m' # działa w terminalu, ale w konsoli pycharma nie
ITALIC = '\x1b[3m'
RESET = '\x1b[22m'

class Entry:
    def __init__(self, title, body):
        self.content = {
            'title': title,
            'date': "",
            'body': body
        }

    def save(self, directory):
        today = datetime.now().strftime("%Y-%m-%d")
        self.content["date"] = today
        pattern_start = f"{today}_entry_"

        existing = [
            filename for filename in os.listdir(directory)
            if filename.startswith(pattern_start) and filename.endswith(".json")
        ]

        max_index = 0
        for filename in existing:
            try:
                index_part = filename.split("_entry_")[1]
                index = int(index_part.split(".")[0])
                if index > max_index:
                    max_index = index
            except:
                continue

        new_index = max_index + 1
        filename = f"{today}_entry_{new_index}.json"
        full_path = os.path.join(directory, filename)

        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(self.content, f, indent=4, ensure_ascii=False)

        return full_path

class Diary:
    def __init__(self, records_path=r"C:\Users\bpartyka\PycharmProjects\ISA\D1_HW\data\D2\ex12"):
        self.records_path = records_path
        self.entries = []
        self.refresh_entries()


    def refresh_entries(self):
        pattern = re.compile(r"\d{4}-\d{2}-\d{2}_entry_\d+\.json$")
        matching_files = [f for f in os.listdir(self.records_path) if pattern.match(f)]

        if matching_files:
            for filename in matching_files:
                if filename not in self.entries:
                    self.entries.append(filename)

    def add_entry(self):
        title = input("Title: ")

        print('Content (type "finish" to end your entry): ')
        lines = []
        while True:
            line = input()
            if line == "finish":
                break
            lines.append(line)
        body = "\n".join(lines)

        new_entry = Entry(title, body)
        print(f"Entry saved in {new_entry.save(self.records_path)}")
        self.refresh_entries()

    def show_entries(self, date=""):
        print("\n\n")
        if date == "":
            for entry in self.entries:
                print(f"{self.entries.index(entry)+1}. {entry}")
            action = input("\n\nTo read an entry, choose the desired number. To go back write 'E'\n>>> ")
            if action != "E":
                self.read_entry(self.entries[int(action)-1])
        else:
            temp = [entry for entry in self.entries if date in entry]
            while True:
                for entry in temp:
                    print(f"{self.entries.index(entry)+1}. {entry}")
                action = input("\n\nTo read an entry, choose the desired number. To go back write 'E'\n>>> ")
                if action != "E":
                    self.read_entry(temp[int(action) - 1])
                else:
                    break


    def read_entry(self, entry_name):
        print("\n\n")
        with open(os.path.join(self.records_path, entry_name), "r", encoding="utf-8") as f:
            entry = json.load(f)
            print(f"{DIM}{entry['date']}{RESET}")
            print(f"{BOLD}{entry['title']}{RESET}\n\n")
            print(entry['body'])
        index = self.entries.index(entry_name)
        action = input("\n\nWhat do you want to do?\n\t1. Next entry\n\t2. Previous entry\n\t3. Exit\n>>> ")
        if action == "1":
            try:
                self.read_entry(self.entries[index+1])
            except IndexError:
                print("This is the lest entry!")
        elif action == "2":
            if index - 1 >= 0:
                self.read_entry(self.entries[index-1])
            else:
                print("This is the first entry!")
        elif action == "3":
            pass

    def mainloop(self):
        print(f"{ITALIC}Dear Diary...{RESET}\n")

        while True:
            print("\n\nChoose action:\n\t1. Add new entry,\n\t2. Browse entries,\n\t3. Browse entries by date,\n\t4. Exit")
            choice = input(">>> ")

            if choice == "1":
                self.add_entry()
            if choice == "2":
                self.show_entries()
            if choice == "3":
                date = input("Choose date (YYYY-MM-DD): ")
                self.show_entries(date)
            if choice == "4":
                if randint(1,1000) == 997:
                    print("Papa, przystojniaku!") # easter egg
                break
            print("\n\n")