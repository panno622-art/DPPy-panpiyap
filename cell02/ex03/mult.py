#!/usr/bin/env python3

f_number = int(input("first number : "))
secorn_number = int(input("secorn number : "))

mult = f_number * secorn_number 

print(f_number, "x", secorn_number, "=", mult,)

if mult > 0:
  print("The result is positive")

elif mult < 0:
  print("The result is negative.")

else:
  print("The result is positive and negative.")
