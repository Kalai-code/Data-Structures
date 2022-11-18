"""
Implement Queue using Stack
input:[2,3,7,8]
output: pop() --> 2
"""

class QueueUsingStack:

    def __init__(self):
        self.list1 =[]
        self.list2 = []
    
    def push(self,num):
        self.list1.append(num)
        print(self.list1)
        return "Item Added"
    
    def pop(self):
        if len(self.list2) != 0:
            return self.list2.pop()
        if len(self.list2) == 0 and len(self.list1) > 0:
            while len(self.list1) > 0:
                self.list2.append(self.list1.pop())
            return self.list2.pop()
        else:
            return "No items to remove"
            

    def peek(self):
        if len(self.list2) != 0:
            return self.list2[-1]
        if len(self.list2) == 0 and len(self.list1) > 0:
            while len(self.list1) > 0:
                self.list2.append(self.list1.pop())
            return self.list2[-1]
        else:
            return "No items to view"
    
    def empty(self):
        if len(self.list1) == 0 and len(self.list2) == 0:
            return True
        else:
            return False


queue = QueueUsingStack()
print(queue.push(3))
print(queue.push(5))
print(queue.push(7))

print(queue.pop())
print(queue.peek())
print(queue.pop())
print(queue.empty())
print(queue.pop())
print(queue.empty())
print(queue.pop())


