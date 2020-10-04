def getName():
	return "Kainth, Mayank"

class MyTrie:
    def __init__(self):
        # Initialize the trie node as needed
        self.trie = {"*": -1} # this is the root node
        print("Trie has been initialized, innit \n")


    def insert(self, word):
        # Insert a word into this trie node
        self.pointer = self.trie
        #print(f"Inserting '{word}' into Trie")

        for char in word:
            if char not in self.pointer:
                self.pointer[char] = {} #instantiate dictionary if char not in trie

            self.pointer = self.pointer[char] # point to char in trie

        self.pointer["*"] = "*" #append star to end of last letter to signify complete word
        self.trie["*"] += 1
        self.pointer = self.trie

        #print(f"'{word}' has been added to the trie")
        #print(f"Trie: {self.trie} \n")

    def exists(self, word, position=0):
        # Return true if the passed word exists in this trie node
        # A terminal node will return true if the word passed is ""

        if position == 0:
            #print(f"checking if word '{word}' exists in Trie")
            self.pointer = self.trie # point to beginning of trie

        if position == len(word) - 1:
            if word[position] in self.pointer:
                self.pointer = self.pointer[word[position]]
                return self.isTerminal()
            return False
        elif word[position] not in self.pointer:
            #print(f"{word[position]} DOES NOT exist in {self.pointer}")
            return False
        else:
            #print(f"{word[position]} DOES exist in {self.pointer}  |  pos: {position}  lenword: {len(word)}")
            self.pointer = self.pointer[word[position]]
            position +=1

            return self.exists(word, position)


    def isTerminal(self):
        # Return true if this node is the terminal point of a word
        #print(f"Checking if Node{self.pointer} is a terminal node")
        x = "*" in self.pointer
        #print(f"Returning {x}")
        return x

    def autoComplete(self, prefix, position=0):
        # Return every word that extends this prefix in alphabetical order
        if position == 0:
            self.list = [] #innit list of words to return
            self.word = prefix #have word be prefix
            self.pointer = self.trie

            for ch in prefix:
                if ch in self.pointer:
                    self.pointer = self.pointer[ch]
                else:
                    print("prefix is not valid")
                    return False

        for i in self.pointer:
            #print(i)
            if i == "*":
                self.list.append(self.word)
                #print(f"added word '{self.word} in to list'")
                self.list = sorted(self.list)
            else:
                position += 1
                h = self.pointer
                self.pointer = self.pointer[i]
                self.word+=i

                self.autoComplete(self.word, position)

                position-=1
                self.word = self.word[:-1]
                self.pointer = h






        return self.list

    def __len__(self, pointer = None):
        # Return the number of words that either terminate at this node or descend from this node
        # A terminal leaf should have length 1, the node A with terminal child leaves B|C should have length 2
        if pointer is None:
            self.count = - 1
            pointer = self.pointer
            #print(f"finding len from pointer {pointer}")



        for i in pointer:
            if "*" == i:
                self.count+=1
            else:
                self.__len__(pointer[i])


        #print(f"returning {self.count}")
        return self.count



a = MyTrie()
a.insert("Hello")
a.insert("Hey")
a.insert("Help")
a.insert("Hellu")
a.insert("Hell")
a.pointer = a.pointer['H']
print(len(a))
print(a.autoComplete("H"))
a.insert("big pp")
print(a.autoComplete(""))
