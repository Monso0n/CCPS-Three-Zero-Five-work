import math

def getName():
	return "Kainth, Mayank"

class MyHeap():
    def __init__(self, array):
        # Create a heap from the passed array. The first element should be None.
        #print(f"Passed array: {array}")

        self.size = 0
        self.heap = [None]
        self.heapMaintained = False

        for i in array:
            self.insert(i)

        #print(f"final heap:{self.getData()}")

    def insert(self, data):
        # Insert an item in to the heap.
        # This method should be ablei A to handle items above and beyond the initial capacity
        self.heapMaintained = False
        self.heap.append(data)
        self.size+=1
        if self.size != 1: self.heapify(self.size)

    def heapify(self, i):
        p = i//2
        u = p + 1

        if  self.heap[p] < self.heap[i]:
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            if p!=1: self.heapify(p)

        if self.heap[u] < self.heap[i]:
            self.heap[i], self.heap[u] = self.heap[u], self.heap[i]
            if u>1: self.heapify(u)

        self.heapMaintained = True

    def extractMax(self):
        # Return the largest item in the heap, but ensure that the heap property is maintained
        data = self.heap[1]

        self.heap = self.heap[2:]
        copy = self.heap
        #"copy array: {copy}")
        self.size = 0
        self.heap = [None]

        for i in copy:
            self.insert(i)

        return data

    def __len__(self):
        # Return the number of items currently in the heap
        return len(self.heap) - 1

    def getData(self):
        # Return the current heap as an array that does not use the first value
        return self.heap[1:]


a = [1,2,3,4,5]
b = MyHeap(a)
print(b.extractMax())
print(b.getData())