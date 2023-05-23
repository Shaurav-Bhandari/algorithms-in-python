def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1
numbers = [1, 5, 2, 8, 12, 4]
val = 8
result = linear_search(numbers, val)
print("Index of the target:", result)
