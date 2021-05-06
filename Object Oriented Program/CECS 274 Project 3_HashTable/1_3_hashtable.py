import math
class Node(object):
    def __init__(self, k, d):
        self.key = k
        self.data = d

    def __str__(self):
        return str(self.key) +": " + str(self.data)

class HashTab(object):
    def __init__(self, size):
        self.Array1 = [None] * (size // 2)
        self.Array2 = [None] * (size // 2)
        self.numRecords = 0
        self.size = size

    def hashFunc(self, key):
        #Hash function just mods the key passed by the size of the array
        return key % (self.size // 2)

    def hashFunc2(self, key):
        #A Hash function that uses a different method to return an index
        return (key**3) % (self.size // 2)

    def insert(self, key, value):
        node = Node(key, value)
        h = self.hashFunc(key)
        h2 = self.hashFunc2(key)
        #Checks if the idnex is equal to none and if it is it inserts that node into that index
        if self.Array1[h] == None:
            self.Array1[h] = node
        #If the index in Array1 is not empty. We take out what is in that index. Insert the new node and then pass
        # the one we took out into the second Array where it is given a different index from the different hash fucntions
        elif self.Array2[h2] == None:
            OG = self.Array1[h]
            self.Array1[h] = node
            self.Array2[h2] = OG
        #If the index in Array2 is not none then we know that we will have mutliple collsions going back and forth from Array1 to Array2 so we fix this by rehashing.
        else:
            self.rehash(self.size)
            #self.insert(key, value)



    def print(self):
        #Prints both tables
        print("First Hash Table: ")
        for i in self.Array1:
            print(i, end="; ")
        print()
        print()
        print("Second Hash Table: ")
        for j in self.Array2:
            print(j, end="; ")
        print()
        print()



    def rehash(self, size): #rehash when tables are full

        #Create 2 new empty arrays double the size of the original
        A = [None] * ((size // 2) * 2)
        B = [None] * ((size // 2) * 2)
        #Traverse the first array passing all the elements inside it through the hashfunction that will a return a new
        #index for them in the new array
        for i in self.Array1:
            if i == None:
                continue
            A[self.hashFunc(i.key)] = i
        # Traverse the second array passing all the elements inside it through the hashfunction that will a return a new
        # index for them in the new array
        for j in self.Array2:
            if j == None:
                continue
            B[self.hashFunc2(j.key)] = j
        #Reassign the new arrays to the names of the origal where theire new values in new indexes
        self.Array1 = A
        self.Array2 = B

    def lookup(self, key):
        # Case when their is nothing to delete because the array is empty
        if self.size == 0:
            return print("The table is empty there is no value to look up.")
        h = self.hashFunc(key)
        h2 = self.hashFunc2(key)
        #Checks if the key in Array1 matches the key at that index. It then returns the data at the key
        if self.Array1[h].key == key:
            return self.Array1[h].data
        # Checks if the key in Array2 matches the key at that index. It then returns the data at the key
        elif self.Array2[h2].key == key:
            return self.Array2[h2].data
        #Case where that key does not exist
        else:
            return print("That key value pair does not exist")

    def delete(self, key):
        #Case when their is nothing to delete because the array is empty
        if self.size == 0:
            return print("The table is empty there is no value to look up.")
        h = self.hashFunc(key)
        h2 = self.hashFunc2(key)
        #Checks if the key in Array1 matches the key at that index. It then replaces it with None deleting it from the array.
        if self.Array1[h].key == key:
            self.Array1[h] = None
        #Checks if the key in Array1 matches the key at that index. It then replaces it with None deleting it from the array.
        elif self.Array2[h2].key == key:
            self.Array2[h2] = None
        # Case where that key does not exist
        else:
            return print("That key value pair does not exist")

def test():
    # Your test case is here, note please put the desired correct outputs of your test case
    ht = HashTab(11)
    ht.insert(44, "Iyad")
    ht.insert(22, "Shadya")
    ht.insert(31, "Ihab")
    ht.insert(41, "Hadi")
    ht.insert(42, "Moni")
    ht.insert(41, "Rima")
    ht.delete(44)


    ht.print()
    print("Value returned when key 22 is looked up: ", ht.lookup(22))
    print("Value returned when key 41 is looked up: ", ht.lookup(41))

def __main():
    test()
    
if __name__ == '__main__':
    __main()       




