#creating node
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#creating doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

#traversing in doubly linked list
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
