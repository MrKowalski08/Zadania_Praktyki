import os

class Main:
    def __init__(self):
        self.f = open('ip.txt', 'r')
        self.content = self.f.read().split("\n")
    def run(self):
        print(self.content)

Main().run()