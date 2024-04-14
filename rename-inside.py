import os

# Path to direct
<<<<<<< HEAD
directory = 'C:\\Users\\aditg\\OneDrive\\Dokumen\\uploads'
=======
directory = 'C:\\Users\\aditg\\OneDrive\\Dokumen\\ProjectSekai'
>>>>>>> lazy/main

for filename in os.listdir(directory):
    if '-' in filename:
        #Rename - to ' ' will make space
        new_filename = filename.replace('-', ' ')
        
        # Construct full path of file
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_filename)
        
        # Rename file
        os.rename(src, dst)
