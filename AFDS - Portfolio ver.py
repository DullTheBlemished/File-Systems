import os
import time

name_of_full_folder_thingymabob = 0
things_to_checkychecky = ["Desktop", "Documents", "Downloads"]
empty_folders = []
path = 0
extirminated_files = []

input("Welcome to the AFDS, by Hung, press 'ENTER' to continue")
os.system("cls")

id = input("Enter your student id:").strip()
input("This program will remove all empty folders in your Documents, Downloads and Desktop. 'ENTER' to continue")
os.system("cls")

input("!!! AS OF CURRENTLY i am not able to gaurentee that the program will work AS INTENDED. Use sparingly, and at you own risk! - Hung !!! 'ENTER' to continue")
for skibidi in things_to_checkychecky:
    if skibidi == "Downloads":
        path =fr"C:\Users\{id}\{skibidi}"
    else:
        path = (fr"C:\Users\{id}\OneDrive - Caroline Chisholm Catholic College\{skibidi}")

    for root, dirs, files in os.walk(fr"{path}", followlinks=True, topdown=False):
        for name in dirs:
            name_of_full_folder_thingymabob = fr"{root}\{name}"

            try:
                    os.rmdir(name_of_full_folder_thingymabob)
                    extirminated_files.append(name)
            except:
                    pass 
 
print(f"The AFDS program has removed the following folders: {extirminated_files}")
print("Made by Hung")
input("'ENTER' to exit the program")