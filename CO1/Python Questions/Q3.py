#3.	Write a Python program to replace vowels with ‘*’ in the given text.

sentence = input("Enter the Sentence: ")
newSentence =""

for x in sentence:
    if x in "AEIOUaeiou":
        newSentence += "*"
    else:
        newSentence += x
        
print("orginal Word: ",sentence,"\nReplaced Word: ",newSentence)