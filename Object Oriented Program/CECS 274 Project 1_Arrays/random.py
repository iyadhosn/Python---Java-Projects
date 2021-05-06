class DynamicArray:
     
     def __init__(self):
          self.a = [1]
          self.n = 0
          self.capacity = len(self.a)


     def resize(self, capacity):
          self.a = resize(self.a, capacity, self.n)
          self.capacity = capacity
          
     def insert(self, k, value):
  
          if self.n== self.capacity:

               self.resize(2 * self._apacity)
               for j in range(len(a)):

                    self.a[j] = valuea[j+1]
                    
               self.a[k] = value
               self.n += 1


     def __str__(self):
          s = "["
          for i in range(self.n):
               s +="%r" % self.a[i]
               if i < self.n-1:
                    s +=  ","
          s += "]"
          return s




dynamic_array = DynamicArray()


'''dynamic_array.insert(0, 2)
dynamic_array.insert(0, 1)
dynamic_array.insert(0, 3)'''
dynamic_array.insert(1, 4)


print(dynamic_array)
