import os
import shutil
import tkinter as tk
from tkinter import filedialog

def sort_files_by_extension(folder_path):
    # Define folder paths
    script_folder = os.path.join(folder_path, "skrypty")
    image_folder = os.path.join(folder_path, "zdjecia")
    sound_folder = os.path.join(folder_path, "dzwiek")
    document_folder = os.path.join(folder_path, "dokumenty")
    programs_folder = os.path.join(folder_path, "programy")
    archive_folder = os.path.join(folder_path, "archiwa")
    video_folder = os.path.join(folder_path, "filmy")
    photoshop_folder = os.path.join(folder_path, "photoshop")
    csv_folder = os.path.join(folder_path, "csv")
    iso_folder = os.path.join(folder_path, "iso")
    other_folder = os.path.join(folder_path, "inne")

    # Create folders if they don't exist
    for folder in [script_folder, image_folder, sound_folder, document_folder, programs_folder, archive_folder, video_folder, photoshop_folder, csv_folder, iso_folder, other_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # File extensions categories
    scripts = [".py", ".js", ".rb", ".pl", ".sh", ".bat", ".php", ".java", ".c", ".cpp", ".cs", ".go", ".r", ".swift", ".kt", ".ts", ".pb"]
    images = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".heic", ".jfif"]
    sounds = [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a", ".wma"]
    documents = [".pdf", ".docx", ".doc", ".rtf", ".txt", ".wpd", ".pptx", ".ppt", ".xls", ".xlsx", ".odt", ".ods", ".odp", ".epub", ".md", ".csv"]
    programs = [".exe", ".url", ".lnk", ".msi", ".bat", ".sh"]
    archives = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".msix"]
    videos = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"]
    photoshop_files = [".psd", ".psb"]
    iso_files = [".iso"]
    csv_files = [".csv"]

    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):  # Check if it's a file, not a directory
            _, file_extension = os.path.splitext(file)
            file_extension = file_extension.lower()  # Normalize to lowercase

            # Determine the destination folder
            if file_extension in scripts:
                destination_folder = script_folder
            elif file_extension in images:
                destination_folder = image_folder
            elif file_extension in sounds:
                destination_folder = sound_folder
            elif file_extension in documents:
                destination_folder = document_folder
            elif file_extension in programs:
                destination_folder = programs_folder
            elif file_extension in archives:
                destination_folder = archive_folder
            elif file_extension in videos:
                destination_folder = video_folder
            elif file_extension in photoshop_files:
                destination_folder = photoshop_folder
            elif file_extension in iso_files:
                destination_folder = iso_folder
            elif file_extension in csv_files:
                destination_folder = csv_folder
            else:
                destination_folder = other_folder

            # Move the file
            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)
            print(f"Przeniesiono {file} do {destination_folder}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_to_sort = filedialog.askdirectory(title="Podaj ścieżkę: ")
    if folder_to_sort:
        sort_files_by_extension(folder_to_sort)
