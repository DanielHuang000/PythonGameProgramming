#This is the program that check if people are in trouble base on if monkeys smile or not
#Please enter 1 if monkey a or b smile
#Please enter 0 if monkey a or b don't smile

import sys
print(sys.argv)

a_smile = sys.argv[1]
b_smile = sys.argv[2]

if (a_smile == '1' and b_smile == '1') or (not a_smile == '1' and not b_smile == '1'):
    print("We are in trouble")
if (a_smile == '1' and not b_smile == '1') or (not a_smile == '1' and b_smile == '1'):
    print("We are fine")

sys.exit()
