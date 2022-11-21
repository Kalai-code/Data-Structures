"""
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]

"""

def selectionSort(arr):
    arrLength = len(arr) - 1
    for index in range(arrLength - 1):
        minIndex = index
        for j in range(index + 1,arrLength):
            if arr[j] < arr[minIndex]:
                minIndex = j
            arr[index], arr[minIndex] = arr[minIndex], arr[index]
    return arr


print(selectionSort([-2, 45, 0, 11, -9,88,-97,-202,747]))