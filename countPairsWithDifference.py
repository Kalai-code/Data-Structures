"""
Given an array of intergers. Count the number of unique pairs of integers that have the difference k
Input: [1,7,5,9,2,12,3], k = 2
Output: 4 => (1,3),(3,5),(5,7),(7,9)
"""

def uniquePairDifference(arr,k):
    arr.sort()
    count = 0
    for index in range(len(arr) - 1):
        num = arr[index] + k
        if num in arr[index+1:]:
            count += 1
    return count


print(uniquePairDifference([1,7,5,9,2,12,3],2))
