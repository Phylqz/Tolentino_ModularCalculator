num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Choose operation")
print("Add - 1")
print("Subtract - 2")
print("Multiply - 3")
print("Divide - 4")
operation = int(input("Enter choice: "))

def add_numbers(num1, num2):
    result = num1 + num2
    return result

def subtract_numbers(num1, num2):
    result = num1 - num2
    return result

def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

def divide_numbers(num1, num2):
    result = num1 / num2
    return result

#addition
if operation == 1:
    print (num1, "+", num2, "=", add_numbers(num1, num2))
#subtraction
elif operation == 2:
    print (num1, "-", num2, "=", subtract_numbers(num1, num2))
#multiplication
elif operation == 3:
    print (num1, "*", num2, "=", multiply_numbers(num1, num2))
#division
elif operation == 4:
    if num2 == 0:
        print (num1, "/", num2, "=", "Undefined")
    else:
        print (num1, "/", num2, "=", divide_numbers(num1, num2))
else:
    print("Choose an operation from the list")