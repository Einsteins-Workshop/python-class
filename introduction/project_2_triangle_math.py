# Look at sample_2_types.py and sample_3_math.py for example statements

# Ask the user for one leg of a right triangle
first_leg = int(input("Enter the length of a side of a right triangle\n"))

# Ask the user for the length of the second leg of the triangle
second_leg = int(input("Enter the length of another side of a right triangle\n"))

# Compute and print the area of the triangle (first_leg times second_leg divided by 2)
print("The area is " + str((first_leg + second_leg) / 2))

# Compute and print the hypotenuse of the triangle (the square root of the first_leg squared + the second leg squared).
print("The third side is " + str(((first_leg ** 2) + (second_leg ** 2)) ** (1/2)))