try:
    num = int(input("Enter a number:"))
    result = 10/num
    print("square of the number:",result)
except ZeroDivisionError:
    print("Error. Cannot divide by zero")
except ValueError:
    print("Error. Invalid input")
finally: #always runs no matter what happens.
    print("Execution complete")            