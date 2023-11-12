import os
import shutil
import tkinter as tk
from tkinter import filedialog
def sort_files_by_extension(folder_path):
    script_folder = os.path.join(folder_path, "skrypty")
    image_folder = os.path.join(folder_path, "zdjecia")
    sound_folder = os.path.join(folder_path, "dziwek")
    document_folder = os.path.join(folder_path, "dokumenty")
    programs_folder = os.path.join(folder_path, "programy")

    for folder in [script_folder, image_folder, sound_folder, document_folder, programs_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)

        _, file_extension = os.path.splitext(file)

        if file_extension == ".py":
            destination_folder = script_folder
        elif file_extension in [".jpg", ".png", ".gif"]:
            destination_folder = image_folder
        elif file_extension in [".mp3", ".wav", ".ogg"]:
            destination_folder = sound_folder
        elif file_extension in [".pdf", ".docx", ".rtf", ".wpd" ".pptx"]:
            destination_folder = document_folder
        elif file_extension in [".exe", ".url", ".lnk",]:
            destination_folder = programs_folder
        else:
            continue

        destination_path = os.path.join(destination_folder, file)
        shutil.move(file_path, destination_path)
        print(f"Przeniesiono {file} do {destination_folder}")

if __name__ == "__main__":
    folder_to_sort = filedialog.askdirectory(title ="Podaj ścieżkę: ")
    sort_files_by_extension(folder_to_sort)

def wybierz_plik_i_katalog_wyjsciowy():
    katalog_wyjsciowy = filedialog.askdirectory()

    