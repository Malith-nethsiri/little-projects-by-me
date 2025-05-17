# little-projects-by-me

# the even or odd calculator
num = int(input("entre your number [press 0 to end the program] = "))

while  not num == 0 :
        print(f"{num} is an even number") if num % 2 == 0 else print(f"{num} is an odd number")
        num = int(input("entre your number [press 0 to end the program] = "))

print("BYE")


  # exapmples for even odd calculator
    >  
entre your number [press 0 to end the program] = 55
55 is an odd number
entre your number [press 0 to end the program] = 99
99 is an odd number
entre your number [press 0 to end the program] = 663
663 is an odd number
entre your number [press 0 to end the program] = 458
458 is an even number
entre your number [press 0 to end the program] = 1209
1209 is an odd number
entre your number [press 0 to end the program] = 0
BYE




# coumpound intererest calculator

# compound interest calculator

while True :
        principal = float(input("what is the principle amount-- "))
        if principal < 0 :
                print("your principle value can't be less than zero")
        else:
                break

while True :
        rate = float(input("what is the annual interest rate-- "))
        if  rate < 0 :
                print("your interest rate can't be a negative value")
        else:
                break

while True :
        time = float(input("For how many years -- "))
        if time < 1  :
                print("it must atleast a year to make a interest ")
        else:
                break

total = principal * pow((1 + rate / 100),time)
print(f"your total amount of money in {time} years is {total:.3f}")

   # examples from compound interest calculator

what is the principle amount-- -5632
your PRINCIPAL VALUE CAN'T BE less than zero
what is the principle amount-- 5569
what is the annual interest rate-- 0.25
For how many years -- 5
your total amount of money in 5.0 years is 5638.961



#  the timer

we can set timer for days hours minutes and seconds 
there is a issue in it the input should be in seconds when we needs to set timer for hours we don't know how meny seconds that to put it in
we can but we needs to calculate it its a negative point in this



        
