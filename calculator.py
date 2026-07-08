print("Simple Calculator")

first_number = float(input("Enter the first number: "))
operator = input("Enter operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
    print("The result is:", result)

elif operator == "-":
    result = first_number - second_number
    print("The result is:", result)

elif operator == "*":
    result = first_number * second_number
    print("The result is:", result)

elif operator == "/":
    if second_number == 0:
        print("Error: You cannot divide by zero.")
    else:
        result = first_number / second_number
        print("The result is:", result)

else:
    print("Invalid operator.")