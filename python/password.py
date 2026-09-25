password = ""

while password != "1234":
    password = input("Enter the password: ")
if password == "1234":
    print("Access granted")
else:
    print("Access denied")