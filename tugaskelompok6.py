import tkinter as tk
from tkinter import messagebox
import time
import random

# Kelas utama aplikasi
class StudentProductivityToolkit:
    def __init__(self, root):

        # Pengaturan jendela utama
        self.root = root
        self.root.title("Student Productivity Toolkit")
        self.root.geometry("400x500")

        # Judul aplikasi
        judul = tk.Label(root, text="Student Productivity Toolkit", font=("Arial", 16))
        judul.pack(pady=20)

        # Tombol - tombol fitur
        tombol_timer = tk.Button(root, text="Timer Belajar", command=self.buka_timer_belajar, width=25)
        tombol_timer.pack(pady=10)

        tombol_catatan = tk.Button(root, text="Catatan Harian", command=self.buka_catatan_harian, width=25)
        tombol_catatan.pack(pady=10)

        tombol_tugas = tk.Button(root, text="To-Do List", command=self.buka_todo_list, width=25)
        tombol_tugas.pack(pady=10)

        tombol_kalkulator = tk.Button(root, text="Kalkulator Sederhana", command=self.buka_kalkulator, width=25)
        tombol_kalkulator.pack(pady=10)

        tombol_motivasi = tk.Button(root, text="Motivational Quote Generator", command=self.tampilkan_motivasi, width=25)
        tombol_motivasi.pack(pady=10)