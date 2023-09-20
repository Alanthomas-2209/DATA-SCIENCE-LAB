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

print(subStringChecker(word, inputList))