# rock paper scissors game

import random

options = ("rock", "paper" ,"scissors")
playing = True
win_count = 0
lost_count = 0
tie = 0

while playing:
    computer = random.choice(options)
    player = input("rock,paper or scissors (press '0' to quit ): ")
    print(f"\nyou :      {player}")
    print(f"computer : {computer}")
    print()

    if player == "0":
        print(f"you won  : {win_count} \nyou lost : {lost_count} \ntie      : {tie}")
        print("-- GOOD BYE --")
        playing = False

    elif player not in options :
        print("just say rock,paper or scissors!!!\n")
        continue

    elif player == computer:
        tie +=1
        print("its a tie")
    elif player == "rock" and computer=="scissors":
        win_count += 1
        print("you win")
    elif player == "paper" and computer=="rock":
        win_count += 1
        print("you win")
    elif player == "scissors" and computer=="paper":
        win_count += 1
        print("you win")
    else:
        lost_count += 1
        print("you lost, try again")
    print()
