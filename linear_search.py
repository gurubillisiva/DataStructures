def search(arr1, n1, x1):
    for i in range(0, n1):
        if arr1[i] == x1:
            return i
    return -1


arr = [1, 2, 20, 45, 60, -5, 80, 70]
x = 55
n = len(arr)
result = search(arr, n, x)
if result == -1:
    print("Element not found")
else:
    print("Element is present at index", result)
