import os

def rename_files():
    #Get the file names
    file_names = os.listdir(r"C:\Users\ThomasMcD\Desktop\Udacity\prank")
    print(file_names)

    saved_dir = os.getcwd()
    os.chdir(r"C:\Users\ThomasMcD\Desktop\Udacity\prank")

    #Rename each filename
    for file_name in file_names:
        os.rename(file_name,file_name.translate(None, "0123456789"))

    os.chdir(saved_dir)

rename_files()
