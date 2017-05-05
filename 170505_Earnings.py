#p.197 q69
#Earnings

def main():
      x=my_input()
      y=weekly_pay(x[0], x[1])
      output(y)

def my_input():
      hours=int(input("Enter hours worked: "))
      hourly_pay=int(input("Enter hourly pay: "))
      return (hours, hourly_pay)

def weekly_pay(hours, hourly_pay):
      if hours<=40:
            weekly_pay = hourly_pay * hours
      else:
            weekly_pay = (40*hourly_pay) + ((hours-40)*(hourly_pay*1.5))

      return weekly_pay

def output(weekly_pay):
      print("week\'s pay: $", weekly_pay)

main()
