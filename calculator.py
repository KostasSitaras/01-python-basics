def calculate(first_number, operator, second_number):
    if operator == "+":
        return first_number + second_number

    elif operator == "-":
        return first_number - second_number

    elif operator == "*":
        return first_number * second_number

    elif operator == "/":
        if second_number == 0:
            print("Error: You cannot divide by zero.")
            return None
        else:
            return first_number / second_number

    else:
        print("Invalid operator.")
        return None


def run_calculator():
    print("Simple Calculator")

    while True:
        try:
            first_number = float(input("Enter the first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            second_number = float(input("Enter the second number: "))

            result = calculate(first_number, operator, second_number)

            if result is not None:
                print("The result is:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")

        again = input("Do you want to calculate again? (yes/no): ")

        if again.lower() != "yes":
            print("Goodbye!")
            break


run_calculator()