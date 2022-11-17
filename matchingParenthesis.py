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

def matchParenthesisdifferentType(input):
    openParenthesis = ['(','[','{']
    closeParenthesis = [')',']','}']
    parenList = []
    for ch in input:
        if ch in openParenthesis:
            parenList.append(ch)
        if ch in closeParenthesis:
            if len(parenList) == 0:
                return False
            else:
                if ch == ')' and parenList[-1] == '(':
                    parenList.pop()
                elif ch == ']' and parenList[-1] == '[':
                    parenList.pop()
                elif ch == '}' and parenList[-1] == '{':
                    parenList.pop()                
                else:
                    return False
    if len(parenList) == 0:
        return True
    else:
        return False




print(matchParenthesisOneType("((a)(b))"))

print(matchParenthesisOneType(" )(ab)"))

print(matchParenthesisOneType(" )(ab)("))

print(matchParenthesisdifferentType("()[]{}"))

print(matchParenthesisdifferentType("(]{}"))


