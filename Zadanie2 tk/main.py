import tkinter as tk
import threading

from fancy_script import Fancy

def update_result( text_widget, value):
    text_widget.config(text=value)


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
        self.frame.columnconfigure(1,weight=1)
        self.frame.columnconfigure(2,weight=1)
        self.frame.columnconfigure(3,weight=1)
        self.frame.rowconfigure(3,weight=1)
        self.frame.grid(row=0,column=0, sticky="nsew")



    def IP_checker(self):
        self.IP_checker_txt = tk.Label(self.frame, text="----------------- IP Checker -----------------")
        self.IP_checker_txt.configure(bg="#1C3A4E", fg="#ffffff")
        self.IP_checker_txt.grid(row=0, column=0, columnspan=4, sticky="new", pady=5)

        self.input_ip = tk.Label(self.frame, text="input ip:")
        self.input_ip.configure(bg="#2b2b2b", fg="#ffffff")
        self.input_ip.grid(row=1, column=0, sticky="nsw", pady=5)

        self.ip_list = tk.Listbox(self.frame)
        self.ip_list.configure(bg="#252525",fg="#FFFFFF")
        self.ip_list.grid(row=3,column=0, columnspan=4, sticky="nsew",padx=5, pady=5)

        self.enter_ip = tk.Entry(self.frame)
        self.enter_ip.configure(bg="#252525",fg="#FFFFFF")
        self.enter_ip.bind("<Return>", lambda e: self.fancy.add_to_list(self.enter_ip,self.ip_list))
        self.enter_ip.grid(row=2,column=0, columnspan=2, sticky="nsew",padx=5, pady=5)

        self.btn_check = tk.Button(self.frame, text="Check", command= lambda: self.fancy.ping_ip(self.ip_list))
        self.btn_check.configure(bg="#575757",fg="#FFFFFF")
        self.btn_check.grid(row=2,column=2,sticky="new",padx=5, pady=5)

        self.btn_upload_from_file = tk.Button(self.frame, text="upload from file", command= lambda: self.fancy.get_from_file(self.ip_list))
        self.btn_upload_from_file.configure(bg="#575757",fg="#FFFFFF")
        self.btn_upload_from_file.grid(row=2,column=3,sticky="new",padx=5, pady=5)

    def IP_rebooter(self):
        self.IP_rebooter_txt = tk.Label(self.frame, text="----------------- IP rebooter -----------------")
        self.IP_rebooter_txt.configure(bg="#1C3A4E", fg="#ffffff")
        self.IP_rebooter_txt.grid(row=4, column=0, columnspan=4, sticky="new", pady=5)

        self.reboot_enter_ip = tk.Entry(self.frame)
        self.reboot_enter_ip.configure(bg="#252525",fg="#FFFFFF")
        self.reboot_enter_ip.grid(row=6,column=0,columnspan=3,sticky="nsew",padx=5, pady=5)

        self.reboot_input_ip = tk.Label(self.frame, text="input ip:")
        self.reboot_input_ip.configure(bg="#2b2b2b", fg="#ffffff")
        self.reboot_input_ip.grid(row=5, column=0, sticky="nsw", pady=5)

        self.reboot_btn = tk.Button(self.frame, text="Reboot IP", command= lambda: threading.Thread(target=self.fancy.reboot_ip,args=(self.reboot_enter_ip,),daemon=True).start())
        self.reboot_btn.configure(bg="#575757",fg="#FFFFFF", width=20)
        self.reboot_btn.grid(row=6,column=3, sticky="sew",padx=5, pady=5)

    def XML_checker(self):
        self.XML_checker_txt = tk.Label(self.frame, text="----------------- XML checker -----------------")
        self.XML_checker_txt.configure(bg="#1C3A4E", fg="#ffffff")
        self.XML_checker_txt.grid(row=7, column=0, columnspan=4, sticky="nsew", pady=5)

        self.search_xml_input_ip = tk.Label(self.frame, text="input ip:")
        self.search_xml_input_ip.configure(bg="#2b2b2b", fg="#ffffff")
        self.search_xml_input_ip.grid(row=8, column=0, sticky="nsw", pady=5)

        self.search_xml_enter_ip = tk.Entry(self.frame)
        self.search_xml_enter_ip.configure(bg="#252525",fg="#FFFFFF",)
        self.search_xml_enter_ip.grid(row=9,column=0, columnspan=3, sticky="nsew",padx=5, pady=5)

        self.search_xml_input_path = tk.Label(self.frame, text="input path to the file:")
        self.search_xml_input_path.configure(bg="#2b2b2b", fg="#ffffff")
        self.search_xml_input_path.grid(row=10, column=0, sticky="nsw", pady=5)

        self.search_xml_enter_path = tk.Entry(self.frame)
        self.search_xml_enter_path.configure(bg="#252525",fg="#FFFFFF")
        self.search_xml_enter_path.grid(row=11,column=0, columnspan=3, sticky="nsew",padx=5, pady=5)

        self.search_xml_enter_name = tk.Entry(self.frame)
        self.search_xml_enter_name.configure(bg="#252525",fg="#FFFFFF")
        self.search_xml_enter_name.grid(row=13,column=0, columnspan=3, sticky="nsew",padx=5, pady=5)

        self.search_xml_btn = tk.Button(self.frame, text="Search XML", command= lambda: threading.Thread(target=self.fancy.search_NetworkPref,
                                                                                                         args=(self.search_xml_enter_ip, 
                                                                                                               self.search_xml_enter_path, 
                                                                                                               self.search_xml_enter_name,
                                                                                                               lambda value: self.frame.after(
                                                                                                                    0,
                                                                                                                    lambda: update_result(self.search_xml_result, value))
                                                                                                               ),
                                                                                                               daemon=True
                                                                                                        ).start())
        self.search_xml_btn.configure(bg="#575757",fg="#FFFFFF")
        self.search_xml_btn.grid(row=9,column=3,sticky="new",padx=5, pady=5)

        self.search_xml_input_name = tk.Label(self.frame, text="input name:")
        self.search_xml_input_name.configure(bg="#2b2b2b", fg="#ffffff")
        self.search_xml_input_name.grid(row=12, column=0, sticky="nsw", pady=5)

        self.search_xml_input_result = tk.Label(self.frame, text="result:")
        self.search_xml_input_result.configure(bg="#2b2b2b", fg="#ffffff")
        self.search_xml_input_result.grid(row=12, column=3, sticky="nsw", pady=5)

        self.search_xml_result = tk.Label(self.frame)
        self.search_xml_result.configure(bg="#252525",fg="#FFFFFF")
        self.search_xml_result.config(state="disabled",height=1,width=3,)
        self.search_xml_result.grid(row=13,column=3,padx=5, sticky="new", pady=5)

    def IP_file_finder(self):
        self.IP_file_finder_txt = tk.Label(self.frame, text="----------------- File checker -----------------")
        self.IP_file_finder_txt.configure(bg="#1C3A4E", fg="#ffffff")
        self.IP_file_finder_txt.grid(row=14, column=0, columnspan=4, sticky="nsew", pady=5)

        self.IP_file_finder_input_ip = tk.Label(self.frame, text="input ip:")
        self.IP_file_finder_input_ip.configure(bg="#2b2b2b", fg="#ffffff")
        self.IP_file_finder_input_ip.grid(row=15, column=0, sticky="nsw", pady=5)

        self.IP_file_finder_enter_ip = tk.Entry(self.frame)
        self.IP_file_finder_enter_ip.configure(bg="#252525",fg="#FFFFFF",)
        self.IP_file_finder_enter_ip.bind("<Return>", lambda e: self.fancy.add_to_list(self.IP_file_finder_enter_ip,self.IP_file_finder_list_ip))
        self.IP_file_finder_enter_ip.grid(row=16,column=0, columnspan=3, sticky="nsew",padx=5, pady=5)

        self.IP_file_finder_input_path = tk.Label(self.frame, text="input path to the file:")
        self.IP_file_finder_input_path.configure(bg="#2b2b2b", fg="#ffffff")
        self.IP_file_finder_input_path.grid(row=18, column=0, sticky="nsw", pady=5)

        self.IP_file_finder_list_ip = tk.Listbox(self.frame)
        self.IP_file_finder_list_ip.configure(bg="#252525",fg="#FFFFFF")
        self.IP_file_finder_list_ip.grid(row=17,column=0, columnspan=4, sticky="nsew",padx=5, pady=5)

        self.IP_file_finder_enter_path = tk.Entry(self.frame)
        self.IP_file_finder_enter_path.configure(bg="#252525",fg="#FFFFFF")
        self.IP_file_finder_enter_path.grid(row=19,column=0, columnspan=3, sticky="nsew",padx=5, pady=5)

        self.IP_file_finder_input_file = tk.Label(self.frame, text="input path to the file:")
        self.IP_file_finder_input_file.configure(bg="#2b2b2b", fg="#ffffff")
        self.IP_file_finder_input_file.grid(row=20, column=0, sticky="nsw", pady=5)

        self.IP_file_finder_enter_name = tk.Entry(self.frame)
        self.IP_file_finder_enter_name.configure(bg="#252525",fg="#FFFFFF")
        self.IP_file_finder_enter_name.grid(row=21,column=0, columnspan=3, sticky="nsew",padx=5, pady=5)

        self.IP_file_finder_btn = tk.Button(self.frame, text="Search file", command= lambda: threading.Thread(target=self.fancy.search_File_based_ip,
                                                                                                         args=(self.IP_file_finder_list_ip, 
                                                                                                               self.IP_file_finder_enter_path, 
                                                                                                               self.IP_file_finder_enter_name,)
                                                                                                            ).start()
                                                                                                        )
        self.IP_file_finder_btn.configure(bg="#575757",fg="#FFFFFF")
        self.IP_file_finder_btn.grid(row=16,column=3,sticky="new",padx=5, pady=5)
    def run(self):
        App.IP_checker(self)
        App.IP_rebooter(self)
        App.XML_checker(self)
        App.IP_file_finder(self)

        print(type(self.search_xml_result))

        self.root.mainloop()

App().run()
