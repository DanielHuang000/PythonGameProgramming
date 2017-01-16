{\rtf1\ansi\ansicpg950\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import sys\
import math\
\
# The while loop represents the game.\
# Each iteration represents a turn of the game\
# where you are given inputs (the heights of the mountains)\
# and where you have to print an output (the index of the mountain to fire on)\
# The inputs you are given are automatically updated according to your last actions.\
\
# game loop\
while True:\
    max = 0\
    nmax = 0\
    for i in range(8):\
        mountain_h = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.\
        if mountain_h > max:\
            max = mountain_h\
            nmax = i\
    print(nmax)\
            \
    # Write an action using print\
    # To debug: print("Debug messages...", file=sys.stderr)\
\
    # The index of the mountain to fire on.\
    #print("4")\
}