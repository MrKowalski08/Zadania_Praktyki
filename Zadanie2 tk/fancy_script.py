import subprocess
import time
import tkinter as tk
import xml.etree.ElementTree as ET
import os

class Fancy:
    def add_to_list(self, address, list):
        text = address.get()
        if text:
            list.insert(tk.END, text)
            address.delete(0, tk.END)

    # def get_from_file(self, ip):
        
    

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

    def reboot_ip(self,i_ip):
        ip = i_ip.get()
        while True:
            subprocess.run(["ping", "-n", "1", ip], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
            subprocess.run(["adb", "connect", ip])
            subprocess.run(["adb", "reboot"])
            time.sleep(300)

    def search_NetworkPref(self, i_ip,i_path,i_name,callback):
        ip = i_ip.get()
        path = i_path.get()
        name = i_name.get()
        subprocess.run(["adb", "connect", str(ip)])
        subprocess.run(["adb", "root"])
        result = subprocess.run(["adb", "shell", "cat", path],
                    capture_output=True,
                    text=True,
        )
        data = ET.fromstring(result.stdout)
        print(data.find(f".//string[@name='{name}']").text)
        value = data.find(f".//string[@name='{name}']").text
        callback(value)
        subprocess.run(["adb","disconnect"])


    def search_File_based_ip(self, i_ip,i_path,i_name):
        ips = i_ip.get(0, "end")
        path = i_path.get()
        name = i_name.get()

        for ip in ips:
            subprocess.run(["adb", "connect", str(ip)])
            subprocess.run(["adb", "root"])

            full_path = f"{path.rstrip('/')}/{name}"

            result = subprocess.run(
                ["adb", "shell", f"if [ -d '{full_path}' ] || [ -f '{full_path}' ]; then echo EXISTS; else echo NONE; fi"],
                capture_output=True,
                text=True,)
            print(result.stdout)
            subprocess.run(["adb","disconnect"])  

