"""
Reserve a given string
"""

def stringReverse(inputStr):
    reverseStr = ""
    for index in range(len(inputStr) - 1,-1,-1):
        reverseStr += inputStr[index]
    return reverseStr


print(stringReverse("abcde"))