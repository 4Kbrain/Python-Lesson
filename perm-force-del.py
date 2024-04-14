import os

def force_delete_folder(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"File '{file_path}' deleted successfully.")
                except Exception as e:
                    print(f"Failed to delete file '{file_path}': {e}")

        for root, dirs, files in os.walk(folder_path, topdown=False):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    os.rmdir(dir_path)
                    print(f"Directory '{dir_path}' deleted successfully.")
                except Exception as e:
                    print(f"Failed to delete directory '{dir_path}': {e}")

        os.rmdir(folder_path)
        print(f"Folder '{folder_path}' deleted successfully.")
    except Exception as e:
        print(f"Failed to delete folder '{folder_path}': {e}")

folder_path = r'C:\Users\aditg\Downloads'
force_delete_folder(folder_path)
