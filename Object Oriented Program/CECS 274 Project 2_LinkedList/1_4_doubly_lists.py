import numpy as np
from base import BaseList
class DLList(BaseList):
    
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy


    def get_node(self, i: int) -> Node:
        if i < (self.n/2):
            curr = self.dummy.next
            for x in range(i):
                curr = curr.next
        else:
            curr = self.dummy
            for x in range(self.n - i):
                curr = curr.prev
        return curr


    def get(self, i: int):
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x


    def set(self, i: int, x):
        # we find node i and set its value equal to x
        curr = self.get_node(i)
        char = curr.x
        curr.x = x
        return char


    def _remove(self, w: Node):
        # Remove node w for the list and decrease the size by one
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1


    def remove(self, i: int):
        if i < 0 or i >= self.n: #raise IndexError()
            return print("Error: Nothing to remove")
        self._remove(self.get_node(i))


    def add_before(self, w: Node, x):
        # Inserts node curr with the data of x before w
        # and increases size by one
        curr = DLList.Node(x)
        curr.prev = w.prev
        curr.next = w
        curr.next.prev = curr
        curr.prev.next = curr
        self.n += 1
        return curr


    def add(self, i: int, x):
        if i < 0 or i > self.n:    #raise IndexError()
            return print("Error: Nothing to remove")
        self.add_before(self.get_node(i), x)


    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next


    def size(self) -> int:
        return self.n


    def append(self, x : np.object)  :
        self.add(self.n, x)


    def isPalindrome(self,) -> bool :
        # Sets curr and last equal to the first node
        curr = self.dummy.next
        last = self.dummy.next
        # Traverses through and sets last equal to the last node
        while last.next.x is not None:
            last = last.next
        # Works its way in checking the last and first element first.
        # If they are not the same it returns false
        # If they are all the same it returns true
        while curr != last:
            if curr.x != last.x:
               return False
            curr = curr.next
            last = last.prev
        return True



    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x


dl = DLList()
dl.remove(0)    # print error message or raise exception
dl.add(0,5)
print(dl)   # print [5]
dl.add(0,1)
print(dl)   # print [1,5]
dl.add(1,3)
print(dl)   # print [1,3,5]
dl.add(2,6)
print(dl)   # print [1,3,6,5]
dl.remove(2)
print(dl)   # print [1,3,5]
dl.add(1,2)
print(dl)   # print [1,2,3,5]
dl.add(3,4)
print(dl)   # print [1,2,3,4,5]
dl.append(6)
print(dl)   # print [1,2,3,4,5,6]
dl.set(5,1)
print(dl)   # print [1,2,3,4,5,1]
dl.remove(3)
print(dl)   # print [1,2,3,5,1]
print(dl.isPalindrome())    # print False
dl.set(1,5)
print(dl)   # print [1,5,3,5,1]
print(dl.isPalindrome())    # print True'''
