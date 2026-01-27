
guess = 5
while True:
    num =  int(input("Enter the guess number:"))
    if num > guess:
        print("too high")
    elif num < guess:
        print("too low")   
    else:
        print("correct")     


