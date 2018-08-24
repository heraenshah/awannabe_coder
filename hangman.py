import random
import string
def hangman():
    global word
    global p
    x="c:/wordsEn.txt"
    k=open(x,'r')
    lines=k.readlines()
    p=lines[random.randint(0,len(lines))]
    p=p.strip()
    word=list(p)
def guess(word):
    o=[]
    h=[]
    k='0'*len(word)
    l=list(k)
    print("The word is %d alphabets long" %len(k))
    tries=0
    left=6
    while tries!=7 and left!=0:
        x=input("\nWhat is your guess?")
        if x in h:
            print("letter already used")
            print("Guesses done till now:")
            for i in h:
                print("%s" %i,end="")
            continue
        h.append(x)
        if x not in string.ascii_letters or len(x)==0:
            print("Should be a letter -.-")
            continue
        elif x not in word:
            print("Your guess is wrong")
            tries=tries+1
            left=left-1
            print("You have %d incorrect tries left" %left)
            if tries>0:
                print("| ¬ ")
            if tries>6:
                print("|  ! ")
            if tries>1:
                print("| O ")
            if tries==2:
                print("| T")
            if tries ==3:
                print("|/T")
            if tries >3:
                print("|/T\ ")
            if tries ==5:
                print("|/ ")
            if tries ==6:
                print("|/  \ ")
            if tries ==7:
                print("  /  \ ")
        elif x in word:
            for i in range(0,len(word)):
                if word[i]==x:
                    l[i]=x
            for i in range(0,len(l)):
                if l[i]=='0':
                    print("__",end=" ")
                else:
                    print(" "+l[i]+" ",end=" ")
            print("\n")
        count=0    
        for i in range(0,len(l)):
            if l[i]==word[i]:
                count=count+1
        if count==len(word):
            print(" YOU HAVE WON THE GAME !!!!")
            break
        if left==0:
            print("YOU HAVE LOST THE GAME :(")
            print("The word was %s"%p)
            return
hangman()
guess(word)
while True:
    u=input("Play Again?(y,n):")
    if u=='n':
        print("Thanks A lot for Playing ;)")
        break
    elif u=='y':
        hangman()
        guess(word)
    else:
        print("Please print y for yes and n for no")
    
        

                    

