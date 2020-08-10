"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use
parens instead of square brackets.

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values
never needs to be mutated, use a tuple instead of a list.

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically.
"""

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""

    x0, y0 = a
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))



# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE
def print_tuple(t):
    for i in t:
        print(i)

t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line


# Declare a tuple of 1 element then print it
u = (1,)  # What needs to be added to make this work?

# we needed to add a comma after the first value in the tuple because a tuple
# is an object delimmited by the comma

print_tuple(u)
