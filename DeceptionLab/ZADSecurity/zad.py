import os
import re
import time
import random
import base64
import string
from cryptography.fernet import Fernet, InvalidToken

class ZADSECURITY():
    def guide(self):
        print("""Usage Instructions:

1. [Options]:
   - Enter `1` to encrypt data.
   - Enter `2` to decrypt data.
   - Enter any other number to access the guide.

2. [Encryption]:
   - If you choose option `1` to encrypt, you will be prompted to enter the data you want to encrypt and a security key.
   - The script will then encrypt the data using Fernet encryption and save it to a file named `_encrypted.enc`.

3. [Decryption]:
   - Select option `2` to decrypt.
   - Enter the encrypted text when prompted, followed by the security key (secret key) used for encryption.
   - The script will decrypt the provided data and display the decrypted text.
""")
    
    # Read binary data from a file
    def read_binary(self, _dir):
        with open(_dir, 'rb') as f:
            data = f.read()
            return data
        
    def ZAD(self, _data:str, _key:str, _command:['enc', 'dec']):
        # Using key as seed
        random.seed(_key)
        # Generate Key: 123AbC
        random_key = "".join(random.choices(string.ascii_lowercase+string.ascii_letters+string.digits+string.ascii_uppercase, k=32))
        # Convert random_key to bytes: b'123AbC'
        randome_key_bytes = random_key.encode('utf-8')
        # Convert bytes value to Base64
        key_base = base64.urlsafe_b64encode(randome_key_bytes)
        fernet = Fernet(key_base)

        if _command == "enc":
            __data = fernet.encrypt(_data)
        else:
            __data = fernet.decrypt(_data).decode()
        return __data
        
    def main(self):
        option = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mOption\033[32;1m]\n\033[32;1m└─$\033[0m ")
        # ENCRYPTION
        count = 0
        if option == '1':
            en_option = input("""
\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mSelect-The-Data-Source\033[32;1m]
│
│   \033[37;1m[1] Import from a file\033[32;1m
│   \033[37;1m[2] Enter text manually\033[32;1m
│
\033[32;1m└─$\033[0m """)
            if en_option == '1':
                directory = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mEnter-Directory\033[32;1m]\n\033[32;1m└─$\033[0m ")
                directory.replace('"', '').replace("'", '')
                if os.path.exists(directory):
                    key = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mSecurity-Key\033[32;1m]\n└─$\033[0m ")
                    # Encrypt a single file
                    if os.path.isfile(directory):
                        text = self.read_binary(directory)
                        enc_data = self.ZAD(text, key, 'enc')
                        file_name = os.path.basename(directory)
                        enc_time = time.strftime("%Y%m%d%H%M%S")
                        with open(f'{file_name}_-{enc_time}-_.enc', 'wb') as ef:
                            ef.write(enc_data)
                        print(f'\r{file_name}')
                        exit()
                    # Encrypt a directory
                    else:
                        for root, folders, files in os.walk(directory):
                                for file in files:
                                    _, extension = os.path.splitext(file)
                                    if extension != '.enc':
                                        count += 1
                                        file_ = os.path.join(root, file)
                                        text = self.read_binary(file_)
                                        enc_data = self.ZAD(text, key, 'enc')
                                        file_name = os.path.basename(file)
                                        enc_time = time.strftime("%Y%m%d%H%M%S")
                                        with open(f'{file_name}_-{enc_time}{count}-_.enc', 'wb') as ef:
                                            ef.write(enc_data)
                                        print(f'\r{file_}')
                    
                    print(f"\n\r\033[32;1m{count} Successfully Encrypted!")
                    exit()
            
            # Encrypt text
            elif en_option == '2':
                text = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mEnter-Data-to-Encrypt\033[32;1m]\n\033[32;1m└─$\033[0m  ").encode('utf-8')
                key = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mSecurity-Key\033[32;1m]\n└─$\033[0m ")
                enc_time = time.strftime("%Y%m%d%H%M%S")
                enc_data = self.ZAD(text, key, 'enc')
                with open(f'_-{enc_time}-_.enc', 'wb') as ef:
                    ef.write(enc_data)
                print(f"\n\r\033[32;1mFile exported as {enc_time}.enc")
                exit()
            
  
        # DECRYPTION    
        elif option == '2':
            de_option = input("""
\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mSelect-The-Data-Source\033[32;1m]
│
│   \033[37;1m[1] Import from a file\033[32;1m
│   \033[37;1m[2] Enter text manually\033[32;1m
│
\033[32;1m└─$\033[0m """)
            if de_option == '1':
                directory = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mEnter-Directory\033[32;1m]\n\033[32;1m└─$\033[0m ")
                directory.replace('"', '').replace("'", '')
                try:
                    if os.path.exists(directory):
                        key = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mSecret-Key\033[32;1m]\n└─$\033[0m ")
                        # Decrypt a single file
                        if os.path.isfile(directory):
                            text = self.read_binary(directory)
                            dec_data = self.ZAD(text, key, 'dec')
                            file_name = os.path.basename(directory)
                            reg_exp = re.compile(r'_(.*?)\.enc')
                            new_file_name = re.sub(reg_exp, '', file_name)
                            random_digit = random.randrange(100, 999)
                            if new_file_name == '':
                                new_file_name = f"Output{random_digit}"
                            with open(f'{new_file_name}', 'w') as ef:
                                ef.write(dec_data)
                            print(f'\r{new_file_name}')
                            exit()
                        # Decrypt a directory (Only .enc files)
                        else:
                            for root, folders, files in os.walk(directory):
                                for file in files:
                                    _, extension = os.path.splitext(file)
                                    if extension == '.enc':
                                        count += 1
                                        file_ = os.path.join(root, file)
                                        text = self.read_binary(file_)
                                        dec_data = self.ZAD(text, key, 'dec')
                                        file_name = os.path.basename(directory)
                                        reg_exp = re.compile(r'_(.*?)\.enc')
                                        new_file_name = re.sub(reg_exp, '', file_name)
                                        if new_file_name == '':
                                            new_file_name = f"Output{count}"
                                        with open(f'{new_file_name}{count}', 'w') as ef:
                                            ef.write(dec_data)
                                        print(f'\r{new_file_name}')
                        
                        print(f"\n\r\033[32;1m{count} Successfully Decrypted!")
                        exit()
                    
                except InvalidToken:
                    print("\033[31mInvalid Key!\033[0m")
            # Decrypt text
            elif de_option == '2':
                text = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mEnter-Data-to-Decrypt\033[32;1m]\n\033[32;1m└─$\033[0m  ").encode('utf-8')
                key = input("\n\033[32;1m┌──(\033[38;2;184;0;0mZAD\033[32;1m)-[\033[34;1mSecurity-Key\033[32;1m]\n└─$\033[0m ")
                dec_time = time.strftime("%Y%m%d%H%M%S")
                dec_data = self.ZAD(text, key, 'dec')
                with open(f'_-{dec_time}-_.txt', 'w') as ef:
                    ef.write(dec_data)
                print(f"\n\r\033[32;1mFile exported as {dec_time}.txt")
                exit()
        
        elif option == '3':
            self.guide()       
        else:
            print("\033[31mInvalid Option!\033[0m")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
\033[38;2;139;0;0m███████╗░█████╗░██████╗░  ░██████╗███████╗░█████╗░██╗░░░██╗██████╗░██╗████████╗██╗░░░██╗\033[0m
\033[38;2;154;0;0m╚════██║██╔══██╗██╔══██╗  ██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██║╚══██╔══╝╚██╗░██╔╝\033[0m
\033[38;2;169;0;0m░░███╔═╝███████║██║░░██║  ╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝██║░░░██║░░░░╚████╔╝░\033[0m
\033[38;2;184;0;0m██╔══╝░░██╔══██║██║░░██║  ░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██║░░░██║░░░░░╚██╔╝░░\033[0m
\033[38;2;199;0;0m███████╗██║░░██║██████╔╝  ██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║██║░░░██║░░░░░░██║░░░\033[0m
\033[38;2;214;0;0m╚══════╝╚═╝░░╚═╝╚═════╝░  ╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░░░░╚═╝░░░\033[0m
\n\n''')
    print("""\033[91mUse the numbers to select an option.\033[37;1m
[1] Encrypt
[2] Decrypt
[3] Help
""")
    app = ZADSECURITY()
    app.main()