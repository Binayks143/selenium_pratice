import os
"""
os.path.join(directory, filename): This function joins the directory path and the filename to 
create a complete file path.

os.path.isfile(): This function checks whether the path passed to it points to a regular 
file (not a directory). It returns True if the path points to a file, and False otherwise.
"""
def list_files_in_directory(directory):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files

directory = r"C:\Users\SC-229-USER\Desktop\Category_framework\ALL_TCs_Latest"
file_names = list_files_in_directory(directory)
print("Files in directory:", file_names)
