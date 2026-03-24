#second largest element in the array
arr = [10, 20, 4, 45, 99]

first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

if second == float('-inf'):
    print("No second largest element")
else:
    print("Second largest is:", second)