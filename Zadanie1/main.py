import subprocess

class Main:
    def __init__(self):
        with open("ip.txt", "r") as f:
            self.content = [line.strip() for line in f if line.strip()]

    def run(self):
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

Main().run()
