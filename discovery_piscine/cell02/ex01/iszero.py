#!/usr/bin/env python3

number = float(input("What is you like number (0-100) : "))

if number >= 1:
	print("This number is different from zero. ")
elif number >=  0:
	print("This number is both positive and negative. ")
elif number < 0:
	print("This number is negative.")
