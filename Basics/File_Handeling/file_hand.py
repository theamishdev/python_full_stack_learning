import os
# 1. Get input from the user
send_data = input("Enter the content to be added in file: ")
#imp:   with helps to open file without being need of closing the file.
# 2. Open in 'a' (append) mode to add data without deleting old content
with open("hello.txt", "a") as f:
    f.write(send_data + "\n")  # Added \n to start the next entry on a new line

# 3. Re-open in 'r' (read) mode to view the updated file
with open("hello.txt", "r") as f:
    data = f.read()
    print("Full file content:\n", data)
#user input
user_input=input("html data")
with open("index.html","a") as html_file:
    html_file.write(user_input)

check=os.path.exists("helllo.txt")
print(check)