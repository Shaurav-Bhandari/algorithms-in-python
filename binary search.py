def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
numbers = [1, 2, 4, 6, 8, 10, 12]
val = 8
result = binary_search(numbers, val)
print("Index of the target value:", result)
