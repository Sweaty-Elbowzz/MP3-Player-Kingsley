import pygame
import tkinter as tk

window = tk.Tk()
window.geometry("300x200")
window.title("Song player")
tk.Label(window, text="", bg="lightblue").pack(fill="x")
tk.Label(window, text="", bg="lightgreen").pack(fill="both", expand=True)
tk.Label(window, text="", bg="lightpink").pack(fill="x")
button_row = tk.Frame(window)
button_row.pack(pady=10)
tk.Button(button_row, text="OK").pack(side="left", padx=5)
tk.Button(button_row, text="Cancel").pack(side="left", padx=5)
window.mainloop()
pygame.mixer.init()
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.mixer.music.set_volume(10)
