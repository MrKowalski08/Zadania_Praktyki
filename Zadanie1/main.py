import os

class Main:
    def __init__(self):
        self.f = open('ip.txt', 'r')
        self.content = self.f.read().split("\n")
    def run(self):
        for ip in self.content:
            print(f"Pinguje: {ip}")
            os.system(f"ping -n 1 {ip}")

Main().run()
import os

class Main:
    def __init__(self):
        with open("ip.txt", "r") as f:
            self.content = [line.strip() for line in f if line.strip()]

    def run(self):
        with open("result.txt", "w") as out:
            for ip in self.content:
                print(f"Pinguje: {ip}")
                result = os.system(f"ping -n 1 {ip} > nul")

                status = result == 0
                out.write(f"{ip} -> {status}\n")

Main().run()
