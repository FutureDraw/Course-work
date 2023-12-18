import tkinter as tk
from tkinter import ttk

class VideoConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Видеоконвертер")
        self.master.config(bg="#333333")
        self.master.resizable(width=False, height=False)