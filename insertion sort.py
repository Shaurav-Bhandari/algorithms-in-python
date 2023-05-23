def insertion_sort(Data):
    n = len(Data)

    for i in range(1, n):
        key = Data[i]
        j = i - 1

        while j >= 0 and Data[j] > key:
            Data[j + 1] = Data[j]
            j -= 1

        Data[j + 1] = key

    return Data
array = [9,8,7,6,5,4,3,2,1]
value = insertion_sort(array)

