class Node:    
    def __init__(self,data):    
        self.data = data
        self.next = None
     
class CreateList:    
 
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def add(self,data):    
        newNode = Node(data)
        # Checks if the list is empty. If it is it sets the head and tail equal to that new node.
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            # Sets self.tail.next equal to the new node. Sets the new node as the new tail and the new
            # node.next equal to the head to create a circular linked list
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head

    # This function will print the nodes of circular linked list from the head
    def print(self):
        # lets the user know if the list is empty
        if self.head is None:
            print("List is empty")

        else:
        # Traverses through the list and prints each node.data until it gets to the end of th list
            curr = self.head
            while curr.next != self.head:
                print(curr.data, end=' ')
                curr = curr.next

    # This function will count the nodes of circular linked list
    def countNodes(self):
        # Traverses through the linked list incrementing counter by one each time a node is taken account for
        # The number of nodes is then returned
        curr = self.head
        counter = 0
        if self.head != None:
            while curr.next != self.head:
                counter += 1
                curr = curr.next
            print("Number of nodes in Linked list: ", counter)
        else:
            print("No nodes in list")

        
     
class CircularLinkedList:    
    cl = CreateList();    
    # Adds data to the list
    cl.add(4);    
    cl.add(5);    
    cl.add(7);    
    cl.add(8);    
    cl.add(12);    
    cl.add(56);   
    cl.add(85);
    cl.add(41); 
    #Displays all the nodes present in the list   
    cl.print();
    cl.countNodes();
