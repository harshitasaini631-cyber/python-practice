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

#inserting at the end
    def insert_at_end(self, data):
        new_node = DNode(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp    


#traversing backward
    def traverse_backward(self):
        temp = self.head

        if temp is None:
             print("None")
             return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")  

    def insert_at_position(self, data, pos):
    new_node = DNode(data)

    if pos == 0:
        self.insert_at_beginning(data)
        return

    temp = self.head
    for _ in range(pos - 1):
        if temp is None:
            print("Invalid position")
            return
        temp = temp.next

    if temp is None:
        print("Invalid position")
        return

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next is not None:
        temp.next.prev = new_node

    temp.next = new_node      
      
    #deleting form end 
    def delete_from_end(self):
    if self.head is None:
        return

    if self.head.next is None:
        self.head = None
        return

    temp = self.head
    while temp.next:
        temp = temp.next

    temp.prev.next = None

    #delete from beginning
    def delete_from_beginning(self):
    if self.head is None:
        return

    if self.head.next is None:
        self.head = None
        return

    self.head = self.head.next
    self.head.prev = None