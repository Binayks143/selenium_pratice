import os

def list_files_in_directory(directory,substring):
    files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)) and substring in filename:
            files.append(filename)
    return files

directory = r"C:\Users\SC-229-USER\Desktop\Category_framework\ALL_TCs_Latest"
substring="17"
file_names = list_files_in_directory(directory,substring)
print("Files in directory:", file_names)
