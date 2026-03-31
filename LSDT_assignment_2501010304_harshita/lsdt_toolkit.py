
class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = x
        self.size += 1

    def _resize(self, new_capacity):
        print(f"Resizing from {self.capacity} to {new_capacity}")
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def pop(self):
        if self.size == 0:
            print("DynamicArray is empty. Cannot pop.")
            return None
        value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return value

    def __str__(self):
        elements = []
        for i in range(self.size):
            elements.append(str(self.data[i]))
        return "[" + ", ".join(elements) + "]"

    def print_status(self):
        print(f"Array: {self}, Size: {self.size}, Capacity: {self.capacity}")


class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, x):
        new_node = SLLNode(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, x):
        new_node = SLLNode(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_by_value(self, x):
        if self.head is None:
            print(f"List is empty. Cannot delete {x}.")
            return

        if self.head.data == x:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            print(f"Deleted {x} from Singly Linked List.")
            return

        current = self.head
        while current.next is not None:
            if current.next.data == x:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                print(f"Deleted {x} from Singly Linked List.")
                return
            current = current.next

        print(f"Value {x} not found in Singly Linked List.")

    def traverse(self):
        if self.head is None:
            print("Singly Linked List is empty.")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def is_empty(self):
        return self.head is None


class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, x):
        new_node = DLLNode(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after_node(self, target, x):
        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        current = self.head
        while current is not None:
            if current.data == target:
                new_node = DLLNode(x)
                new_node.next = current.next
                new_node.prev = current

                if current.next is not None:
                    current.next.prev = new_node
                else:
                    self.tail = new_node

                current.next = new_node
                print(f"Inserted {x} after {target}.")
                return
            current = current.next

        print(f"Target {target} not found in Doubly Linked List.")

    def delete_at_position(self, pos):
        if self.head is None:
            print("Doubly Linked List is empty.")
            return

        if pos < 0:
            print("Invalid position.")
            return

        current = self.head
        index = 0

        while current is not None and index < pos:
            current = current.next
            index += 1

        if current is None:
            print("Position out of range.")
            return

        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        print(f"Deleted node at position {pos}.")

    def traverse_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty.")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


class Stack:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, x):
        self.sll.insert_at_beginning(x)

    def pop(self):
        if self.sll.head is None:
            print("Stack Underflow. Cannot pop.")
            return None
        value = self.sll.head.data
        self.sll.head = self.sll.head.next
        if self.sll.head is None:
            self.sll.tail = None
        return value

    def peek(self):
        if self.sll.head is None:
            print("Stack is empty.")
            return None
        return self.sll.head.data

    def is_empty(self):
        return self.sll.head is None

    def display(self):
        print("Stack top to bottom:")
        self.sll.traverse()


class Queue:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def enqueue(self, x):
        self.sll.insert_at_end(x)

    def dequeue(self):
        if self.sll.head is None:
            print("Queue Underflow. Cannot dequeue.")
            return None

        value = self.sll.head.data
        self.sll.head = self.sll.head.next
        if self.sll.head is None:
            self.sll.tail = None
        return value

    def front(self):
        if self.sll.head is None:
            print("Queue is empty.")
            return None
        return self.sll.head.data

    def is_empty(self):
        return self.sll.head is None

    def display(self):
        print("Queue front to rear:")
        self.sll.traverse()


def is_balanced(expr):
    stack = Stack()
    matching = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            top = stack.pop()
            if top is None or top != matching[ch]:
                return False

    return stack.is_empty()


def main():
    print("=" * 50)
    print("TASK 1: DYNAMIC ARRAY")
    print("=" * 50)
    arr = DynamicArray(2)

    for i in range(1, 12):
        print(f"Appending {i}")
        arr.append(i)
        arr.print_status()

    print("\nPerforming 3 pops:")
    print("Popped:", arr.pop())
    arr.print_status()
    print("Popped:", arr.pop())
    arr.print_status()
    print("Popped:", arr.pop())
    arr.print_status()

    print("\n" + "=" * 50)
    print("TASK 2A: SINGLY LINKED LIST")
    print("=" * 50)
    sll = SinglyLinkedList()

    print("Insert 3 elements at beginning:")
    sll.insert_at_beginning(30)
    sll.traverse()
    sll.insert_at_beginning(20)
    sll.traverse()
    sll.insert_at_beginning(10)
    sll.traverse()

    print("\nInsert 3 elements at end:")
    sll.insert_at_end(40)
    sll.traverse()
    sll.insert_at_end(50)
    sll.traverse()
    sll.insert_at_end(60)
    sll.traverse()

    print("\nDelete value 40:")
    sll.delete_by_value(40)
    sll.traverse()

    print("Delete value 100 (not present):")
    sll.delete_by_value(100)
    sll.traverse()

    print("\n" + "=" * 50)
    print("TASK 2B: DOUBLY LINKED LIST")
    print("=" * 50)
    dll = DoublyLinkedList()

    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.traverse_forward()

    print("\nInsert 25 after 20:")
    dll.insert_after_node(20, 25)
    dll.traverse_forward()

    print("\nDelete node at position 1:")
    dll.delete_at_position(1)
    dll.traverse_forward()

    print("\nDelete last node:")
    dll.delete_at_position(3)
    dll.traverse_forward()

    print("\n" + "=" * 50)
    print("TASK 3A: STACK USING SLL")
    print("=" * 50)
    stack = Stack()
    stack.push(100)
    stack.push(200)
    stack.push(300)
    stack.display()
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    stack.display()

    print("\n" + "=" * 50)
    print("TASK 3B: QUEUE USING SLL")
    print("=" * 50)
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    print("Front:", queue.front())
    print("Dequeue:", queue.dequeue())
    queue.display()

    print("\n" + "=" * 50)
    print("TASK 4: BALANCED PARENTHESES CHECKER")
    print("=" * 50)
    test_cases = ["([])", "([)]", "(((", ""]
    for expr in test_cases:
        result = is_balanced(expr)
        print(f'Expression: "{expr}" ->', "Balanced" if result else "Not Balanced")


if __name__ == "__main__":
    main()