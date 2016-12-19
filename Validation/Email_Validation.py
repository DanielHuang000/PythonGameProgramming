import re

# get email information from users
email = input("Please enter an email address (EX: abc@gmail.com): ")

regex = r"(\w+[.|\w])*@(\w+[.])*(\w+)"

# a variable that returns None if the input doesn't match the format
check = re.search(regex, email)

# to check if the input of email match the require format
if check == None:
    print("This email is invalid")
else:
    print("This email is valid")
