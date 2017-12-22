from string import ascii_uppercase

class levenCheck():
    def __init__(self,words, word):
        self.wordDict = words
        self.result = []
        self.stack = [word]
        self.count = 0

    def levenFinder(self, word):
        while len(self.stack) != 0:
            word = self.stack.pop()
            self.insertLetter(word)
            self.deleteLetter(word)
            self.substituteLetter(word)


    def insertLetter(self,word):
        for index in len(word):
            for letter in ascii_uppercase:
                temp = list(word)
                temp = temp.insert(index,letter)
                temp = ''.join(temp)
                if self.wordsDict.contains(temp) and temp not in self.result:
                    self.result.append(temp)
                    self.stack.append(temp)
                    self.count+=1

    def deleteLetter(self,word):
        for index in len(word):
            temp = list(word)
            temp.pop(index)
            temp = ''.join(temp)
            if self.wordsDict.contains(temp) and temp not in self.result:
                self.result.append(temp)
                self.stack.append(temp)
                self.count+= 1

    def substituteLetter(self,word):
        for index in len(word):
            for letter in ascii_uppercase:
                temp = list(word)
                temp[index] = letter
                temp = ''.join(temp)
                if self.wordsDict.contains(temp) and temp not in self.result:
                    self.result.append(temp)
                    self.stack.append(temp)
                    self.count += 1

    def levenSize(self):
        return self.count