import os
def display_folder(path):
    items=os.listdir(path)

    for item in items:
        full_path=os.path.join(path,item)

        if os.path.isfile(full_path):
            print("File:", item)

        elif os.path.isdir(full_path):    
            print("Directory:", item)
            display_folder(full_path)

folder_path = input("Enter folder path:")

if os.path.exists(folder_path):
    display_folder(folder_path)
else:
    print("Invalid folder path")