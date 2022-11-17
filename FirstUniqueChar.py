"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

"""

def firstUniqChar(inputStr):
    dictCh = {}
    for ch in inputStr:
        if ch not in dictCh:
            dictCh[ch] = 1 
        else:
             dictCh[ch] += 1
    for index in range(len(inputStr)):
        if dictCh[inputStr[index]] == 1:
            return index
    return -1


print(firstUniqChar("loveleetcode"))

print(firstUniqChar("leetcode"))

print(firstUniqChar("aabb"))

