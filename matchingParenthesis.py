"""
Return true if the parenthesis matches. Else return false
Input: ((a)(b)), )(ab)(
"""

def matchParenthesisOneType(inputStr):
    if inputStr.count('(') != inputStr.count(')'):
        return False
    else:
        parenList = []
        for ch in inputStr:
            if ch == '(':
                parenList.append(ch)
            if ch == ')':
                if len(parenList) == 0:
                    return False
                else:
                    parenList.pop()
        if len(parenList) == 0:
            return True
        else:
            return False


print(matchParenthesisOneType("((a)(b))"))

print(matchParenthesisOneType(" )(ab)"))

print(matchParenthesisOneType(" )(ab)("))

