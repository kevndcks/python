try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divide by zero")
except(ValueError, TypeError):
    print("Error occurred")

try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")