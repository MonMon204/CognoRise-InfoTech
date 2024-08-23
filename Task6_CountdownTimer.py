#
#    Task6_CountdownTimer.py
#
# Created on Fri Aug 23 2024 1:18:14 PM
#       Author: Mina Waguih
#
# Description: A simple countdown timer using tkinter
#

import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Countdown Timer")
        self.label = tk.Label(self.root, text="Enter time:", font=("Helvetica", 24))
        self.label.pack()
        self.label = tk.Label(self.root, text="Min:", font=("Helvetica", 24))
        self.label.pack()
        self.mins_entry = tk.Entry(self.root, font=("Helvetica", 20))
        self.mins_entry.pack()
        self.label = tk.Label(self.root, text="Sec:", font=("Helvetica", 24))
        self.label.pack()
        self.secs_entry = tk.Entry(self.root, font=("Helvetica", 20))
        self.secs_entry.pack()
        self.button = tk.Button(self.root, text="Start", command=self.start_timer, font=("Helvetica", 24))
        self.button.pack()
        self.time_label = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.time_label.pack()

    def start_timer(self):
        try:
            self.time_in_min = int(self.mins_entry.get())
            self.time_in_sec = int(self.secs_entry.get())
            self.button.config(state="disabled")
            self.update_timer()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid time in seconds.")

    def update_timer(self):
        if self.time_in_min > 0 or self.time_in_sec > 0:
            while self.time_in_sec > 60:
                self.time_in_min += self.time_in_sec // 60
                self.time_in_sec = self.time_in_sec % 60
            

            self.time_label.config(text=f"{self.time_in_min:02d}:{self.time_in_sec:02d}")

            if self.time_in_sec == 0:
                self.time_in_min -= 1
                self.time_in_sec = 59
            else:
                self.time_in_sec -= 1 
            
            self.root.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Time's up!")
            self.button.config(state="normal")

    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    timer = CountdownTimer()
    timer.run()