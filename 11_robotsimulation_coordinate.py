#!/usr/local/bin/python3

# Robot simulation program. Moving and finding final coordinates of a robot.

import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


coordinates = [0,0]

while True:
	input_char = getch()
	
	if input_char == "a":
		print("Left: A")
		coordinates[0] = coordinates[0] - 1
	elif input_char == "d":
		print("Right: D")
		coordinates[0] = coordinates[0] + 1
	elif input_char == "w":
		print("Up: W")
		coordinates[1] = coordinates[1] + 1
	elif input_char == "s":
		print("Down: S")
		coordinates[1] = coordinates[1] - 1
	else:
		print("Final corodinate: ", coordinates)
		exit()
	print("Current coordinate: ", coordinates)