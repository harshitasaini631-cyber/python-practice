#finding the maximum element in an array

arr = [4,7,1,3,9]

maximum = arr[0] #assuming element at index 0 is maximum and then comapring it to all the other elements

for num in arr:
    if num > maximum:
        maximum = num
print("Maximum:",maximum)