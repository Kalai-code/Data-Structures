"""
Given an array of integers. Return indices of the two numbers such that they add up to a specific target
Input: [2,7,11,15], target = 9
Output: [0,1]
"""

def twoSum(arr, target):
    for index in range(len(arr) - 1):
        newNum = target - arr[index]
        if newNum in arr[index + 1:]:
            return index, arr.index(newNum,index + 1)

print(twoSum([2,7,11,15],9))
        