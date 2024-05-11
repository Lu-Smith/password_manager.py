pwd = input("What is the master password? ").lower()

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + pwd + "\n")


if pwd == "cat":
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
    print("Wrong manster password, try again.")