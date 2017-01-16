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
surface_n = int(input())  # the number of points used to draw the surface of Mars.\
for i in range(surface_n):\
    # land_x: X coordinate of a surface point. (0 to 6999)\
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.\
    land_x, land_y = [int(j) for j in input().split()]\
\
# game loop\
while True:\
    # h_speed: the horizontal speed (in m/s), can be negative.\
    # v_speed: the vertical speed (in m/s), can be negative.\
    # fuel: the quantity of remaining fuel in liters.\
    # rotate: the rotation angle in degrees (-90 to 90).\
    # power: the thrust power (0 to 4).\
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]\
\
    # Write an action using print\
    # To debug: print("Debug messages...", file=sys.stderr)\
\
\
    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).\
    # print("0 3")\
    if abs(v_speed) > 39:\
        if power >= 0 and power <= 4:\
            power = 4\
        else:\
            continue\
    elif abs(v_speed) < 39:\
        power = 0\
    else:\
        power = 1\
        \
    if abs(rotate) > 8:\
        if rotate < 0:\
            rotate +=2\
        elif rotate > 0:\
            rotate -=2\
        \
    print(rotate,power)}