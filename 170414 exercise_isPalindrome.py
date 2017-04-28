def isPalindrome(word):
    for i in range(round(len(word)/2)):
        if word[i]!=word[-(i+1)]:
            return False        
    return True


print(isPalindrome("madam"))
print(isPalindrome("icecream"))

