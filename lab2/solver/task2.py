import os
import re


class Container:
    def __init__(self, username):
        self.username = username
        self.storage = set()
        self.user_file = f'./data/{username}.txt'
        self.process = True

    def add(self, element):
        self.storage.add(element)

    def remove(self, element):
        self.storage.remove(element)

    def find(self, element):
        return element in self.storage

    def list(self):
        return list(self.storage)

    def grep(self, regex):
        return list(filter(lambda el: re.match(regex, el), self.storage))

    def save(self):
        os.makedirs(os.path.dirname(self.user_file), exist_ok=True)
        with open(self.user_file, 'w') as file:
            for line in self.list():
                file.write(line + "\n")
            file.close()

    def load(self):
        if os.path.exists(self.user_file):
            with open(self.user_file, 'r') as file:
                for line in file.readlines():
                    self.add(line[:len(line)-1])
            file.close()

    def switch(self, username):
        self.username = username
        self.user_file = f'./data/{username}.txt'
        self.storage.clear()

    def cli(self):
        print(f"Welcome, {self.username}")
        old_user = self.username
        while self.process:
            old_user = self.username
            print("Enter the command: ")
            commands = input('> ').split()
            if commands[0] == "switch":
                ans = input("Do you want to save data before switching? [y/n]\n")
                if ans.lower() == "y":
                    self.save()
            if self.take_command(commands):
                print(self.take_command(commands))
            print(self.storage)
            if old_user != self.username:
                ans = input("Do you want to load data? [y/n]\n")
                if ans.lower() == "y":
                    self.load()
        return

    def take_command(self, commands):
        match commands[0]:
            case  "add":
                for command in commands[1:]:
                    self.add(command)
            case "remove":
                if self.find(commands[1]):
                    self.remove(commands[1])
                else:
                    return "No such element"
            case "find":
                res = ""
                for command in commands[1:]:
                    if self.find(command):
                        res = res + f"{command}: Found\n"
                    else:
                        res = res + f"{command}: No such element\n"
                return res

            case "list":
                self.list()
            case "grep":
                reg = self.grep(commands[1])
                res = ""
                for num in self.storage:
                    if num in reg:
                        res = res + f"{num}: Found\n"
                    else:
                        res = res + f"{num}: No such element\n"
                return res
            case "save":
                self.save()
            case "load":
                self.load()
            case "switch":
                self.switch(commands[1])
                return f"Welcome, {self.username}"
            case "break":
                self.process = False
                return f"All the best, {self.username}"
            case "help":
                return "add <key>\n" \
                       "remove <key>\n" \
                       "find <key>\n" \
                       "grep <regex>\n" \
                       "list\n" \
                       "save\n" \
                       "load\n" \
                       "switch\n"
            case _:
                return "Incorrect operation\nEnter 'help' for a list of built-in commands."


def main():
    a = Container("Anton")
    a.cli()


if __name__ == "__main__":
    main()