class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        print(item, "inserted")

    # Dequeue operation
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            removed = self.queue.pop(0)
            print(removed, "deleted")

    # Display queue
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", self.queue)