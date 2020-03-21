
arr = [64, 25, 12, 22, 11]
print("Before sorting")
print(arr)
for i in range(0,len(arr)):
    min_indx = i

    for j in range(i+1,len(arr)):
        if arr[min_indx] > arr[j]:
            min_indx = j
    temp = arr[min_indx]
    arr[min_indx] = arr[i]
    arr[i] = temp

print("Sorted array", arr)
selectionSort(arr)
for i in range(len(arr)):
    print("%d" %arr[i]),
