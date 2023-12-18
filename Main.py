import tkinter as tk
from tkinter import ttk

class VideoConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Видеоконвертер")
        self.master.config(bg="#333333")
        self.master.resizable(width=False, height=False)

        self.source_file_label = tk.Label(master, text="Выберите видеофайл:", bg="#333333", fg="white")
        self.source_file_label.grid(row=0, column=0, padx=2, pady=10, sticky="w")

        self.browse_button = tk.Button(master, text="Обзор", bg="white", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")