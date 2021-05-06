
class priorityQueue:
    def __init__(self):
        self.heap = []              # an array of integers
        self.size = 0               # the size of heap

    def __len__(self):
        return self.size

    def parent(self, index):
        return (index - 1) // 2
        
    def leftChild(self, index):
        return (2 * index) + 1
        
    def rightChild(self, index):
        return (2 * index) + 2
        
    def swap(self, index1, index2):
        # Switch position of values at the two indexes
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def insert(self, x):
        # appends value x to back of array
        self.heap.append(x)
        self.size += 1
        index = self.heap.index(x)
        while index > 0:
            # Compare the value inserted to the value of its parent. If it is greater than its parent then we swap and
            # repeat until the max heap requirments are satisfied.
            if self.heap[index] > self.heap[self.parent(index)]:
                self.swap(index, self.parent(index))
                index = self.parent(index)
            else:
                return


    def delete_Max(self):
        if self.size == 0:
            return print("Priority Queue is empty")
        Max = self.heap[0]
        # Swaps the root with the bottom right most value of the tree/heap
        self.heap[0] = self.heap[-1]
        # Deletes the root node at the end of the heap
        self.heap.pop()
        self.size -= 1
        index = 0
        # Once the max value is deleted, the value that was swapped with it gets comapred to its children. The bigger of
        # the two children take its place and the cycle repeats until the requirements for a max value heap is satisfied.
        while (self.heap[index] < self.heap[self.leftChild(index)]) or (self.heap[index] < self.heap[self.rightChild(index)]):
            if self.heap[self.leftChild(index)] > self.heap[self.rightChild(index)]:
                self.swap(self.leftChild(index), index)
                index = self.leftChild(index)
                if self.rightChild(index) >= self.size or self.leftChild(index) >= self.size:
                    break
            elif self.heap[self.leftChild(index)] < self.heap[self.rightChild(index)]:
                self.swap(self.rightChild(index), index)
                index = self.rightChild(index)
                if self.leftChild(index) >= self.size or self.rightChild(index) >= self.size:
                    break
        return Max

#Test case
h = priorityQueue()
h.insert(22)
h.insert(31)
h.insert(12)
h.insert(46)
h.insert(37)
h.insert(32)
print(h.heap)
x = h.delete_Max()
print(h.heap)
x = h.delete_Max()
h.insert(66)
h.insert(42)
h.insert(56)
print(h.heap)
x = h.delete_Max()
h.insert(41)
h.insert(121)
print(h.heap)
x = h.delete_Max()
print(h.heap)
# Default outputs:
#[46, 37, 32, 22, 31, 12]
#[37, 31, 32, 22, 12]
#[66, 32, 56, 22, 31, 12, 42]
#[121, 56, 42, 32, 31, 12, 41, 22]
#[56, 32, 42, 22, 31, 12, 41]