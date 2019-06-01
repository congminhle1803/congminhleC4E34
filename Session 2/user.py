
username = input("Please input username: ")

if username == "C4E":
    password = input("Please input password: ")
    
    if password == "codethechange":
        print("Welcome",username)
    else:
        print("Wrong password")
else:
    print("Not found")