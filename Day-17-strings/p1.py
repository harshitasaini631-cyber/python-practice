str = input("Enter the string:")
lower = 0
upper = 0
for i in str:
    if(i.islower()):
        lower+=1
    elif i.isupper():
        upper+=1
print("lower case letters:",lower)            
print("upper case letters:",upper)            
