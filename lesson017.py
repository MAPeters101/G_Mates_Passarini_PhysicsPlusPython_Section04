# Given a quadratic equation: ax^2 + bx + c = 0
# Find the roots of the equations.
# The exercise must have three user inputs to determine the equation:
# a, b, and c.
import math
a = float(input("Please enter the value for a: "))
b = float(input("Please enter the value for b: "))
c = float(input("Please enter the value for c: "))

delta = b*b - 4*a*c

if delta > 0:
    root1 = (-b + math.sqrt(delta))/(2*a)
    root2 = (-b - math.sqrt(delta))/(2*a)
    print(f"The two roots are: {root1} and {root2}")
elif delta == 0:
    root = (-b)/(2*a)
    print(f"The 1 root is: {root}")
else:
    print("There are no real roots.")
