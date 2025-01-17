# Given a quadratic equation: ax^2 + bx + c = 0
# Find the roots of the equations.
# The exercise must have three user inputs to determine the equation:
# a, b, and c.

a = int(input("Coefficient a: "))
b = int(input("Coefficient b: "))
c = int(input("Coefficient c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + delta**(0.5))/(2*a)
    x2 = (-b - delta**(0.5))/(2*a)
    print(f"The solutions for this equation are: {x1} and {x2}")
elif delta == 0:
    x = (-b)/(2*a)
    print(f"The real solution for this equation is: {x}")
else:
    print("There are no real solutions for this equation.")
