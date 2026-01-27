import subprocess
import time
import tkinter as tk

class Fancy:
    def add_to_list(self, address, list):
        text = address.get()
        if text:
            list.insert(tk.END, text)
            address.delete(0, tk.END)

    def ping_ip(self,list):
        with open("result.txt", "w") as out:
            all_ips = list.get(0, "end")
            for ip in all_ips:
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

    def reboot_ip(self,input):
        ip = input.get()
        while True:
            subprocess.run(["ping", "-n", "1", ip], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
            subprocess.run(["adb", "connect", ip])
            subprocess.run(["adb", "reboot"])
            time.sleep(300)
