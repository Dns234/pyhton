from datetime import datetime,date, time
import csv

def pengeluaran():
    while True:
        out = ()
        kategori = input("Kategori : ")
        uang = int(input("Jumlah : "))
        deskripsi = input("Deskrpsi : ")
        out = (now_formatted, kategori, uang, deskripsi)
        print(out)
        pilih = input("Apakah data sudah benar? (y/n)")
        if pilih != 'y':
            print("Ketik ulang")
        else:
            transaksi.append(out)
            break
    print(transaksi)
             
now = datetime.now()
now_formatted= now.strftime("%Y-%m-%d")
print(now_formatted)
transaksi = []
total = 0
while True:
    print(70*"=")
    print("Selamat datang di Expanse Tracker")
    print("[1] Tambah pengeluaran")
    print("[2] Daftar pengeluaran")
    print("[3] Total pengeluaran")
    print("[4] Export CSV")
    print("[5] Keluar")
    while True:
        try:
            opt= int(input("Silahkan pilih menu: "))
            if opt in [1,2,3,4,5]:
                break
            else:
                print("Pilihanmu tidak ada, pilih antara 1,2,3,4,5")
        except ValueError:
            print("Pilihanmu tidak valid, masukkan angka")
    print(70*"=")
    if opt == 1:
        pengeluaran()
    elif opt == 2:
        print(20*"-", "List Pengeluaranmu hari ini", 20*"-")
        try:
            with open('output.csv', mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                
                # Print each row
                for row in csv_reader:
                    print(row)
        except FileNotFoundError:
            print("The file 'example.csv' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}") 


    elif opt == 3:
        jumlah = 0 
        for i in range(0,len(transaksi)):
            jumlah = jumlah + transaksi[i][2]
        print(f"Total Pengeluaranmu saat ini : Rp {jumlah}")
    elif opt == 4:
        # Save data to a CSV file
        filename = "output.csv"
        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(transaksi)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")
    elif opt == 5:
        print("Terimakaih sudah menggunakan aplikasi, jangan lupa cata pengeluaranmu!!")
        print(70*"=")
        break
        
       

    