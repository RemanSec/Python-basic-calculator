
print("===== WELCOME TO PYTHON CALCULATOR =====")

# Ask for the first number
num1 = float(input("Enter your first number: "))

# Ask which operation the user wants
operation = input(
    "What do you want to do? (+, -, *, /): "
)

# Ask for the second number
num2 = float(input("Enter your second number: "))

# Perform the calculation
if operation == "+":
    result = num1 + num2
    print("Your result is:", result)

elif operation == "-":
    result = num1 - num2
    print("Your result is:", result)

elif operation == "*":
    result = num1 * num2
    print("Your result is:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Your ANSWER is:", result)
    else:
        print("Error! You cannot divide ZERO by ZERO .")

else:
    print("INVALID! Please use +, -, * or /.")

print("===== THANK YOU FOR USING CALCULATOR =====")
