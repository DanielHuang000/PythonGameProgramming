{\rtf1\ansi\ansicpg950\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sys\
import math\
\
# Auto-generated code below aims at helping you parse\
# the standard input according to the problem statement.\
\
n = int(input())  # the number of temperatures to analyse\
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526\
\
# Write an action using print\
# To debug: print("Debug messages...", file=sys.stderr)\
\
T = temps.split()\
x=5526\
n=0\
for i in T:\
    if x > abs(int(i)):\
        x = abs(int(i))\
        n = int(i)\
    elif x == abs(int(i)):\
        if n <= int(i):\
            n = int(i)\
        else:\
            continue\
        \
    print(x, file=sys.stderr)\
\
print(n)\
}