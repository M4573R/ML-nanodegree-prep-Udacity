import os


def rename_files():
    # 1. get all file names from a folder
    file_list = os.listdir(r"C:\Users\Lenovo\Pictures\Udacity\prank\prank")
    saved_path = os.getcwd()
    print saved_path
    os.chdir(r"C:\Users\Lenovo\Pictures\Udacity\prank\prank")
     #2. for each file, rename filename
    for file_name in file_list:
       os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(r"C:\Python27")

rename_files()
