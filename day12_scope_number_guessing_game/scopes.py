# Modifying global scope variables
counter = 1 # global variable

def increase_counter():
    print(f"Inside function, Counter = {counter}")
    return counter + 1

counter = increase_counter()
print(f"Outside function, Counter = {counter}")
