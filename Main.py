import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from moviepy.editor import VideoFileClip
from tkinter import ttk
import shutil
from pathlib import Path

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

    def convert_video(self):
        source_file = self.source_file_entry.get()

        if not source_file:
            messagebox.showerror("Ошибка", "Выберите исходный видеофайл")
            return

        try:
            script_dir = Path(sys._MEIPASS) if getattr(sys, 'frozen', False) else Path(
                os.path.dirname(os.path.realpath(__file__)))

            temp_file_name = script_dir / Path(f"temp_video_{Path(source_file).stem}.mp4")

            clip = VideoFileClip(source_file)
            clip.write_videofile(str(temp_file_name), codec="libx264", audio_codec="aac")

            clip.close()

            output_folder = filedialog.askdirectory()
            if not output_folder:
                messagebox.showerror("Ошибка", "Выберите папку для сохранения")
                return

            selected_codec = self.codec_var.get()
            output_file_name = simpledialog.askstring('Название файла', 'Введите название файла')
            if not output_file_name:
                messagebox.showerror("Ошибка", "Введите название файла")
                return

            output_file = Path(output_folder) / Path(f"{output_file_name}.{selected_codec}")

            shutil.move(str(temp_file_name), str(output_file))

            messagebox.showinfo("Успех", "Видео успешно сконвертировано!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoConverterApp(root)
    root.mainloop()