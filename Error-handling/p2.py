try:
    num = int(input("Enter the number:"))
    print("You entered:",num)
except ValueError:
    print("Error . please enter a valid number")

#value error happens when conversion fails        