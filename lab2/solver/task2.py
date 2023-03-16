import json
import os
import re


class Container:
    def __init__(self, username):
        self.username = username
        self.storage = set()
        self.user_file = f'./data/{username}.txt'
        self.load()

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
                self.storage = set(file.readline())
                self.storage.remove('\n')
                file.close()

    def switch(self, username):
        self.username = username
        self.user_file = f'./data/{username}.txt'
        self.storage.clear()
        self.load()
