import tkinter as tk
from tkinter import messagebox
import time
import threading
import keyboard
import mouse
import pygame
import os

pygame.init()
pygame.mixer.init()
current_dir = os.path.dirname(__file__)
assets_dir = os.path.join(current_dir, 'assets')
sfx = pygame.mixer.Sound(os.path.join(assets_dir, "main.wav"))
class AutoClicker:
    def __init__(self, master):
        self.master = master
        self.master.title("AutoClicker by Apathy")
        self.master.configure(bg='#2b2b2b') 
        icon_path = os.path.join(assets_dir, 'credit-card.ico')
        if os.path.exists(icon_path):
            self.master.iconbitmap(icon_path)
        self.is_on = False
        self.keybind = '`'
        self.delay = 0.1
        self.font_family = 'Poppins'
        self.keybind_label = tk.Label(master, text="Keybind(dont use command keys):", bg='#2b2b2b', fg='white', font=(self.font_family, 12))
        self.keybind_label.pack()
        self.keybind_entry = tk.Entry(master, bg='#434343', fg='white', font=(self.font_family, 12))
        self.keybind_entry.insert(0, self.keybind)
        self.keybind_entry.pack()
        self.delay_label = tk.Label(master, text="Delay (seconds):", bg='#2b2b2b', fg='white', font=(self.font_family, 12))
        self.delay_label.pack()
        self.delay_entry = tk.Entry(master, bg='#434343', fg='white', font=(self.font_family, 12))
        self.delay_entry.insert(0, str(self.delay))
        self.delay_entry.pack()
        self.start_button = tk.Button(master, text="Start", bg='#1f7bff', fg='white', font=(self.font_family, 10, 'bold'),
                                     command=self.start_autoclicker, relief=tk.FLAT)
        self.start_button.pack(pady=5, padx=10, ipadx=10)
        self.stop_button = tk.Button(master, text="Stop", bg='#ff3d3d', fg='white', font=(self.font_family, 10, 'bold'),
                                     command=self.stop_autoclicker, relief=tk.FLAT)
        self.stop_button.pack(pady=5, padx=10, ipadx=10)
        self.master.bind('<Return>', lambda event: self.start_button.invoke())
    def start_autoclicker(self):
        try:
            self.keybind = self.keybind_entry.get()
            self.delay = float(self.delay_entry.get())
            keyboard.add_hotkey(self.keybind, self.toggle_autoclicker)
            self.autoclicker_thread = threading.Thread(target=self.autoclicker)
            self.autoclicker_thread.daemon = True
            self.autoclicker_thread.start()
            messagebox.showinfo("Important!", f"Autoclicker started with keybind '{self.keybind}' and delay {self.delay} seconds.")
        except ValueError:
           messagebox.showerror("Error", "Please enter a valid delay (number).")

    def stop_autoclicker(self):
        self.is_on = False
        messagebox.showinfo("AutoClicker", "Autoclicker stopped.")
    def toggle_autoclicker(self):
        self.is_on = not self.is_on
        if self.is_on:
            sfx.play()
        print(f"Autoclicker {'enabled' if self.is_on else 'disabled'}")
    def autoclicker(self):
        while True:
            if self.is_on:
                mouse.click(button='left')
                time.sleep(self.delay)
            else:
                time.sleep(0.1)  
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClicker(root)
    root.geometry('600x500')
    root.mainloop()
