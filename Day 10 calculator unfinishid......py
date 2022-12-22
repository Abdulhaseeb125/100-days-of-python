def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 != 0:
        return n1 / n2


def Dictionary(operation):
    Dict = {
        "+": add(num1, num2),
        "-": subtract(num1, num2),
        "*": multiply(num1, num2),
        "/": divide(num1, num2)
    }
    result = Dict[operation]
    return result


num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))

operation = input("operation:")
print(Dictionary(operation))
Again = True
while Again:
    pre = Dictionary(operation)
    again = input("Do you want to continue:")
    if again == 'y':
        num1 = pre
        num2 = int(input("2nd number:"))
        operation = input("operation:")
        Dictionary(operation)
        print(Dictionary(operation))
    elif again == 'a':
        num1 = int(input("Enter 1st number:"))
        num2 = int(input("Enter 2nd number:"))
        operation = input("operation:")
        print(Dictionary(operation))
    else:
        Again = False
