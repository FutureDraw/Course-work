import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class VideoConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Видеоконвертер")
        self.master.config(bg="#333333")
        self.master.resizable(width=False, height=False)

        self.source_file_label = tk.Label(master, text="Выберите видеофайл:", bg="#333333", fg="white")
        self.source_file_label.grid(row=0, column=0, padx=2, pady=10, sticky="w")

        self.source_file_entry = tk.Entry(master, width=30)
        self.source_file_entry.grid(row=0, column=1, padx=0, pady=10, sticky="ew")

        self.browse_button = tk.Button(master, text="Обзор", bg="white", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4;*.avi;*.mpeg;*.mov;*.flv;*.webm;*.mkv")])

        if file_path:
            self.source_file_entry.delete(0, tk.END)
            self.source_file_entry.insert(0, file_path)
        else:
            messagebox.showinfo("Информация", "Выбор файла отменен.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverterApp(root)
    root.mainloop()