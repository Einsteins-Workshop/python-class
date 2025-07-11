#Lists are a sequence of objects, and are created by putting items inside []
my_list = [1,4,6,8]
a= "foo"
b="bar"
c = [a,b]
print(c)
# You can add things to a list with the append method.
print(f"The initial list is {my_list}")
my_list.append(7)
print(f"The list after appending 7 is {my_list}")
#You can look at elements of the list my_list[1]. Indexes are tricky, starting at 0. Y
# ou can also use negative index elements, which count from the end of the list.
# Create a list and try accessing elements of the list:
print(f"The first element is {my_list[0]}")
print(f"The element at index 2, which is the third element of the list, is {my_list[2]}")
print(f"The element at index -1, which is the last element of the list, is {my_list[-1]}")

# You can also change elements of the list like they are variables
my_list[0] = "Changed"
print(f"The changed list is {my_list}")

# You can get a range of values, creating a new list, using [:] notation
print(f"A range from index 1 to 3 is {my_list[1:3]}") # This will get everything from position 1 (the second index) up to but not
                    # including position 3. So, it will print out two elements.


# Note that lists can contain anything. They can contain numbers and strings together, or even other
# lists!
complex_list = [1, 2, "a", "b", [1, 2, 3]]
print("\n\n")
print(f"A more complex list is: {complex_list}")
print(f"The first element of that list is complex_list[0]")
print(f"Indexing on -1 and then 2 of that list is {complex_list[-1][2]}")

# You can also use the range() function to quickly get a list of numbers from 0 to one less than the
# argument
print("\nHere is the result of a range of 10")
print(list(range(10)))

