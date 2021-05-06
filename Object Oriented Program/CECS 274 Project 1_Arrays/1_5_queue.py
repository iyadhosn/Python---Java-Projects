class twoStack:
    def __init__ (self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):
        self.s1.append(x)

    def deQueue(self):
        if(len(self.s2) == 0):
            while(len(self.s1) != 0):
                self.s2.append(self.s1.pop())
        return self.s2


q = twoStack()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print(q.deQueue())
