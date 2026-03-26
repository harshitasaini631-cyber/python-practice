#move negative to left

arr = [1, -2, 3, -4, 5]
j=0
for i in range(len(arr)):
    if arr[i] < 0:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1
print(arr)
