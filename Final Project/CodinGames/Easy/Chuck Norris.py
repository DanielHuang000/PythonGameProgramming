{\rtf1\ansi\ansicpg950\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sys\
import math\
# Auto-generated code below aims at helping you parse\
# the standard input according to the problem statement.\
\
message = input()\
\
# Write an action using print\
# To debug: print("Debug messages...", file=sys.stderr)\
# change message into binary\
string = ''\
for x in message:\
    # get an extra 0 in each numbers or signs \
    if x.isalpha()==False:    \
        string += '0'+''.join(format(ord(x), 'b'))\
    else:\
        string += ''.join(format(ord(x), 'b'))\
\
lists = list(string)\
# set a variable for the starting value\
var = ''\
# coding numbers into 0s\
for i in lists:\
    if var =='' and i =='1':\
        print("0 ",end='0')\
        var = i\
    elif var =='' and i =='0':\
        print("00 ",end='0')\
        var = i\
    elif var =='1' and i =='1':\
        print("0",end='')\
        var = i\
    elif var =='1' and i =='0':\
        print(" 00 ",end='0')\
        var = i\
    elif var =='0' and i =='1':\
        print(" 0 ",end='0')\
        var = i\
    elif var =='0' and i =='0':\
        print("0",end='')\
        var = i}