#creating a node
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#creating doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None

#traversing in a dpoubly linked list
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

#insert at beginnig
    def insert_at_beginning(self, data):
        new_node = DNode(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node

        self.head = new_node
      
