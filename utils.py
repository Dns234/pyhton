# Fungsi tambahan seperti filter, format, dll
from tabulate import tabulate
import csv

def filter_kategori(file_path, kategori):
    filtered= []
    mini= kategori.lower()
    try:
        with open(file_path, mode='r', newline='', encoding= 'utf-8') as file:
            csv_reader = csv.reader(file)
            headers = ['Tanggal','Kategori','Jumlah','Deskripsi']
            for row in csv_reader:
                target = row[1].lower()
                if mini == target:
                    filtered.append(row)
            print(tabulate(filtered, headers=headers, tablefmt="fancy_grid"))
    except Exception as e:
        print(f"Required error : {e}")
