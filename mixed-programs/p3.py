
num = int(input("Enter a number: "))
n = num
power = len(str(num))
total = 0

while n > 0:
    digit = n % 10  #% 10 gives last digit. 153%10 = 3
    total += digit ** power #3 ** 3 = 27. total = 0+27
    n //= 10  #Removes last digit. 153//10 => n = 15

    
# goes upto 3 itertions because n = 153 which is 3  so n >0 but after three it will satisfy the condition so it will stop.
if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")