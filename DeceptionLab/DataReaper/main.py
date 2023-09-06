import os
import random
import sys

def secureDelete(_path):
    try:
        # Check if the provided path is a file
        if os.path.isfile(_path):
            with open(_path, mode='wb') as file:
                size = os.path.getsize(_path)
                generate = bytearray(os.urandom(size))
                file.write(generate)
            os.remove(_path)
            print(f"File {_path} has been securely deleted.")
        # Check if the provided path is a directory
        elif os.path.isdir(_path):
            w_directory = input(f"Do you want to delete the entire directory {_path} including subfolders and files? (y/n): ")
            if w_directory.lower() == 'y':
                for root, folders, files in os.walk(_path):
                    for file in files:
                        secureDelete(os.path.join(root, file))
                print(f"Directory {_path} has been securely deleted, including its contents.")
            else:
                print(f"Directory {_path} hasn't been deleted.")
        else:
            print(f"Invalid path or file not found: {_path}")
    except (FileNotFoundError, PermissionError, FileExistsError, IOError) as e:
        print(e)
        exit()

def main():
    # Handle the command line arguments
    if '-h' in sys.argv:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Display usage instructions
        print("[==[Usage]==]\n\n> '-dir' : Specify a directory (e.g., C:\\Program Files\\Wireshark)\n> '-f'   : Provide a file.txt containing multiple directory paths")
    
    elif '-dir' in sys.argv:
        DIRECTORY_Index = sys.argv.index('-dir') + 1
        DIRECTORY = sys.argv[DIRECTORY_Index]
        DIRECTORY = os.path.abspath(DIRECTORY)
        DIRECTORY = rf"{DIRECTORY}"
        secureDelete(DIRECTORY)
        
    elif '-f' in sys.argv:
        if '-f' in sys.argv:
            FILE_Index = sys.argv.index('-f') + 1
            FILE = sys.argv[FILE_Index]
            with open(FILE, 'r') as f:
                data = [line.strip() for line in f.readlines()]
                for directory in data:
                    secureDelete(directory)
    else:  
        # No valid command-line arguments provided
        print('Please specify the directory or file.txt!')
        exit()

if __name__ == "__main__":
    main()
