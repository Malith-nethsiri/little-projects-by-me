# a guessing game

import random

print("***  geuss the number correctly you only gets 5 chances  ***")
print(" hint -- the number is in between 1 and 100")

secret_number = random.randint(1,100)
guessed_number = None
attemps = 0


while guessed_number != secret_number :
    guessed_number = int(input("give me a guess -- "))
    attemps += 1

    if attemps == 5 :
        print(f"""your attemps are over try againg next time
the correct answer is {secret_number}""")

    elif guessed_number > secret_number :
        print("it's lower than you thinck")

    elif guessed_number < secret_number :
        print("it's higher than you thinck")

    else  :
        print(f"you guessed it correctly in {attemps} attemps")
