import os

#deletes files

#Current working dir
current_dir = os.getcwd()
file_ext = ".jpg"

for files in os.listdir(current_dir):
    if files.endswith(file_ext):
        print(files) #probably should add prompt, and error handling
        os.remove(files)
