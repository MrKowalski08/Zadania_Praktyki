import tkinter as tk
import threading

from fancy_script import Fancy


# ---------- APP ----------
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("IP Checker / Rebooter")
        self.root.configure(bg="#2b2b2b")
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)

        self.fancy = Fancy()
        self.frame = tk.Frame(self.root)
        self.frame.configure(bg="#2b2b2b")
        self.frame.columnconfigure(0,weight=1)
        self.frame.rowconfigure(1,weight=1)

        self.enter_ip = tk.Entry(self.frame)
        self.enter_ip.configure(bg="#333333",fg="#FFFFFF")
        self.reboot_enter_ip = tk.Entry(self.frame)
        self.reboot_enter_ip.configure(bg="#333333",fg="#FFFFFF")
        self.ip_list = tk.Listbox(self.frame)
        self.search_np_enter_ip = tk.Entry(self.frame)
        self.search_np_enter_ip.configure(bg="#333333",fg="#FFFFFF")
        self.ip_list.configure(bg="#333333",fg="#FFFFFF")
        self.btn_add = tk.Button(self.frame, text="Add", command= lambda: self.fancy.add_to_list(self.enter_ip,self.ip_list))
        self.btn_add.configure(bg="#575757",fg="#FFFFFF", width=10)
        self.btn_check = tk.Button(self.frame, text="Check", command= lambda: self.fancy.ping_ip(self.ip_list))
        self.btn_check.configure(bg="#575757",fg="#FFFFFF", width=10)
        self.btn_reboot = tk.Button(self.frame, text="Start Rebooting", command= lambda: threading.Thread(target=self.fancy.reboot_ip,args=(self.reboot_enter_ip,),daemon=True).start())
        self.btn_reboot.configure(bg="#575757",fg="#FFFFFF", width=20)
        self.btn_search_np = tk.Button(self.frame, text="Start Rebooting", command= lambda: threading.Thread(target=self.fancy.search_NetworkPref,args=(self.search_np_enter_ip,),daemon=True).start())
        
    def run(self):
        self.frame.grid(row=0,column=0, sticky="nsew")
        self.enter_ip.grid(row=0,column=0, sticky="nsew")
        self.btn_add.grid(row=0,column=1, sticky="new")
        self.btn_check.grid(row=0,column=2,sticky="new")

        self.ip_list.grid(row=1,column=0, columnspan=3, sticky="nsew")

        self.reboot_enter_ip.grid(row=2,column=0,sticky="nsew")
        self.btn_reboot.grid(row=2,column=1,columnspan=2,sticky="sew")

        self.search_np_enter_ip.grid(row=3,column=0,sticky="nsew")
        self.btn_search_np.grid(row=3,column=1,columnspan=2,sticky="sew")

        self.root.mainloop()

App().run()
