from datetime import datetime,date, time
from tabulate import tabulate
import csv
import os

def pengeluaran(path):
    while True:
        # out = ()
        while True:
            try: 
                now_formatted= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                kategori = input("Kategori : ")
                uang = int(input("Jumlah : "))
                deskripsi = input("Deskrpsi : ")
                out = (now_formatted, kategori, uang, deskripsi)
                break
            except Exception as e:
                print(f"Kesalahan di {e}")
                
        print(out)
        pilih = input("Apakah data sudah benar? (y/n)")
        if pilih != 'y':
            print("Ketik ulang")
        else:            
            filename = "expanse.csv"
            file_path = os.path.join(path, filename)
            file_exists = os.path.isfile(file_path)
            try:
                with open(file_path, mode="a", newline="", encoding="utf-8") as file:
                    if not os.path.exists(path):
                        os.mkdir(path)
                    writer = csv.writer(file)
                    #CSV HEADER
                    if not file_exists:
                        writer.writerow(['Tanggal','Kategori','Jumlah','Deskripsi'])
                    writer.writerow(out)
                print(f"Data {out} successfully saved to {filename}")
                break
            except Exception as e:
                print(f"An error occurred: {e}")        
        
def daftar_pengeluaran(file_path):
    data = []
    print(20*"-", "List Pengeluaranmu hari ini", 20*"-")
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print("The file 'example.csv' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}") 
    print(tabulate(data, headers="firstrow", tablefmt = "pipe"))
    
def total_pengeluaran(file_path):
    jumlah = 0 
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for i in csv_reader:
                if i[2] !='Jumlah':
                    jumlah += int(i[2])                    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    print(f"Total Pengeluaranmu saat ini : Rp {jumlah}")
    
def filter(file_path, kategori):
    # filtered= []
    try:
        with open(file_path, mode='r', newline='', encoding= 'utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if kategori in row:
                    print(row)
    except Exception as e:
        print(f"Required error : {e}")

transaksi = []
total = 0
path= "C:/Users/DANY/Pemrograman/python/Project_beginner/expanse_tracker"
filename = "expanse.csv"
file_path = os.path.join(path, filename)
while True:
    print(70*"=")
    print("Selamat datang di Expanse Tracker")
    print("[1] Tambah pengeluaran")
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
        pengeluaran(path)
    elif opt == 2:
        daftar_pengeluaran(file_path)
    elif opt == 3:
        total_pengeluaran(file_path)
    elif opt == 4:
        kategori = input("Filter apa? ")
        filter(file_path, kategori)
    elif opt == 5:
        print("Terimakaih sudah menggunakan aplikasi, jangan lupa cata pengeluaranmu!!")
        print(70*"=")
        break
        
       

    