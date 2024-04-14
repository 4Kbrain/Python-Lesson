import os

# Path to dir
directory = 'C:\\Users\\aditg\\OneDrive\\Dokumen\\ProjectSekai'


# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.startswith('-'):
        # Construct new file name to rename
        new_filename = filename.replace('-', '_',1)
        
        # Construct full path of file
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_filename)
        
        # Rename file :DDD
        os.rename(src, dst)
