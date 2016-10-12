# 1. This program convert binary to a decimal number

bin = [2]
dec = 0
c = 0
T = sum(bin) >= len(bin)
bin = input('Enter only 1s and 0s (EX: 10111): ')
if T:
    for c in range(len(bin)-1,-1,-1):
        dec += int(bin[c])*(2**(len(bin)-1-c))
print('Decimal number is ' + str(dec))
