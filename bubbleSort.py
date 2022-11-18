"""
Input: arr = [64, 34, 25, 12, 22, 11, 90,15]
Output: [11,12,22,25,34,64,90]
"""

def bubbleSort(arr):
    arrLength = len(arr)
    for i in range(arrLength - 1):
        swapped = False
        for j in range(i+1,arrLength):
            if arr[i] > arr[j]:
                swapped = True
                arr[i], arr[j] = arr[j],arr[i]
        if not swapped:
            return arr
    return arr


print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))

print(bubbleSort([39, 12, 18, 85, 72, 10, 2, 18]))