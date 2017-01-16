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
# ---\
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.\
\
# light_x: the X position of the light of power\
# light_y: the Y position of the light of power\
# initial_tx: Thor's starting X position\
# initial_ty: Thor's starting Y position\
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]\
\
thor_x, thor_y = initial_tx, initial_ty\
\
# game loop\
while 1:\
    remaining_turns = int(input())\
    \
    dx = "" #direction of x\
    dy = "" #direction of y\
    \
    # Moing toward location x and y 1 digit at the time until Thor reach the location\
    if thor_x > light_x:\
        dx = "W"\
        thor_x -= 1\
        \
    elif thor_x < light_x:\
        dx = "E"\
        thor_x += 1\
    \
    if thor_y > light_y:\
        dy = "N"\
        thor_y -= 1\
    \
    elif thor_y < light_y:\
        dy = "S"\
        thor_y += 1\
    \
    # A single line providing the move to be made: N NE E SE S SW W or NW\
    print(dy + dx)\
}