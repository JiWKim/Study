#170428 Hangman


## 1. Random selection of a word
import random
words=['strawberry', 'banana', 'watermelon', 'grapes', 'orange'] 
x=random.randint(0,4)

word=words[x] 
_word=list("_"*len(word))
listWrong=list()
numWrong=len(listWrong)
print("Answer = ", "  ".join(_word))


## 2-0. Get input
def chGet():
      ch=input("Enter a single character: ")
      if  len(ch)!=1:
            while len(ch)!=1:
                  print("Invalid input")
                  ch=input("Enter a single character: ")
      ch=ch.lower()
      return ch


## 2-1. When the Character if Correct
def chCorrect(ch):      
      for i in range(len(word)):
                     if word[i]==ch :
                           _word[i]=ch
      print("Answer = ", "  ".join(_word))
      

## 2-2. When the Character is Wrong
def chWrong(ch):
      listWrong.append(ch)
      numWrong=len(listWrong)
      print("Wrong = ", "  ".join(listWrong))
      print("Answer =", "  ".join(_word))


## 2. Operate

while (numWrong<10) & (_word.count("_")!=0):

      ch=chGet()
      
      if (ch in _word) or (ch in listWrong):
            print("You already entered this character")
            print("Answer =", "  ".join(_word))

      elif (ch in word) & (ch not in _word):
            chCorrect(ch)
            
      elif (ch not in word) & (ch not in listWrong):
            chWrong(ch)
            
      numWrong=len(listWrong)
      print("Numer of chance left: ", 10-numWrong)
      print()




