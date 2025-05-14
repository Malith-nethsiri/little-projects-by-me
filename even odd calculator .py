# even or odd checker

num = int(input("entre your number [press 0 to end the program] = "))

while  not num == 0 :
        print(f"{num} is an even number") if num % 2 == 0 else print(f"{num} is an odd number")
        num = int(input("entre your number [press 0 to end the program] = "))

print("BYE")