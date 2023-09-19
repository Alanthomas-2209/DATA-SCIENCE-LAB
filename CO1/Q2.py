sentence = input("Enter the Sentence: ").replace(" ","")
countOfCapital = 0
countOfSmall = 0
for x in sentence:
    if x.isupper():
        countOfCapital+=1
    elif x.islower():
        countOfSmall+=1
print("Count of Capital Letter :",countOfCapital,"Count of Small Letter :",countOfSmall)