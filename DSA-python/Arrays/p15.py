#check if array is sorted
arr = [ 1,2,3,4,5]
isSorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        isSorted = False
        break

print(isSorted)