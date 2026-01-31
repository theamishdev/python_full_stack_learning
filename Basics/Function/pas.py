isAdmin=False
password="Password"
def check():
    a=str(input("Enter the password"))
    global isAdmin
    global password
    if a==password:
        print("Password is correct. Welcome Admin")
        isAdmin=True
    else:
        print("Wrong password")

check()
print(isAdmin)