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
        self.value = [None] * self.size
        print(f"created hashtable of size {self.size}")

    def put(self, key, data = None): #54, 65
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the table should not be changed
        index = self.hash(key)
        self.data = data

        print(f"the index for the key({key}) is {index}")
        print(f"the data passed is '{self.data}'")
        print(f"len at index is: {len(self.hashtable[index])}")

        if len(self.hashtable[index]) == 0:
            self.hashtable[index] = [self.data]
            self.itemCount+=1
            print(f"self.hashtable[{index}] == '{self.data}'  ||    itemCount is now: {self.itemCount} \n")z
            return True
        elif len(self.hashtable[index]) == 1:
            self.hashtable[index] = [self.data]
            print(f"Returning false because the data {self.hashtable[index][0]}: already occupies {index} \n")
            return False

    def get(self, key): #75
        # Returns the item linked to the key given, or None if element does not exist
        print(f"getting data from key {key} which is index {self.hash(key)}")
        index = self.hash(key)

        printer = self.hashtable[index][0] if self.hashtable[index][0] != "" else None

        print(f"Index Data: {printer} \n")

        if len(self.hashtable[index]) == 0 or self.hashtable[index][0] == "":
            return None
        else:
            return self.hashtable[index][0]


    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.itemCount

    def isFull(self):
        # Returns true if the HashTable cannot accept new members

        print(f"self.size:: {self.size}     self.len():: {self.__len__()} ")
        if self.size == self.__len__():
            return True
        else:
            return False

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)
        print("Created CHAIN HASHTABLE")

    
    def put(self, key, data):
        # Store the data with the key given in a list in the table, return true if successful or false if the data cannot be entered
        # On a collision, the data should be added to the list
        tuple = (key, data)
        index = self.hash(key)
        print(f"key of {key} and data of {data} was passed to create tuple {tuple}")
        self.hashtable[index].append(tuple)


        self.itemCount += 1
        print(f"len of self.hashtable[{index}] is {len(self.hashtable[index])}  || total items in hashtable is {self.itemCount}")
        print(f"Chain hashtable at index {index} is: {self.hashtable[index]} \n")
        return True

    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        index = self.hash(key)

        print(f"getting data with key {key} at index {index}")
        print(f"{self.hashtable[index][0][1]}")
        for i in self.hashtable[index]:
            if i[0] == key:
                return i[1]
        return None


    def __len__(self):
        # Returns the number of items in the Hash Table
        print(f"returning {super().__len__()}")
        return super().__len__()

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        super().isFull()

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        super().__init__(size,hash1)
        self.hash1 = self.hash
        self.hash2 = hash2
        print("DOUBLE HASH TABLE CREATED \n")

    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination of the first and second hash functions
        # Be careful that your code does not enter an infinite loop
        print(f"Trying to put data {data} with key {key}")
        pair = (key,data)

        if self.size == self.__len__:
            return False

        index = self.hash1(key)

        if len(self.hashtable[index]) == 0:
            self.hashtable[index].append(pair)

            print(self.hashtable)
            return True
        else:
            for i in range(self.size):
                index = (index + i*self.hash2(key)) % self.size

                print(f"new index = {index}")
                print(len(self.hashtable[index][0]))

                if len(self.hashtable[index]) == 0:
                    self.hashtable[index] = [pair]
                    print(f"appended {pair} to index {index} \n")
                    return True
            return False



    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist
        pass

    def __len__(self):
        # Returns the number of items in the Hash Table
        return self.itemCount

#f = lambda a: a % 10
#a = MyHashTable(10, f)
#a.put(12, "big pp")
#print(a.get(12))