
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, numBuckets):
        self.MAX = numBuckets
        self.array = [[] for i in range(self.MAX)]

    def simple_hash(self, key):
        #Adds up each individual letter from the ASCII table and MODS it by the size of the array
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.MAX

    def double_hash(self, key):
        i = 0
        #h and h2 will both return their own unique index
        h = self.simple_hash(key)
        h2 = 7 - (h % 7)
        # modded hash is the function we will use to return an empty index for the double hash
        moddedHash = h + (i * h2)
        #Checks if the index modded hash returned is equal to [] if its not we increment i by one and redo the function until we find an index that is empty.
        #We then return that index
        while self.array[moddedHash] != []:
            i += 1
            moddedHash = ((h + (i * h2)) % 11)
        return moddedHash

    def add(self, key, value, method):
        #Passes the key into our first hash function
        h = self.simple_hash(key)
        #If method is equal to 1 we solve our collisions with seperate chaining
        if method == 1:
            self.array[h].append((key, value))
        #If method is equal to 2 we solve our collisions with double hashing
        if method == 2:
            #Whatever index is returned from our double hash function is used as the index where we will insert out key value pair
            self.array[self.double_hash(key)].append((key, value))


    def updateValue(self, key, value):
        #h is the index at which we will update the value
        h = self.simple_hash(key)
        #Checks if at index h their is a key value pair and that the key that we were asked to update matches the key that was passed.
        #It then replaces the value
        for idx, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                self.array[h][idx] = (key, value)
                break

    def delete(self, key):
        h = self.simple_hash(key)
        x = -1
        #Traverese the array until we get to the index with the right key
        #We then pop what is in that index deleting it from the array.
        for element in self.array[h]:
            x += 1
            if element[0] == key:
                self.array[h].pop(x)
            return
        print("That key value pair does not exist.")
    
    def lookUp(self, key):
        h = self.simple_hash(key)
        #Traverses the array until we get to an index where the key matches what was passed
        #Returns the value at that specific key
        for element in self.array[h]:
            if element[0] == key:
                return element[1]
        return print("That key value pair does not exist.")
        
    def _print(self):
        #Traverse the array printing each index
        x = 0
        for i in self.array:
            print(x, i)
            x += 1

if __name__ == '__main__':

    #___NOTE___:
    #When you test both cases make sure to comment the other one completely out!!!

    print("Test 1: Separate Chaining ")
    ht_1 = HashTable(11)
    ht_1.add("Iyad", 78, 1)
    ht_1.add("Ihab", 67, 1)
    ht_1.add("Moni", 4, 1)
    ht_1.add("Firas", 459, 1) #Collides with Iyad because same Index: Separate Chaining
    ht_1.add("Tyler", 44, 1)
    ht_1.add("Tymor", 13, 1) #Collides with Tyler because same Index: Separate Chaining
    ht_1.add("Reebal", 1, 1)
    ht_1.delete("Iyad")
    ht_1.add("Rashad", 88, 1)
    ht_1.updateValue("Ihab", 999) #Updates the value of specific key
    ht_1.add("Katya", 33, 1) #Collides with Tyler and Tymor because same Index: Separate Chaining
    ht_1.add("Mia", 105, 1) #Collides with Reebal because same Index: Separate Chaining
    ht_1.add("Shadya", 20, 1)
    ht_1.add("Julian", 365, 1) #Collides with Iyad and Firas because same Index: Separate Chaining
    ht_1.add("Maysa", 211, 1) #Collides with Rashad because same Index: Separate Chaining
    ht_1.updateValue("Maysa", 907)
    ht_1.delete("Katya")
    ht_1._print()
    print("Value returned when key Maysa is looked up: ", ht_1.lookUp("Maysa"))
    print("Value returned when key Julian is looked up: ", ht_1.lookUp("Julian"))
    print("Value returned when key Moni is looked up: ", ht_1.lookUp("Moni"))

    # print("Test 2: Double Hashing")
    # ht_2 = HashTable(11)
    # ht_2.add("Iyad", 78, 2)
    # ht_2.add("Ihab", 67, 2)
    # ht_2.add("Moni", 4, 2)
    # ht_2.add("Firas", 459, 2)
    # ht_2.add("Tyler", 44, 2)
    # ht_2.add("Tymor", 13, 2)
    # ht_2.add("Reebal", 1, 2)
    # ht_2.add("Rashad", 88, 2)
    # ht_2.add("Katya", 33, 2)
    # ht_2.add("Mia", 105, 2)
    # ht_2.add("Shadya", 20, 2)
    # ht_2.delete("Iyad")
    # ht_2._print()
    # print("Value returned when key Moni is looked up: ", ht_2.lookUp("Moni"))
    # print("Value returned when key Iyad is looked up: ", ht_2.lookUp("Iyad"))


