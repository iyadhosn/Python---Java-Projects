class Node:
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class HashTable:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_by_Index(self, index, key, val):
        curr = Node(key, val)
        #Checks if index in DLL exists
        if index > self.size or index < 0:
            return print("That index does not exist.")
        #Case where we insert it at the fron of the DLL
        if index == 0:
            self.head.prev = curr
            curr.next = self.head
            self.head = curr
        #Case where we insert it at the end of the DLL
        elif index + 1 == self.size:
            self.tail.next = curr
            curr.prev = self.tail
            self.tail = curr
        #Case where we insert it into the center of the DLL
        else:
            front = self.head
            x = 0
            while index != x:
                front = front.next
                x += 1
            curr.prev = front.prev
            curr.next = front
            curr.next.prev = curr
            curr.prev.next = curr
        #Incrementing size by one
        self.size += 1

    def getValue_by_Index(self, index):
        #Traverse the DLL up to the given index and returns the value of that node at that index
        curr = self.head
        x = 0
        while x != index:
            curr = curr.next
            x += 1
        return curr.val
                
    def getValue_by_Key(self, key):
        #Traverses the DLL comparing each key at each node until it finds the correct node. It then returns the value at that node
        curr = self.head
        while curr.key != key:
            curr = curr.next
        return curr.val

    def delete_by_Value(self, val):
        curr = self.head
        # Checks if the DLL is empty
        if self.size == 0:
            return print("There DLL is empty.")
        while curr is not None:
            #Traverses the DLL until we find a mode with a matching value
            if curr.val != val:
                curr = curr.next
            #Case where the value we have to delete is in the first node
            elif curr.val == val and curr.prev == None:
                self.head = curr.next
                self.size -= 1
                return
            #Case where the value we have to delete is the last node
            elif curr.val == val and curr.next == None:
                self.tail = curr.prev
                self.tail.next = None
                self.size -= 1
                return
            #Case where the value we have to delete is in the center if the DLL
            elif curr.val == val:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.size -= 1
                return
        #This statement is printed when we traverse the DLL and cannot find that value
        print("There is no val", val, "to be deleted.")


    def delete_by_Index(self, index):
        curr = self.head
        #Checks if the DLL is empty
        if self.size == 0:
            return print("There DLL is empty.")
        #Checks if the index exists in the DLL
        if index > self.size or index < 0:
            return print("That index does not exist.")
        x = 0
        while index != x:
            curr = curr.next
            x += 1
            #Deletes the node at the start of the DLL
        if curr.prev == None:
            self.head = curr.next
            self.size -= 1
            #Deletes the node at the end of the DLL
        elif curr.next == None:
            self.tail = curr.prev
            self.tail.next = None
            self.size -= 1
            #Deletes the node in the midlle of two nodes
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            #Decreasing the size by one
            self.size -= 1

    def delete_by_Key(self, key):
        curr = self.head
        #Checks if the DLL is empty
        if self.size == 0:
            return print("There DLL is empty.")
        while curr is not None:
            #Traverses through the DLl until we get to the node with the same key as the arguement
            if curr.key != key:
                curr = curr.next
            #Case where we have to delete the first node of the DLL
            elif curr.key == key and curr.prev == None:
                self.head = curr.next
                self.size -= 1
                return
            #Case where we have to delete the last node of the DLL
            elif curr.key == key and curr.next == None:
                self.tail = curr.prev
                self.tail.next = None
                self.size -= 1
                return
            #Case where the node we are deleting is in the middle
            elif curr.key == key:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.size -= 1
                return
        #If that key does not exist it prints the following statement
        print("There is no key", key, "to be deleted.")

    def print_all_keyValues(self):
        #Traverses the DLL printing each node inside of it.
        curr = self.head
        while curr is not None:
            print({curr.key: curr.val})
            curr = curr.next

    def insert_at_First(self, key, val):
        curr = Node(key, val)
        #Checks if length is zero for the DLL in which it makes the node the head and the tail
        if self.size == 0:
            self.head = curr
            self.tail = curr
        else:
            #inserts the node at the front of the DLL and increments the size by one.
            self.head.prev = curr
            curr.next = self.head
            self.head = curr
        self.size += 1

    def insert_at_Last(self,key,val):
        curr = Node(key, val)
        # Checks if length is zero for the DLL in which it makes the node the head and the tail
        if self.size == 0:
            self.head = curr
            self.tail = curr
        else:
            #Inserts the node at the end of the DLL and increments the size by one
            self.tail.next = curr
            curr.prev = self.tail
            self.tail = curr
        self.size += 1

    def length(self):
        if self.head != None and self.tail != None:
            return self.size
        else:
            return "Note: Table is Empty!"

# test cases               
d1 = HashTable()
d1.insert_at_First("csulb", 1)
d1.insert_at_First("CECS", 2)
d1.insert_at_First("CECS274", 3)
d1.insert_at_Last("CS", 4)
d1.insert_by_Index(1, "life", 12)
d1.insert_by_Index(0, "time", 44)
d1.insert_by_Index(3, "value", 22)
d1.insert_by_Index(4, "good", 26)
d1.insert_by_Index(4, "eng", 27)
d1.delete_by_Value(8)
d1.delete_by_Index(4)
d1.delete_by_Key("time")
d1.insert_at_First("why",24)
d1.insert_at_Last("how",57)
d1.insert_by_Index(3,"know",145)
d1.insert_by_Index(4,"yes",243)
print("HashTable: ", end="\n")
d1.print_all_keyValues()
print("Length:", d1.length())
print("Value at Key 'value':", d1.getValue_by_Key("value"))
print("Value at Key 'csulb':",d1.getValue_by_Key("csulb"))
print("Value at index 3:",d1.getValue_by_Index(3))
print("Value at index 7:",d1.getValue_by_Index(7))





