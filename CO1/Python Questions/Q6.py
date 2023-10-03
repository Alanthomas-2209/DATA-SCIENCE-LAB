#6.	Given is a list of of words, wordlist, and a string, name. Write a Python function which takes wordlist and name as input and returns a tuple. 
#The first element of the output tuple is the number of words in the wordlist which have name as a substring in it. 
#The second element of the tuple is a list showing the index at which the name occurs in each of the words of the wordlist and a 0 if it doesn’t occur.

def subStringChecker(word, wordlist):
    count = 0
    resultList = []
    index = 1
    for x in wordlist:
        if word in x:
            count += 1
            resultList.append(index)
        index += 1
    return count, resultList

word = input("Enter the word to be searched: ")
inputList = input("Enter the words to be added to the list, separated by spaces: ").split(" ")
print("Output")

print(subStringChecker(word, inputList))