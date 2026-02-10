while True:
    print("\n choose an option")
    print("1. choose an option")
    print("2. choose an option")

    num = int(input("Enter your choice:"))

    if num == 1:
        a = int(input("Enter the no. = "))
        b = int(input("Enter the no. = "))
        print(f"Sum: {a+b}")

    elif num == 2:
        break

    else:
        print("Invalid number. Only choose 1 or 2")     
