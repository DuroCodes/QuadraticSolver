import math

# get the coefficients from the user
a = float(input("Please enter coefficient a: "))
b = float(input("Please enter coefficient b: "))
c = float(input("Please enter coefficient c: "))

discRoot = math.sqrt((b * b) - 4 * a * c) # first pass
root1 = (-b + discRoot) / (2 * a) # solving positive
root2 = (-b - discRoot) / (2 * a) # solving negative

print()
print("The solutions are:",  root1, root2)
