# Look at sample_2_types.py and sample_3_math.py for example statements
import math

number = 25
square_root = math.sqrt(number)
print(square_root)

# Ask the user for one leg of a right triangle
first_leg = int(input("Enter the length of a leg of a right triangle\n"))

# Ask the user for the length of the second leg of the triangle
second_leg = int(input("Enter the length of a leg of a right triangle\n"))


# Compute and print the area of the triangle (first_leg times second_leg divided by 2)
print((first_leg * second_leg) / 2)

# Compute and print the hypotenuse of the triangle (the square root of the first_leg squared + the second leg squared).
print(first_leg^2 + second_leg^2)