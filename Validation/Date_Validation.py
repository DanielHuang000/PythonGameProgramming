import re

# get date information from users
date = input("Please enter a correct date (EX: 2016-12-15): ")

regex = r"(\d{4})*-(\d{2})*-(\d{2})"

# a variable that returns None if the input doesn't match the format
check = re.search(regex, date)

# check if the input of date match the require format
if check == None:
    print("The date is invalid")
else:
    print("The date is valid")

