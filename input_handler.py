# Fungsi untuk input dan validasi data

from datetime import datetime,date, time
from report import write_csv

def get_pengeluaran(path):    
    while True:
        try: 
            now_formatted= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            kategori = input("Kategori : ")
            uang = int(input("Jumlah : "))
            deskripsi = input("Deskrpsi : ")
            out = (now_formatted, kategori, uang, deskripsi)
            pilih = input("Apakah data sudah benar? (y/n)")
            if pilih != 'y':
                print("Ketik ulang")
            else:            
                write_csv(path,out)
                break
        except ValueError:
            print("Kesalahan")    
