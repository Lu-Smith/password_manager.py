pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + pwd)

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