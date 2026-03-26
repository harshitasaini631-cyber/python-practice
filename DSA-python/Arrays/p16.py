#place all zeros to end

arr = [1,3,0,9,2,0,5,0,0,1]
j = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j],arr[i]=arr[i],arr[j]
        j+=1
print(arr)        