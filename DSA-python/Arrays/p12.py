#reverse an array using pointers

arr = [1,4,7,9,3,0]

left = 0
right = len(arr)-1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)    