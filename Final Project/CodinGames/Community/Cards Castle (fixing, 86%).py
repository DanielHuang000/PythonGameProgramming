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
A = []\
# A list of invalid sequence\
invalid = [".\\.","/.",".\\/"," \\.","./ ","\\./","//","\\\\"]\
valid = "/"\
inst = []\
h = int(input())\
for i in range(h):\
    s = []\
    s.append(input())\
    s = "".join(s)\
    A.append(s)\
    print(s, file=sys.stderr)\
#print(A)\
\
\
def checks(A, invalid):\
    check = None\
    for x in invalid:\
        for y in A:\
            if x in y:\
                check = False\
                return check\
            else :\
                check = True\
                continue\
    return check\
    \
def check1(A, valid, inst):\
    check = None\
    x = valid\
    inst = []\
    for y in A:\
        if x in y:\
            inst.append(1)\
            continue\
        else :\
            inst.append(0)\
    print(inst, file=sys.stderr)\
\
    return inst\
\
def check2(inst, h):\
    print(inst, file=sys.stderr)\
\
    x = 0\
    check = None\
    for i in inst:\
        if x == 0 and i == 0:\
            x+=0\
            check = True\
            continue\
        elif x==0 and i != 0:\
            x+=1\
            check = True\
            continue\
        elif x!=0 and i == 0:\
            check = False\
            return check\
        elif x!=0 and i != 0:\
            check = True\
            continue\
\
    return check\
        \
#print(check1(A,valid,inst))\
if checks(A, invalid) == True or check2(check1(A,valid,inst),h) == True:\
    print("STABLE")\
elif checks(A, invalid) == False or check2(check1(A,valid,inst),h) == False:\
    print("UNSTABLE")\
\
}