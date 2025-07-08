import os
import shutil

def organize_folder(path):
    if not os.path.exists(path):
        print("❌ Folder path not found!")
        return

    for file in os.listdir(path):
        filename, ext = os.path.splitext(file)
        ext = ext[1:].lower()  # remove dot

        if ext == '':
            continue  # skip files without extensions

        # Create folder if not exists
        folder = os.path.join(path, ext + "_files")
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Move the file
        shutil.move(os.path.join(path, file), os.path.join(folder, file))

    print("✅ Files organized successfully!")

# Example: Ask user for folder path
folder_path = input("Enter the full path of folder to organize: ")
organize_folder(folder_path)
