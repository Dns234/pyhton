  # Fungsi untuk menampilkan daftar dan total pengeluaran
  
from file_manager import file_exists,file_path
from tabulate import tabulate
import csv

def write_csv(path, content):
    filename = "expanse.csv"
    exists = file_exists(path, filename)
    join_file_path = file_path(path,filename)
    try:
        with open(join_file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            #CSV HEADER
            if not exists:
                writer.writerow(['Tanggal','Kategori','Jumlah','Deskripsi'])
            writer.writerow(content)
        print(f"Data {content} successfully saved to {filename}")
    except Exception as e:
        print(f"Kesalahan di {e}")


def daftar_pengeluaran(path, file_name):
    file_exists(path, file_name)
    join_file_path = file_path(path,file_name)
    data = []
    print(20*"-", "List Pengeluaranmu hari ini", 20*"-","\n")
    try:
        with open(join_file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
                # print(row)
            print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))
    except FileNotFoundError:
        print("Data kosong.")
    except Exception as e:
        print(f"An error occurred: {e}") 
    
def total_pengeluaran(path, csv_filename):
    file_exists(path, csv_filename)
    join_file_path = file_path(path,csv_filename)
    jumlah = 0     
    try:
        with open(join_file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for i in csv_reader:
                if i[2] !='Jumlah':
                    jumlah += int(i[2])                    
    except FileNotFoundError:
        print(f"The file '{join_file_path}' was not found.")
    print(f"Total Pengeluaranmu saat ini : Rp {jumlah}")
    
