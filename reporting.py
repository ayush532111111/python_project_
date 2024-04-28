import os
import shutil

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def copy_file_to_directory(source_file, destination_directory):
    shutil.copy(source_file, destination_directory)

def main():
    # Get the file path from the user
    file_path = input("Enter the path of the file you want to store: ")

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found!")
        return

    # Get the destination directory from the user
    destination_directory = input("Enter the path of the directory where you want to store the file: ")

    # Check if the destination directory exists, if not create it
    create_directory(destination_directory)

    # Extract the file name from the file path
    file_name = os.path.basename(file_path)

    # Copy the file to the destination directory
    copy_file_to_directory(file_path, destination_directory)

    print(f"File '{file_name}' has been successfully stored in '{destination_directory}'.")

if __name__ == "__main__":
    main()
