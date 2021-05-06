'''
Zaineb Halibi
Project 1 : Array-Based Lists
Part 1
'''
from utils import new_array
from base import BaseList
class ArrayStack(BaseList):

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self): #set all our variables
        self.a = new_array(1)
        self.n = 0
        self.capacity = len(self.a)

    def get(self, i):
        return self.a[i]

    def set(self, i, x):
        y = self.a[i]
        self.a[i] = x
        return y

    '''Creates a new array b which is double the size of the old one 
        then replaces elements from a to be leaving the space doubled. 
        Then sets a equal to b.
    '''
    def add(self, i, x):
        if self.n == len(self.a):
            self.resize()
        for j in range(self.n-1, i-1 , -1):
            self.a[j+1] = self.a[j]
        self.a[i] = x
        self.n += 1

    def remove(self, i):
        x = self.a[i]
        for i in range (i, self.n+1):
            self.a[i] = self.a[i+1]
        self.n -= 1

    '''Creates a new array b which is double the size of the old one 
        then replaces elements from a to be leaving the space doubled. 
        Then sets a equal to b.
    '''
    def resize(self):
        b = new_array(max(1, 2*self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

stack = ArrayStack()
stack.add(0,1)
stack.add(0,2)
stack.add(1,3)
stack.add(3,5)
stack.add(2,4)
print(stack.get(0))
print(stack.get(1))
print(stack.get(2))
print(stack.get(3))
print(stack.get(4))

