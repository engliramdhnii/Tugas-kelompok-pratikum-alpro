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

        # Mendefinisikan fungsi timer_belajar
    def buka_timer_belajar(self):
        # Jendela Timer Belajar
        jendela_timer = tk.Toplevel(self.root)
        jendela_timer.title("Timer Belajar")
        jendela_timer.geometry("300x200")

        # Label waktu
        label_waktu = tk.Label(jendela_timer, text="00:00", font=("Arial", 24))
        label_waktu.pack(pady=20)

        # Input durasi
        label_durasi = tk.Label(jendela_timer, text="Masukkan durasi (menit):")
        label_durasi.pack()
        input_durasi = tk.Entry(jendela_timer)
        input_durasi.pack()

        def mulai_timer():
            try:
                # Ambil durasi dari input
                menit = int(input_durasi.get())
                detik = menit * 60

                # Hitung mundur
                def hitung_mundur():
                    nonlocal detik
                    if detik > 0:
                        menit_tampil = detik // 60
                        detik_tampil = detik % 60
                        label_waktu.config(text=f"{menit_tampil:02d}:{detik_tampil:02d}")
                        detik -= 1
                        jendela_timer.after(1000, hitung_mundur)
                    else:
                        messagebox.showinfo("Selesai", "Waktu belajar habis!")
                hitung_mundur() # Mulai hitung mundur

            except ValueError:
                messagebox.showerror("Kesalahan", "Masukkan durasi yang valid!")

        # Tombol mulai
        tombol_mulai = tk.Button(jendela_timer, text="Mulai", command=mulai_timer)
        tombol_mulai.pack(pady=10)

    # Mendefinisikan fungsi catatan_harian
    def buka_catatan_harian(self):
        # Jendela Catatan Harian
        jendela_catatan = tk.Toplevel(self.root)
        jendela_catatan.title("Catatan Harian")
        jendela_catatan.geometry("400x300")

        # Area teks catatan
        area_catatan = tk.text(jendela_catatan, height = 10)
        area_catatan.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)

        def simpan_catatan():
            # Simpan catatan ke file
            with open("catatan_harian.txt", "w") as file:
                file.write(area_catatan.get("1.0", tk.END))
            messagebox.showinfo("Berhasil", "Catatan tersimpan!")
        
        # Tombol simpan
        tombol_simpan = tk.Button(jendela_catatan, text = "Simpan", command = simpan_catatan)
        tombol_simpan.pack(pady=10)
