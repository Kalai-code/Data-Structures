"""
Implement Queue using Stack
input:[2,3,7,8]
output: pop() --> 2
"""

list1, list2 = [],[]

def Enqueue(num):
    list1.append(num)


def Dequeue():
    if len(list2) == 0:
        while len(list1) > 0:
            list2.append(list1.pop())
    list2.pop()
    print(list2)


Enqueue(2)
Enqueue(3)
Dequeue()