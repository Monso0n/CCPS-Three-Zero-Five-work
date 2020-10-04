# You may not use dicts.
def getName():
	return "Kainth, Mayank"
	
class MyHashTable():

    def __init__(self, size, hash1): #44
        # Create an empty hashtable with the size given, and stores the function hash1
        self.size = size
        self.hash = hash1
        self.itemCount = 0
        self.hashtable = [] * self.size
        print(f"created hashtable of size {self.size}")

    def put(self, key, data = None): #54, 65
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the table should not be changed
        index = self.hash(key)
        self.data = data if data != "" else None

        print(f"the index for the key({key}) is {index}")
        print(f"the data passed is '{self.data}'")

        if self.hashtable[index] is None:
            self.hashtable[index] = self.data
            self.itemCount+=1
            print(f"self.hashtable[{index}] = '{self.data}'  ||    itemcount: {self.itemCount} \n")
            return True
        else:
            return False

    def get(self, key): #75
        # Returns the item linked to the key given, or None if element does not exist
        print(f"getting data from key {key} which is index {self.hash(key)}")
        index = self.hash(key)

        print(f"will be returning: {self.hashtable[index]}")

        if self.hashtable[index] is not None:
            return self.hashtable[index]
        else:
            return None


    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.itemCount

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        print(f"size: {self.size} and len: {self.__len__()}")

        if self.size == self.__len__() - 1:
            return True
        else:
            return False

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)
        pass
    
    def put(self, key, data):
        # Store the data with the key given in a list in the table, return true if successful or false if the data cannot be entered
        # On a collision, the data should be added to the list
        tuple = (key, data)
        index = self.hash(key)
        self.data = data if data != "" else None

        print(f"the index for the key({key}) is {index}")
        print(f"the data passed is '{self.data}'")

        if self.hashtable[index] is None:
            self.hashtable[index] = self.data
            self.itemCount+=1
            print(f"self.hashtable[{index}] = '{self.data}'  ||    itemcount: {self.itemCount} \n")
            return True
        else:
            return False



    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        index = self.hash(key)

        print(f"getting data with key {key} at index {index}")
        print(f"{self.hashtable[index]}")


        if len(self.hashtable[index]) == 0:
            return None
        else:
            for i in len(self.hashtable[index]):
                if self.hashtable[index][i][0] == key:
                    return self.hashtable[index][1]
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        super().__len__()

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        super().isFull()

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.hash1 = self.hash
        self.hash2 = hash2

    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination of the first and second hash functions
        # Be careful that your code does not enter an infinite loop
        if super().isFull():
            return None
        else:
            index = self.hash(key)
            if len(self.hashtable[index]) == 0:
                self.hashtable[index] == [data]


    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        super().get(key)
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        pass

#f = lambda a: a % 10
#a = MyHashTable(10, f)
#a.put(12, "big pp")
#print(a.get(12))