# banking project
from bank_core import depositing
from bank_core import withdrawing
from bank_core import final_balance
from bank_core import withdraw_history
from bank_core import depositing_history

is_running = True

while is_running :
    print( "1. Check Balance\n"
           "2. Deposite Money\n"
           "3. Withdraw Money\n"
           "4. Bancking History\n"
           "5. Exit\n"
           "------------------ ")
    choice = int(input("Choose from above --  "))

    if choice == 1:
        final_balance()

    elif choice == 2:
        deposit_value = float(input("Enter the amount-- "))
        depositing(deposit_value)

    elif choice == 3:
        withdraw_value = float(input("Enter the amount-- "))
        withdrawing(withdraw_value)

    elif choice == 4:
        print("--- DEPOSIT HISTORY ---")
        for w,z in depositing_history.items():
            print(f"{z:20} .......{w}")

        print("--- WITHDRAW HISTORY ---")
        for x, y in withdraw_history.items():
            print(f"{y:20} .......{x}")


    elif choice == 5:
        break
    else:
        print("choose correctly")








