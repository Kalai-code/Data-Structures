"""
first the most repeated element for Integer Array
arr = [1,2,2,3,3,3,4]
"""

def mostFrequent(arr):
    frequencies = {}
    max = 0
    for num in arr:
        if num not in frequencies:
            frequencies[num] = 1
        else:
            frequencies[num] += 1
    for num in arr:
        if max < frequencies[num]:
            max = frequencies[num]
    
    return max


print(mostFrequent(arr = [1,2,2,3,3,3,4]))
    

