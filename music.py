import pygame
import tkinter as tk

window = tk.Tk()
window.geometry("300x200")
window.title("Song player")

def songclick():
    list = tk.Frame(window)
    list.pack(pady=10)
    tk.Label(window, bg="white").pack(fill="x")
    tk.Label(window, bg="white").pack(fill="both", expand=True)
    tk.Label(window, bg="white").pack(fill="x")

    button_row = tk.Frame(window)
    button_row.pack(pady=10)

    tk.Button(button_row, text="Continue").pack(side="left", padx=5)
    tk.Button(button_row, text="Pause").pack(side="left", padx=5)
    window.mainloop()
    pygame.mixer.init()
    pygame.mixer.music.load()
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(10)

button_row = tk.Frame(window)
button_row.pack(pady=10)

tk.Button(button_row, text="Die For You - The Weeknd", command = songclick).pack(side="top", padx=5)
tk.Button(button_row, text="Continue").pack(side="bottom", padx=5)
tk.Button(button_row, text="Pause").pack(side= "bottom", padx=5)

tk.Label(window, bg = "white").pack(fill = "both")

window.mainloop()
