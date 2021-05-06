class ArrayQueue:

    
    def __init__(self):
        self.queue = list()
        self.Qsize = 1 
        self.start = 0
        self.finish = 0
        

    def Total_size(self):
        if self.finish >= self.start:
            return (self.finish - self.start)
        return (self.Qsize - (self.start - self.finish))    


    def enqueue(self,data):
        if self.Qsize == 0:
            return ("Qsize MUST be GREATER than 0!")
        else:
            for n in range(self.Qsize):
                new_Qsize = 0
            if self.Total_size() == self.Qsize-1:
                new_Qsize = self.Qsize * 2
                self.Qsize = new_Qsize
        self.queue.append(data)
        self.finish = (self.finish + 1) % self.Qsize
        return data

    
    def dequeue(self):
        if self.Total_size() == 0:
            return ("There are no more elements in this queue.") 
        data = self.queue[self.start]
        self.start = (self.start + 1) % self.Qsize
        return data

      
    


queue = ArrayQueue()

print('The queue size is: ', queue.Total_size())
print(queue.enqueue(5))
print(queue.enqueue(10))
print(queue.enqueue(15))
print(queue.enqueue(20))
print(queue.enqueue(25))
print('The queue size is: ', queue.Total_size())

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print('The queue size is: ', queue.Total_size())