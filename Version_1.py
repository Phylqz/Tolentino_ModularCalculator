num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Choose operation")
print("Add - 1")
print("Subtract - 2")
print("Multiply - 3")
print("Divide - 4")
operation = int(input("Enter choice: "))

result = 0
if operation == 1:
    add_numbers = num1 + num2
    print (num1, "+", num2, "=", add_numbers)
elif operation == 2:
    subtract_numbers = num1 - num2
    print (num1, "-", num2, "=", subtract_numbers)
elif operation == 3:
    multiply_numbers = num1 * num2
    print (num1, "*", num2, "=", multiply_numbers)
elif operation == 4:
    divide_numbers = num1 / num2
    print (num1, "/", num2, "=", divide_numbers)
else:
    print("Choose an operation from the list")