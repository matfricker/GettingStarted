# add num_1 to num_2
def add(num_1, num_2):
    return num_1 + num_2

# subtract num_1 from num_2
def subtract(num_1, num_2):
    return num_1 - num_2

# multiple num_1 and num_2
def multiply(num_1, num_2):
    return num_1 * num_2

# divide num_1 by num_2
def divide(num_1, num_2):
    return num_1 / num_2

def operationName(num):
    if num == "1":
        return "Add"
    elif num == "2":
        return "Subtract"
    elif num == "3":
        return "Multiple"
    else:
        return "Divide"

print("Operator choices:")
print("1. Add")
print("2. Subtract")
print("3. Multiple")
print("4. Divide")

operation = input("Enter operator 1, 2, 3 or 4):")

if operation in ("1", "2", "3", "4"):
    if operation != "1":
        print(f"{operationName(operation)} still under development.")
    else:
        first_input = int(input("Enter first number: "))
        second_input = int(input("Enter second number: "))
        print(first_input, "+", second_input, "=", add(first_input, second_input))
else:
    print("Invalid input")
