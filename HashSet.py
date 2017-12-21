from collections import defaultdict
import hashlib

class hashSet():
    def __init__(self):
        self.words = defaultdict(list)
        self.hcapacity = 100
        self.hsize = 0

    def readWords(self, fileName):
        file = open(fileName, "r")
        for line in file.readlines():
            line = line.strip('\n')
            self.addWord(line)


    def addWord(self, word):
        hashed = hashlib.md5(word.encode())
        hashed = int(hashed.hexdigest(), 16) % self.hcapacity
        self.words[hashed].append(word)

    def contains(self, word):
        hashed = hashlib.md5(word.encode())
        hashed = int(hashed.hexdigest(), 16) % self.hcapacity
        if word in self.words[hashed]:
            return True
        return False

    def printWords(self):
        print(self.words)

hSet = hashSet()

hSet.readWords("very_small_test_dictionary.txt", )

hSet.printWords()

print(hSet.contains("LUSTY"),hSet.contains("LUSTER"))