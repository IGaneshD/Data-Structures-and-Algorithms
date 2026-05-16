# Implement stack in python
# Stack works on FILO(First in Last Out) or LIFO(Last in First Out) principle
# Used in function calls, broswer previous and next page 

# Operations can be performed on Stack
# 1. push(insert)
# 2. pop(remove)
# 3 getStackTop
# 4. isEmpty
# 5. isFull



class Stack:
    """
    This Class implements the stack operations.
    """
    def __init__(self,stacksize=5):
        self.max_stacksize = stacksize
        self.index = -1
        self.stack = []

    
    def push(self, val):
        if self.isFull():
            return "Stack is full, you cannot add more"
        
        self.index += 1
        self.stack.append(val)
        
        return f"element added to stack {val}"

    def pop(self):
        if self.isEmpty():
            return "Stack is empty, you cannot pop anything"

        value_popped = self.stack[self.index]
        self.index -= 1
        self.stack.pop()

        return f"Value popped {value_popped}"

    def isFull(self):
        return self.index + 1 == self.max_stacksize

    def isEmpty(self):
        return self.index == -1

    def getStackTop(self):
        if self.isEmpty():
            return "Stack is Empty"
        
        return self.stack[self.index]
    


object = Stack(5)

print(object.pop())
print(object.push(15))
print(object.push(11))
print(object.push(13))
print(object.getStackTop())
print(object.push(1))
print(object.push(10))
print(object.push(12))
print(object.pop())
