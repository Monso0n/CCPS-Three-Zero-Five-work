# You may not use dicts.
def getName():
	return "Kainth, Mayank"
	
class MyHashTable():

    def __init__(self, size, hash1): #44
        # Create an empty hashtable with the size given, and stores the function hash1
        self.size = size
        self.hash = hash1
        self.itemCount = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size
        #print(f"Created hashtable of size {self.size}")

    def put(self, key, data = None): #54, 65
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the table should not be changed
        index = self.hash(key)

        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = data
            self.itemCount+=1
            #print(f"'{data}' has been added to the hashtable at index {index} \n")
            #print(f"self.hashtable[{index}] == '{self.data}'  ||    itemCount is now: {self.itemCount} \n")
            return True
        elif self.keys[index] is not None:
            #print(f"Returning false because the data {self.values[index]}: already occupies index {index} \n")
            return False

    def get(self, key): #75
        # Returns the item linked to the key given, or None if element does not exist
        #print(f"getting data from key {key} which is index {self.hash(key)}")
        index = self.hash(key)

        if self.keys[index] == key:
            #print(f"returned {self.values[index]} \n")
            return self.values[index]
        else:
            #print("Returned None \n")
            return None

    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.itemCount

    def isFull(self):
        # Returns true if the HashTable cannot accept new members

        #print(f"self.size:: {self.size}     self.len():: {self.__len__()} ")
        if self.size == self.__len__():
            return True
        else:
            return False

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        self.size = size
        self.hash = hash1
        self.itemCount = 0
        self.hashtable = [[]] * self.size
        #print(f"Created CHAINED HASHTABLE of size {self.size} \n")
    
    def put(self, key, data):
        # Store the data with the key given in a list in the table, return true if successful or false if the data cannot be entered
        # On a collision, the data should be added to the list
        index = self.hash(key)
        tuple = (key, data)

        #print(f"key of {key} and data of {data} was passed to create tuple {tuple} | looking to place in index{index}")
        self.itemCount += 1

        if self.hashtable[index] == []:
            self.hashtable[index] = [tuple]
            #print(f"index {index} now looks like {self.hashtable[index]} \n")
        else:
            self.hashtable[index].append(tuple)
            #print(f"index {index} now looks like {self.hashtable[index]} \n")

        return True



    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        #print(f"getting data from key {key} which is index {self.hash(key)}")
        index = self.hash(key)

        #print(f"All data: {self.hashtable[index]}")
        for i in self.hashtable[index]:
            if i[0] == key:
                #print(f"returning {i[1]} \n")
                return i[1]
        return None


    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.itemCount

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        return self.itemCount == self.size

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.hash2 = hash2
        #print("A DOUBLE HASHTABLE HAS BEEN CREATED \n")
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination of the first and second hash functions
        # Be careful that your code does not enter an infinite loop
        #print(f"Trying to insert data {data} with key {key}")


        if super().isFull():
            #print("returning false because full")
            return False

        for i in range(self.size):
            index = (self.hash(key) + i*self.hash2(key)) % self.size
            #print(f"index is {index} and key value at index is: {self.keys[index]}")
            if self.keys[index] is None:
                self.keys[index] = key
                self.values[index] = data
                self.itemCount+=1
                #print(f"the data {data} has been appended to index {index} \n")
                return True

        return False

    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        for i in range(self.size):
            index = (self.hash(key) + i * self.hash2(key)) % self.size

            if self.keys[index] == key:
                return self.values[index]
        return None
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.itemCount
