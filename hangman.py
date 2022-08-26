import random

#Lword = ["two","up","use","very","want","way",'we',"well",'what','when','which','who','will','with','would','year',"you","your"]
Lword = ["two","up","use"]

word = random.choice(Lword)
word1 = list(word)
lw=[]
for j in range(len(word1)):
    lw.append('-')
i=0
live =7

while len(word1)!=i:
    x = str(input("enter name :"))
    while x not in word1 :
        live -= 1
        if live == 0:
            print(f"you lose !! {live} live,your word is {word}")
            exit(0)

        else:
            print("try agine")
            x = str(input(f"you still have {live} lives:"))

    else:

        if x in word1:
            lw[word1.index(x)]=word1[word1.index(x)]
            print("".join(lw))
            i+=1

print(f"your word is {word}")

	
