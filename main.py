from input_handler import get_pengeluaran
from report import daftar_pengeluaran, total_pengeluaran
from utils import filter_kategori
from datetime import datetime,date, time
from tabulate import tabulate
import csv
import os

transaksi = []
total = 0
path= "C:/Users/DANY/Pemrograman/python/Project_beginner/expanse_tracker"
csv_filename = "expanse.csv"
file_path = os.path.join(path, csv_filename)
while True:
    print(70*"=")
    print("Selamat datang di Expanse Tracker\n")
    daftar_pengeluaran(path, csv_filename)    
    print("\n[1] Tambah pengeluaran")
    print("[2] Daftar pengeluaran")
    print("[3] Total pengeluaran")
    print("[4] filter pengeluaran")
    print("[5] Keluar")
    while True:
        try:
            opt= int(input("Silahkan pilih menu: "))
            if opt in [1,2,3,4,5]:
                break
            else:
                print("Pilihanmu tidak ada, pilih antara 1,2,3,4")
        except ValueError:
            print("Pilihanmu tidak valid, masukkan angka")
    print(70*"=")
    if opt == 1:
        get_pengeluaran(path)
    elif opt == 2:
        daftar_pengeluaran(path, csv_filename)
    elif opt == 3:
        total_pengeluaran(path, csv_filename)
    elif opt == 4:
        kategori = input("kategori ? ")
        filter_kategori(file_path, kategori)
    elif opt == 5:
        print("Terimakaih sudah menggunakan aplikasi, jangan lupa cata pengeluaranmu!!")
        print(70*"=")
        break
        
       

    