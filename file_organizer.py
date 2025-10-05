"""
File Organizer Script
=====================

This script scans a specified directory (default: ~/Downloads) and organizes files
into categorized subfolders based on file extensions.

Categories include:
    - Images (.jpg, .png, .gif, etc.)
    - Documents (.pdf, .docx, .txt, etc.)
    - Videos (.mp4, .mkv, etc.)
    - Music (.mp3, .wav, etc.)
    - Archives (.zip, .rar, etc.)
    - Executables (.dmg, .pkg, .exe, etc.)

Usage:
    Run the script to automatically sort files:
        $ python file_organizer.py

Author: Anish Parikh
Created: February 2025
"""
import os
import shutil

# Define the folder to organize (change this path as needed)
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Executables": [".dmg", ".pkg", ".app", ".exe"]
}

# Function to move files into respective folders
def organize_files():
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)

        if os.path.isfile(file_path):
            # Check file extension
            file_ext = os.path.splitext(filename)[1].lower()

            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    category_folder = os.path.join(DOWNLOADS_FOLDER, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved: {filename} ➝ {category}")
                    break

if __name__ == "__main__":
    organize_files()
    print("✅ Files organized successfully!")

