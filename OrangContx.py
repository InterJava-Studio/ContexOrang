import customtkinter as ctk
import subprocess
import time
def restart_explorer():
    subprocess.run(["taskkill", "/f", "/im", "explorer.exe"])
    time.sleep(1)
    subprocess.run("start explorer.exe", shell=True)
def switch_to_old():
    subprocess.run(["reg", "add", "HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\\InprocServer32", "/f", "/ve"])
    restart_explorer()
def switch_to_new():
    subprocess.run(["reg", "delete", "HKCU\\Software\\Classes\\CLSID\\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}", "/f"])
    restart_explorer()
app = ctk.CTk()
app.geometry("237x180")
app.title("ContxOrang")
frame = ctk.CTkFrame(master=app)
frame.pack(pady=10, padx=20, fill="both", expand=True)
label = ctk.CTkLabel(master=frame, text="Made By InterJava's Projects")
label.pack(pady=1, padx=1)
label = ctk.CTkLabel(master=frame, text="Switch Context Menu To")
label.pack(pady=6, padx=5)
old_button = ctk.CTkButton(master=frame, text="Windows Legacy", command=switch_to_old, fg_color="orange", hover_color="darkorange")
old_button.pack(pady=6, padx=5)
new_button = ctk.CTkButton(master=frame, text="Windows 11", command=switch_to_new, fg_color="orange", hover_color="darkorange")
new_button.pack(pady=6, padx=5)
app.mainloop()