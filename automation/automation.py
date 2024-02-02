from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os, re, shutil

console = Console()

def create_folder(directory):
    
    while True:
        
        if not os.path.exists(directory):
            choice = Prompt.ask("Sorry friend, this directory doesn't exist. Would you like to make one in the current directory? Y/N :")
            if choice.lower() in ['y', 'yes']:
                os.makedirs(directory)
                console.print(f"Directory {directory} , created !")
            else:
                console.print("Canceled")
                return
            
        try:        
                
            files = os.listdir(directory)
            table = Table(title=f"Files here [bold yellow]{directory}[/bold yellow]")
            table.add_column("File Name", style="cyan")
            for file in files:
                table.add_row(file)
            
            console.print(table)
            
            choice = Prompt.ask("Would you like to make a folder in this directory? Y/N :")
            if choice.lower() in ['y', 'yes']:
                new_folder_name = Prompt.ask("Please enter the folder's name. :")
                new_folder_path = os.path.join(directory, new_folder_name)
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                    console.print(f"Folder '{new_folder_name}' created successfully.", style="bold green")
                else:
                    console.print(f"A folder with the name '{new_folder_name}' already exists.", style="bold yellow")
            else:
                console.print("No new folder created.\n")
                return
            
        except FileNotFoundError:
            console.print("Apologies, unable to find directory")
            return
        
def deleted_user():
    
    
    user_folder = r'assets\user-docs\user1'
    temp_folder = "assets\\user-docs\\user1Temp"
    
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
        print(f"Created Temporary folder at {temp_folder}.")
        
    try:
        for filename in os.listdir(user_folder):
            source = os.path.join(user_folder, filename)
            destination = os.path.join(temp_folder, filename)
            shutil.move(source, destination)
            print(f"Moved {filename} to {temp_folder}")
        print(f"All files from {user_folder} have been moved to {temp_folder}.")
        
    except FileNotFoundError:
        print(f"Unable to find filename, {user_folder}")
        return

def document_sort(source_directory):
    
    user_directory = os.path.join(source_directory, "user2")
    
    console.print(f"Target Directory, {user_directory}")
    
    log_directory = os.path.join(user_directory, "log")
    email_directory = os.path.join(user_directory, "mail")
    
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    if not os.path.exists(email_directory):
        os.makedirs(email_directory)
        
    log_pattern = re.compile(r'\.log\.txt$')
    email_pattern = re.compile(r'\.(email|mail)')
        
    for filename in os.listdir(user_directory):
        file_path = os.path.join(user_directory, filename)
        
        if os.path.isdir(file_path):
            continue
        
        if log_pattern.search(filename):
            shutil.move(file_path, log_directory)
            print(f"Moved {filename} to log folder.")
        elif email_pattern.search(filename):
            shutil.move(file_path, email_directory)
            print(f"Moved {filename} to mail folder.")

def log_file():
    pass
    

def main():
    
    console.print("Howdy Pardner")
    
    while True:
        console.print("\n1. Create folder\n2. Deleted Users\n3. Document Sorting\n4. Check Log File\n5. Exit")
        choice = Prompt.ask("What will it be pardner? : ", choices=['1', '2', '3', '4', '5'], default='5')
        
        try:
            
            if choice == '1':
                directory = Prompt.ask("Please input the directory.")
                create_folder(directory)
            elif choice == '2':
                deleted_user()
            elif choice == '3':
                source_directory = r'assets\user-docs'
                document_sort(source_directory)
            elif choice == '4':
                log_file()
            elif choice == '5':
                exit()
            else:
                console.print("Not sure what you did there but I'm going to keep you here")
        except ValueError:
            console.print("Why are you trying to be difficult, I'm just trying to help!")
        
    
main()