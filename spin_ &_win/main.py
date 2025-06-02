# main file

running = True

from func import spinning, entry_fee_cal, remaining_balance_after_bet, additional_fee_cal

print("--- SPIN & WIN ---\n")

while running:
    entry_fee = float(input("enter the entry fee-- "))

    if entry_fee < 100:
        print("You need at least $100 to enter \n")


    elif entry_fee >= 100 :
        entry_fee_cal(entry_fee)
        print("\n---  LET'S PLAY  ---")

        while running :
            from func import balance

            if balance == 0:
                print(f"You balance is ${balance}\n")

                additional_amount = float(input("Enter the amount of money if you wanna play again or \n"
                                                "press '0' to quit\n"))

                if additional_amount == "0" :
                    print("--- BYE I HOPE YOU ENJOY --- ")
                    running =False

                else :
                    additional_fee_cal(additional_amount)

            from func import balance
            betting_amount = float(input(f"How much you like to bet from ${balance} \n"
                                         "If you want to quit press '0' -- "))
            print()

            if betting_amount == 0 :
                print("--- BYE I HOPE YOU ENJOY --- ")
                running = False


            elif betting_amount < 0:
                print("enter a valid amount to bet!! \n ")


            elif betting_amount > balance:
                print("enter a valid amount to bet!! \n")

            else:
                remaining_balance_after_bet(betting_amount)
                from func import balance
                print(f"you bet ${betting_amount}")
                print(f"balance is ${balance}\n")

                spinning(betting_amount)

        running = False
