import os
import shutil

# This automatically points to C:\Users\roliv\Downloads
target_dir = os.path.expanduser("~/Downloads")

extensions = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

for filename in os.listdir(target_dir):
    file_ext = os.path.splitext(filename)[1].lower()
    for folder, exts in extensions.items():
        if file_ext in exts:
            folder_path = os.path.join(target_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(os.path.join(target_dir, filename), os.path.join(folder_path, filename))