# Write a python program to reverse a linked list

# Input list: 2 -> 3 -> 5 -> 10
# Ouput list: 10 -> 5 -> 3 -> 2

# Create a Node class
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def __init__(self, val=None):
        self.head = Node(val) if val else None

    
    def createAlinkedList(self, list_of_val):
        temp = self.head
        for val in list_of_val:
            newNode = Node(val)
            if not self.head:
                self.head = newNode
                temp = self.head
            else:
                temp.next = newNode
                temp = temp.next
        
        return self.head
    

def reverseALinkedList(sll):
    current = sll
    head = None

    while current:
        if not head:
            head = current
            current = current.next
            head.next = None
        else:
            temp = current
            current = current.next
            temp.next = head
            head = temp
    return head


# instantiate the singlyLinkedList class
sll = SinglyLinkedList()
sll_head = sll.createAlinkedList([2,3,5,10])

# print linked list
temp = sll_head
while temp:
    print(f"{temp.val}", end="->")
    temp = temp.next

# reverse the linkedlist
reversedLL = reverseALinkedList(sll_head)
# print the reversed linked list
temp = reversedLL
print()
while temp:
    print(f"{temp.val}", end="->")
    temp = temp.next