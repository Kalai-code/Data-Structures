"""
find the first repeated character in a given string
"""

def firstRepeatChar(inputStr):
    outList = []
    for ch in inputStr:
        if ch not in outList:
            outList.append(ch)
        else:
            return ch
    return 0


print(firstRepeatChar("hello"))