import heapq

def getName():
	return "Kainth, Mayank"

# This node structure might be useful to you
class Node:
    def __init__(self,value,data,left=None,right=None):
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False

    def __le__(self, other):
        if self.value <= other.value:
            return True
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        return False

    def __ge__(self, other):
        if self.value >= other.value:
            return True
        return False

class MyHuffman():


    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        #print("Building huffman tree with dictionary {}".format(weights))

        self.heap = []  # create and empty heap
        def printHeap():
            for i in self.heap:
                print("{}/{}".format(i.value, i.data))

        for i in weights: # poulate heap with leaf nodes
            self.heap.append(Node(weights[i], i))
            #print(f"added node {weights[i]}/{i}")

        heapq.heapify(self.heap)



        #printHeap()

        while True:
            a = heapq.heappop(self.heap)
            b = heapq.heappop(self.heap) if len(self.heap) > 0 else None
            sum = a.value + b.value if b is not None else a.value
            heapq.heappush(self.heap, Node(sum, None, a, b))
            #   print(f"The Node with L:{a.value} and R:{b.value} has been created with value{sum}")

            if len(self.heap) == 1:
                break

        print("Finished building Huffman Tree for passed word")

    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        #print(f"The word that was passed is {word}")

        self.word = word
        dict = {}
        for i in word: dict[i] = word.count(i)
        #print(f"Dictionary: {dict}")

        self.build(dict) #build a huffman tree
        self.reference = {} #create a dictionary of references to speed up encoding the word
        encodedWord, self.code = "", ""

        def fillReference(node):
            if node.data is not None:
                self.reference[node.data] = self.code

            if node.left is not None:
                self.code += "1"
                fillReference(node.left)
                self.code = self.code[:-1]

            if node.right is not None:
                self.code+="0"
                fillReference(node.right)
                self.code = self.code[:-1]

        fillReference(self.heap[0])

        for i in word:
            encodedWord += self.reference.get(i)

        print(f"the bitcode for the word {word} is: {encodedWord}  lenght: {len(encodedWord)}")
        print(self.reference)
        self.solutions[encodedWord] = word
        return encodedWord



    def decode(self, bitstring):
        # Return the word encoded in bitstring, or None if the code is invalid
        if self.solutions.has_key(bitstring):
            return self.solutions[bitstring]
        return None





a = MyHuffman()
