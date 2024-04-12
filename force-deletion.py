# Created by Aditya Dwi Nugroho Friday, 09/10/2023
import shutil
import os
import subprocess

# Folder path and its content to delete
folder_path = r'C:\Users\aditg\Downloads\freedom.v1.11'

try:
    # shutil.rmtree to delete the folder and its contents
    shutil.rmtree(folder_path)
    print("Folder deleted successfully.")
except PermissionError as e:
    
    # Handle permission errors
    print(f"PermissionError: {e}")
    print("Some files or subfolders could not be deleted.")
    print("Continuing to delete other files and folders...")

    # os.remove to force delete individual files that are causing the permission error
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # subprocess to execute a command to delete the file :>
                subprocess.run(['cmd', '/c', 'del', '/F', '/Q', file_path], shell=True)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

    # Try deleting the folder again after attempting to force delete individual files
    try:
        shutil.rmtree(folder_path)
        print("Folder deleted successfully after attempting to force delete individual files.")
    except Exception as e:
        print(f"Failed to delete folder: {e}")
