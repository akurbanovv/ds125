import math

"""
@author: Akhmad Kurbanov

This program gets two integers from the user and finds the first 
number, raised to the power of the second one and finds log base 
2 of the first number.
""" 

x = int(input("Enter number x: "))      
y = int(input("Enter number y: "))
print("x**y =", (x**y))
print("log(x) =", int(math.log2(x)))
