from levenChecker import levenCheck
from HashSet import hashSet

#Class called socialNetwork which takes a file name and a word to find it's social network
#Imports levenCheck which is used to find the word's social network by inserting/deleting/substituting a letter to see if the distance is 1
#Imports HashSet which is what I used to store the dictionary.txt
class socialNetwork():
    def __init__(self, file):
        self.wordsDict = hashSet(file)

    #method to cal levenCheck in order to determine the word's network size
    def findNetworkSize(self, word):
        leven = levenCheck(self.wordsDict,word)
        leven.levenFinder()
        size = leven.levenSize()
        return size


#Sequence to set up the social network and find the word's network size
if __name__ == "__main__":
    print("Test for very_small_test_dictionary.txt:\n")
    network = socialNetwork("very_small_test_dictionary.txt")

    test1 = network.findNetworkSize("LISTY")
    print("LISTY's social network size: {}".format(test1))
    print("Correct Answer: 5")
    if (test1 == 5):
        print("Correct answer has been found\n")

    test1 = network.findNetworkSize("HUBERT")
    print("HUBERT's social network size: {}".format(test1))
    print("Correct Answer: 0")
    if (test1 == 0):
        print("Correct answer has been found\n")

    print("Test for original_test_dictionary.txt:\n")
    network = socialNetwork("original_test_dictionary.txt")

    test2 = network.findNetworkSize("HI")
    print("HI's social network size: {}".format(test2))
    print("Correct Answer: 7")
    if (test2 == 7):
        print("Correct answer has been found\n")

    print("Social Network built on dictionary.txt:\n")
    network = socialNetwork("dictionary.txt")
    listy = network.findNetworkSize("LISTY")
    print("LISTY's social network size: {}".format(listy))

