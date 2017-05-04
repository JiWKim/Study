#p.198
##Wilson's Theorem

my_num=int(input("Enter an integer greater than 1: "))

def factorial(number):
      result=1
      for i in range(1,number+1):
            result=result*i
      return result


def isPrime(number):
      fact_result=factorial(number-1)
      if (fact_result+1)%number==0:
            print(number, " is a prime number.")
            return True
      else:
            print(number, " is not a prime number.")
            return False

isPrime(my_num)
