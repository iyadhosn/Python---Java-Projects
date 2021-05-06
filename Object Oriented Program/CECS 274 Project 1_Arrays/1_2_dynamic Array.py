

from utils import new_array
from utils import _new_array


class DynamicArray:

    def __init__(self):
        self.A = new_array(1)
        self.n = 0
        self.capacity = len(self.A)

    def insert(self, k, value):
        # If the capacity of the array A is full then it will create a
        # new array called B which is empty but can store double the capacity
        # (_new_array would be imported from utils)

        if self.n == self.capacity:
            self.B = _new_array(2 * self.capacity)
            print(self.B)
            print(self.A)

            # Iterate through the loop inserting all the elemnts before index
            # k into array B and then inserting the value and index k and continuing
            # to insert the rest of the values after index k in array B
            C = 0
            for i in range(len(self.A)):
                if i  - 1== k:
                    self.B[C] = value
                    C += 1
                self.B[C] = self.A[i - 1]
                C += 1
            self.A = self.B
            self.capacity = len(self.B)
            self.n += 1

        else:
            '''for j in range(self.n, k, -1):
                self.A[j] = self.A[j - 1]'''
            self.A[k] = value
        self.n += 1

    def __str__(self):
        s = "["
        for i in range(self.n):
            s += "%r" % self.A[i]
            if i < self.n - 1:
                s += ","
        s += "]"
        return s


dynamic_array = DynamicArray()
dynamic_array.insert(0, 2)
dynamic_array.insert(0, 1)
dynamic_array.insert(0, 3)
#dynamic_array.insert(1, 4)

print(dynamic_array)



    

