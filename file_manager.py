# Fungsi untuk baca/tulis file CSV
import csv
import os

def file_path(path, file_name):
    filepath = os.path.join(path, file_name)
    return filepath

def file_exists(path, file_name):
    join_filepath = file_path(path, file_name)
    file_exists = os.path.isfile(join_filepath)
    if not file_exists:
        print("File Tidak ada")
        return False
    else:
        return True
    