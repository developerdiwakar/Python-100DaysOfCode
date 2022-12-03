from art import calc_logo
# Perform calculator operation on user inputs
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulo(a, b):
    return a % b

# operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo
}
    
def calculate():
    print(calc_logo)
    finished_calculating = False

    num1 = float(input("What's the first number? "))
    while not finished_calculating: 
        
        for op in operations:
            print(op)
        operation = input("Type one of the above operation: ")
        num2 = float(input("What's the next number? "))

        function = operations[operation]
        output = function(num1, num2)
        print(f"{num1} {operation} {num2} = {output}")
        
        continue_calculating = input(f"Type any key to continue calculating with {output}, or type 'n' to start new or 'e' to exit.: ")
        if continue_calculating == 'e':
            finished_calculating = True
        elif continue_calculating == 'n':
            calculate()
        else:
            num1 = output
calculate()