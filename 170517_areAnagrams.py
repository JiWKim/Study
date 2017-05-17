#p.194
##q51 Anagrams

def areAnagrams(string1, string2):

      string1=string1.upper()
      string2=string2.upper()

      string1_letters=list()
      for strings in string1:
            string1_letters.append(strings)

      string2_letters=list()
      for strings in string2:
            string2_letters.append(strings)

      if string1_letters.count(" ")!=0:
            string1_letters.remove(" ")
      if string1_letters.count(",")!=0:
            string1_letters.remove(",")

      if string2_letters.count(" ")!=0:
            string2_letters.remove(" ")
      if string2_letters.count(",")!=0:
            string2_letters.remove(",")

      for letter in string1_letters:
            if string1_letters.count(letter)!=string2_letters.count(letter):
                  return False
      return True

a=input("Enter the first word or phrase: ")
b=input("Enter the second word or phrase: ")

if areAnagrams(a,b):
      print("Are anagrams")
else:
      print("Are not anagrams")
