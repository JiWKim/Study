def getSpamLines(filename):
      f=open(filename,'r')
      spam_no=0
      for line in f:
            data=line.split(':')
            if data[0]=='SPAM-Confidence':
                  if float(data[1])>0.8:
                        spam_no=spam_no+1
      return spam_no

print(getSpamLines("spam.txt"))
