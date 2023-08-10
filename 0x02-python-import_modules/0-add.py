#!/usr/bin/python3

# Assign values to variables a and b
a = 1
b = 2

# Import the add function from add_0.py
if __name__ == "__main__":
    from add_0 import add

    # Calculate the result using the imported add function
    result = add(a, b)

    # Print the formatted output
    print("{} + {} = {}".format(a, b, result))

