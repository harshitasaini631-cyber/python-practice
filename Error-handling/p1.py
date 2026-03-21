#Handle division by Zero
try:
    num1 = int(input("Enter the numerator:"))
    num2 = int(input("Enter the denominator:"))

    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Error. Cannot divide by zero")    