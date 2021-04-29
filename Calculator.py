# Übung dazu: einen Taschenrechner programmieren, in dem der User die Zahlen und die Rechenoperation eingibt

user_name = input("Bitte geben Sie Ihren Namen ein: ")
print("Hallo " + user_name)

try:
    first_number = float(input("Bitte geben Sie die erste Zahl ein: "))
except ValueError:
    print("Das ist keine Zahl.")
    exit()

operator = input("Geben Sie einen Operator ein (+ addieren, - subtrahieren, * multiplizieren, : dividieren): ")
try:
    second_number = float(input("Bitte geben Sie die zweite Zahl ein: "))
except ValueError:
    print("Das ist keine Zahl.")
    exit()

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == ":":
    print(first_number / second_number)
else:
    print("Invalider Operator")
