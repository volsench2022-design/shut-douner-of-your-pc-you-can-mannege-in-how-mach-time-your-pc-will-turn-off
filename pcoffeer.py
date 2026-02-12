import tkinter as tk
from tkinter import messagebox
import os

timer_running = None

def run_command(cmd_type):
    global timer_running

    try:
        seconds = int(entry_time.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid time")
        return
    
    if cmd_type == "shutdown":
        if messagebox.askyesno("Confirm", f"Are you sure you want to shutdown the computer in {seconds} seconds?"):
            os.system(f"shutdown /s /t {seconds}")
            start_ui_countdown(seconds)

    elif cmd_type == "restart":
        os.system(f"shutdown /r /t {seconds}")
        start_ui_countdown(seconds)

    elif cmd_type == "cancel":
        os.system("shutdown /a")
        if timer_running:
            root.after_cancel(timer_running)
        label_countdown.config(text="Operation cancelled", fg="white")
        messagebox.showinfo("Cancelled", "Shutdown/Restart operation has been cancelled.")

def start_ui_countdown(time_left):
    global timer_running
    if time_left > 0:
        label_countdown.config(text=f"Time remaining: {time_left} seconds", fg="green")
        timer_running = root.after(1000, start_ui_countdown, time_left - 1)
    else:
        label_countdown.config(text="Executing command now!", fg="white")

def open_folder():
    os.startfile(os.getcwd())

root = tk.Tk()
root.title("Shutdown/Restart Scheduler")
root.geometry("400x350")
root.config(bg="black")

tk.Label(root, text="System Shutdown Timer", font=("Courier", 20, "bold"),
         bg="black", fg="green").pack(pady=20)
tk.Label(root, text="Enter time in seconds:", bg="black", fg="white").pack()
entry_time = tk.Entry(root, font=("Arial", 14), justify="center", width=10)
entry_time.insert(0, "60")
entry_time.pack(pady=10)

label_countdown = tk.Label(root, text="Timer not running", font=("Arial", 12),
                           bg="#1a1a1a", fg="gray")
label_countdown.pack(pady=10)

btn_style = {"width": 25, "height": 2, "font": ("Arial", 10, "bold")}

tk.Button(root, text="Shutdown", bg="#c0392b", fg="white",
          command=lambda: run_command("shutdown"), **btn_style).pack(pady=5)
tk.Button(root, text="Restart", bg="#d35400", fg="white",
          command=lambda: run_command("restart"), **btn_style).pack(pady=5)
tk.Button(root, text="Open Project Folder", bg="#2980b9", fg="white",
          command=open_folder, **btn_style).pack(pady=5)
tk.Button(root, text="Cancel", bg="#27ae60", fg="white",
          command=lambda: run_command("cancel"), **btn_style).pack(pady=20)

info_text = f"User: {os.getlogin()}\nOS: {os.name}"
tk.Label(root, text=info_text, bg="#1a1a1a", fg="#555", font=("Arial", 8)).pack(side="bottom")

root.mainloop()