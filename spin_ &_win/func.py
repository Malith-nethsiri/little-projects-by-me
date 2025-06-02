# functions

import random


items = ["🎁", "🎉", "🌹", "🏆", "🧿", "🎲"]

balance = 0

# b_a means betting amount, e_f means entry fees, a_f means additional fees

def entry_fee_cal(e_f):
    global balance
    balance += e_f

def additional_fee_cal(a_f):
    global balance
    balance += a_f
    return

def remaining_balance_after_bet(b_a):
    global balance
    balance -= b_a
    return


def spinning(b_a):
    global balance
    new_items = [random.choice(items) for _ in range(3)]
    for x in new_items:
        print(f" | {x}", end=" | ")
    print()

    if all(y == new_items[0] for y in new_items):
        multiplier = {"🎁": 2, "🎉":3, "🌹":4, "🏆":5, "🧿":6, "🎲":10}.get(new_items[0], 0)
        balance += (b_a * multiplier)
        print("--- YOU WON ---\n")
        print(f"New total is {balance}")

    else :
        print("\n--- YOU LOST ---\n")