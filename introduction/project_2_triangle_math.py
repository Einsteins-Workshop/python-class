# Look at sample_2_types.py and sample_3_math.py for example statements

# Ask the user for one leg of a right triangle
first_leg = int(input("Enter the length of a leg of a right triangle\n"))

# Ask the user for the length of the second leg of the triangle
second_leg = int(input("Enter the length of the second leg of a right triangle\n"))

# Compute and print the area of the triangle (first_leg times second_leg divided by 2)
triangle_area = first_leg*second_leg
print("The area of the triangle is:")
print(triangle_area/2)
# Compute and print the hypotenuse of the triangle (the square root of the first_leg squared + the second leg squared).
# sqrt of a^a + b*b
a = int(input("Enter a number"))
b = int(input("Enter another number"))
from math import sqrt
print(sqrt(a*a + b*b))