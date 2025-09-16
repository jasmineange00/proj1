x = int(input("Enter number1: "))
y = int(input("Enter number2: "))
op = input("Operator (+, -, *): ")

if op == "+":
    print(f"Sum of {x} + {y} = {x + y}")
elif op == "-":
    print(f"Difference of {x} - {y} = {x - y}")
elif op == "*":
    print(f"Product of {x} * {y} = {x * y}")
else:
    print("Invalid operator. Bye")
