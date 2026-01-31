from pathlib import Path

def create_folder():
    folder_name = input("Enter the name of the folder to create: ")
    try:
     print(f"Creating folder: {folder_name}") 
     p = Path(folder_name)
     p.mkdir() 
     print("Folder created successfully.")
    except Exception as err:
        print(f"Error: {err}")

def read_folders():
    try:
        p = Path("")
        itmes = list(p.rglob("*"))
        for idx, item in enumerate(itmes):
                print(f"{idx + 1}. {item.name}")
    except Exception as err:
        print(f"Error: {err}")

def delete_folder():
    read_folders()
    try:
        folder_name = input("Enter the name of the folder to delete: ")
        if (folder_name == "main.py"):
            print("You cannot delete main.py file")
            return
        p = Path(folder_name)
        p.rmdir()
        print("Folder deleted successfully.")
    except Exception as err:
        print(f"Error: {err}")

def update_folder():
    read_folders()
    try:
        old_name = input("Enter the current name of the folder: ")
        new_name = input("Enter the new name for the folder: ")
        p = Path(old_name)
        p.rename(new_name)
        print("Folder renamed successfully.")
    except Exception as err:
        print(f"Error: {err}")
        
print("Press 1 to create a new folder")
print("Press 2 to Real all folders")
print("Press 3 to delete a folder")
print("Press 4 to update a folder name")
print("Press 5 to exit")

user_input = int(input("Enter your choice: "))

if user_input == 1:
    create_folder()

elif user_input == 2:
    read_folders()

elif user_input == 3:
    delete_folder()

elif user_input == 4:
    update_folder()

elif user_input == 5:
    print("Exiting the program.")