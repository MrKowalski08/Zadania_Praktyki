import subprocess
import argparse
import time

class Main:
    def __init__(self):
        with open("ip.txt", "r") as f:
            self.content = [line.strip() for line in f if line.strip()]
            self.parser = argparse.ArgumentParser()
            

    def run(self):
        self.parser.add_argument("-n", action="store_true", help="run normaly")
        self.parser.add_argument("-r", action="store_true", help="rebooting in 5 min")
        self.args = self.parser.parse_args()

        if self.args.p:
            with open("result.txt", "w") as out:
                for ip in self.content:
                    print(f"Pinguje: {ip}")
                    try:
                        subprocess.run(
                            ["ping", "-n", "1", ip],
                            stdout = subprocess.DEVNULL,
                            stderr = subprocess.DEVNULL,
                            check = True
                        )
                        status = True
                    except subprocess.CalledProcessError:
                        status = False
                    
                    out.write(f"{ip} -> {status}\n")

        if self.args.r:
            while True:
                subprocess.run(
                    ["ping", "-n", "1", "10.62.6.132"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                subprocess.run(["adb", "reboot"])
                time.sleep(300)
Main().run()
