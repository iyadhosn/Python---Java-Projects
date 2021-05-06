
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedQueue:
    # FIFO queue implementation using a singly linked list for storage.
    def __init__(self):
        # Create an empty queue.
        self.head = None
        self.tail = None
        self.size = 0 # number of queue elements

    def len(self):
        # Return the number of elements in the queue.
        return self.size


    def is_empty(self):
        # Return True if the queue is empty.
        return self.size == 0



    def first(self):
        # Return (but do not remove) the element at the front of the queue
        if self.is_empty():
            raise("The List is emppty.")
        else:

            return print(self.head.data)


    def dequeue(self):
        # Remove and return the first element of the queue (i.e., FIFO).
        if self.is_empty():
            return print("The List is empty, there is nothing to return.")
        # If the list isn't empty return self.head, assign a new self.head, and decrese the size by one
        else:
            curr = self.head
            self.head = self.head.next
            self.size -= 1
            return print(curr.data)


    def enqueue(self, e):
        newNode = Node(e)
        # If it is empty set tail and head = to new node
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        # Otherwise assign the node as the new tail and increment the size by one.
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def rotate(self):
        # If the size is greater than 0 set self.tail.next  = to the head, assign that node as your new tail,
        # and shift head over to set your head to the next node.
        if self.size > 0:
            self.tail.next = self.head
            self.tail = self.head
            self.head = self.head.next


queue = LinkedQueue()
queue.dequeue() # print error message or throw exception
queue.enqueue(6) # queue = 6
queue.enqueue(2) # queue = 6->2
queue.enqueue(7) # queue = 6->2->7
queue.dequeue() # print 6 and queue = 2->7
queue.first() # print 2 and queue = 2->7
queue.enqueue(1) # queue = 2->7->1
queue.rotate() # queue = 7->1->2
#queue.enqueue(5) # queue = 7->1->2->5
