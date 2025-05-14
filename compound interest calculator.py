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
