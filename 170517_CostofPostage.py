#p.193
##q49 Cost of Postage

#The original postage cost of airmail letters was 5 cents for the first ounce and 10 cents for each additional ounce.

def ceil():
      num=float(input("Enter the number of ounces: "))
      int_num=int(num)

      if int_num!=num:
            int_num=int_num+1
            
      return int_num

def cost():
      weight=ceil()
      
      if weight<=1:
            post_cost=0.05
      elif weight>1:
            post_cost=0.05+(0.1*(weight-1))
      return post_cost


print("Cost: $", cost())
