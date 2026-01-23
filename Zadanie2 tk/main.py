import tkinter as tk
import subprocess
import threading
import time
import ipaddress

# ---------- HELPERS ----------
def is_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


# ---------- APP ----------
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("IP Checker / Rebooter")
        self.root.geometry("600x420")
        self.root.configure(bg="#2b2b2b")

        self.ip_list = []
        self.reboot_running = False

        # ---------- CHECK IP FROM LIST ----------
        frame_top = tk.Frame(root, bg="#4a4a4a", padx=10, pady=10)
        frame_top.pack(fill="x", padx=15, pady=15)

        tk.Label(
            frame_top, text="check ip from list",
            fg="white", bg="#4a4a4a", font=("Segoe UI", 12)
        ).pack(anchor="w")

        frame_input = tk.Frame(frame_top, bg="#4a4a4a")
        frame_input.pack(fill="x", pady=5)

        self.entry_ip_add = tk.Entry(
            frame_input, bg="#2f2f2f", fg="white",
            insertbackground="white"
        )
        self.entry_ip_add.pack(side="left", fill="x", expand=True, padx=(0, 10))

        tk.Button(
            frame_input, text="add",
            command=self.add_ip,
            bg="#2f2f2f", fg="white", relief="flat", padx=15
        ).pack(side="left", padx=5)

        tk.Button(
            frame_input, text="check ip's",
            command=self.check_ips,
            bg="#2f2f2f", fg="white", relief="flat", padx=15
        ).pack(side="left")

        self.text_ips = tk.Text(
            frame_top, height=10,
            bg="#2f2f2f", fg="white",
            insertbackground="white"
        )
        self.text_ips.pack(fill="both", expand=True, pady=10)

        # ---------- REBOOT ----------
        frame_bottom = tk.Frame(root, bg="#4a4a4a", padx=10, pady=10)
        frame_bottom.pack(fill="x", padx=15)

        tk.Label(
            frame_bottom, text="reboot IP",
            fg="white", bg="#4a4a4a", font=("Segoe UI", 12)
        ).pack(anchor="w")

        frame_reboot = tk.Frame(frame_bottom, bg="#4a4a4a")
        frame_reboot.pack(fill="x", pady=5)

        self.entry_reboot_ip = tk.Entry(
            frame_reboot, bg="#2f2f2f", fg="white",
            insertbackground="white"
        )
        self.entry_reboot_ip.pack(side="left", fill="x", expand=True, padx=(0, 10))

        tk.Button(
            frame_reboot, text="reboot IP",
            command=self.start_reboot,
            bg="#2f2f2f", fg="white", relief="flat", padx=20
        ).pack(side="left")

    # ---------- LOGIC ----------
    def add_ip(self):
        ip = self.entry_ip_add.get().strip()
        if not is_ip(ip):
            return

        if ip not in self.ip_list:
            self.ip_list.append(ip)
            self.text_ips.insert(tk.END, ip + "\n")

        self.entry_ip_add.delete(0, tk.END)

    def check_ips(self):
        thread = threading.Thread(target=self._check_ips)
        thread.daemon = True
        thread.start()

    def _check_ips(self):
        self.text_ips.delete(1.0, tk.END)

        with open("result.txt", "w") as out:
            for ip in self.ip_list:
                try:
                    subprocess.run(
                        ["ping", "-n", "1", ip],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        check=True
                    )
                    status = "ONLINE"
                except subprocess.CalledProcessError:
                    status = "OFFLINE"

                line = f"{ip} -> {status}\n"
                self.text_ips.insert(tk.END, line)
                out.write(line)

    def start_reboot(self):
        if self.reboot_running:
            return

        ip = self.entry_reboot_ip.get().strip()
        if not is_ip(ip):
            return

        self.reboot_running = True
        thread = threading.Thread(target=self.reboot_loop, args=(ip,))
        thread.daemon = True
        thread.start()

    def reboot_loop(self, ip):
        while True:
            subprocess.run(["ping", "-n", "1", ip],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            subprocess.run(["adb", "connect", ip])
            subprocess.run(["adb", "reboot"])
            time.sleep(300)


# ---------- START ----------
root = tk.Tk()
app = App(root)
root.mainloop()
