


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    
class SinglyLinkedList:

    """
    this singly linked list can be instantiated using a val for first Node, default is set to None
    ```
    sll = SinglyLinkedList(val=10) # this will create a singlyLinkedList with head Node having value 10

    sll1 = SinglyLinkedList() # this will create an empty linkedList.
    ```
    """

    def __init__(self, val=None):
        self.head = Node(val) if val else None

    def isEmpty(self):
        return self.head == None
    
    def addNodeAtEnd(self, val):
        """
        addNodeAtEnd() method appends the node at the end.
        ```
        sll.addNodeAtEnd(val=14)
        ```
        It becomes first node in the list if the list is empty.
        """
        newNode = Node(val)

        if self.isEmpty():
            self.head = newNode
            return self.head
        
        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = newNode
        
        return self.head

    def addNodeAtStart(self, val):
        """
        addNodeAtStart() method appends the node at the end.
        ```
        sll.addNodeAtStart(val=12)
        ```
        if list is empty, then it becomes first element in the list.
        """
        newNode = Node(val)

        newNode.next = self.head
        self.head = newNode

        return self.head
    
    def printLinkedList(self):
        if self.isEmpty():
            print("Linked List is Empty")
            return 
        
        temp = self.head

        while temp:
            print(f"{temp.val}", end="-->")
            temp = temp.next

    
    def deleteFirstNode(self):
        pass

    def deleteLastNode(self):
        pass

    def deleteNthNode(self):
        pass





sll = SinglyLinkedList(10)

sll.printLinkedList()

sll.addNodeAtEnd(11)
sll.addNodeAtEnd(12)
sll.addNodeAtEnd(13)
sll.addNodeAtEnd(14)

sll.addNodeAtStart(20)

sll.printLinkedList()