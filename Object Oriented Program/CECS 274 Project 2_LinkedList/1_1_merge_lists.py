class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next


class LinkedList:
  def __init__(self):  
    self.head = None

  def insert(self, data):
    # Checks if specific list is empty. If it is insert the new element as head.
    newNode = Node(data)
    if self.head is None:
      self.head = newNode
    # If its not, sets curr = self.head and traverses through the linked list until we get to the last node
    # We then add the new node at the end of the list
    else:
      curr = self.head
      while curr.next is not None:
        curr = curr.next
      curr.next = newNode

  def printLL(self):
    # Set curr = self.head. Traverse through the list printing the data of each node as we go through it.
    curr = self.head
    while curr:
      print(curr.data, end=' ')
      curr = curr.next

def merge(List_1, List_2) -> Node:
  mergeList = LinkedList()
  dummy = Node(0)
  temp = dummy

  # Checks if either one of the lists are empty. Whichever list is empty we return the other one unless
  # both are empty then we return the statement: "Both lists are empty.
  if List_1 is None and List_2 is None:
    return "Both lists are empty."
  elif List_1 is None:
    return List_2
  elif List_2 is None:
    return List_1
  # We traverse through the two lists comparing the nodes in the same position. Whichever node.data of each list
  # is smaller we add that node to our dummy and then compare the next node of that list to the
  # the previous node until all nodes have been added to the dummy list
  while List_1 and List_2:
    if List_1.data < List_2.data:
      temp.next = List_1
      List_1 = List_1.next
    else:
      temp.next = List_2
      List_2 = List_2.next
    temp = temp.next
  if List_1:
    temp.next = List_1
  if List_2:
    temp.next = List_2
  return dummy.next


# Test merge() function
# Linked List of L
L = LinkedList()
L.insert(3)
L.insert(6)
L.insert(9)
L.insert(14)
L.insert(17)
# Linked List of M

M = LinkedList()
M.insert(2)
M.insert(8)
M.insert(15)
M.insert(19)
M.insert(22)

# Merge Function
LM = LinkedList()
LM.head = merge(L.head, M.head)
LM.printLL()
