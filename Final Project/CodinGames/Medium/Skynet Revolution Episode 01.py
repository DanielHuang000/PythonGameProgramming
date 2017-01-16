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
# n: the total number of nodes in the level, including the gateways\
# l: the number of links\
# e: the number of exit gateways\
\
# Write an action using print\
# To debug: print("Debug messages...", file=sys.stderr)\
\
\
# Example: 0 1 are the indices of the nodes you wish to sever the link between\
    \
list = [] # Make the given data of two dots in list\
n, l, e = [int(i) for i in input().split()]\
for i in range(l):\
    # n1: N1 and N2 defines a link between these nodes\
    n1, n2 = [int(j) for j in input().split()]\
    list.append([n1,n2])\
\
exit = [] # Make the given number of gateway nodes into a list\
\
for i in range(e):\
    ei = int(input()) # the index of a gateway node\
    exit.append(ei)\
    \
# game loop\
while True:\
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn\
    d = False\
    a = 0\
    b = 0\
    \
    # Remove one of the closes link between gateway and agent\
    for e in exit:\
        if [e, si] in list or [si, e] in list:\
            if [e, si] in list:\
                list.remove([e, si])\
            else:\
                list.remove([si, e])\
            a = e\
            b = si\
            d = True\
            break\
\
    # Remove a random (the first) link in list if there are no links in between gateway and agent\
    if not d:\
        for x in list:\
            if si in x:\
                a = x[0]\
                b = x[1]\
                list.remove(x)\
                break\
    print(a, b)\
    }