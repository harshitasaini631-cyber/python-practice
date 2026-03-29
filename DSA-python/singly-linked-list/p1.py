class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    #traversing thorugh a linked list
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")       


    #insert at beginning
    def insert_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node