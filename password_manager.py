from cryptography.fernet import Fernet

master_pwd = input("What is the master password? ").lower()

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, password = data.split("|")
                print("User:", user, "- Password: ", password)
            else:
                print("Invalid data format:", data)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + pwd + "\n")


if master_pwd  == "cat":
    while True:
        mode = input("Would you like to add a new password or view existing ones? (Type: Add/View or Q  to quit) ").lower()

        if mode == "q":
            break

        if mode == "view": 
            view()
        elif mode == "add":
            add()
        else: 
            print("Invalid mode.")
            continue
else:
    print("Wrong master password, try again.")