import time

balance = 0
depositing_history = {}
withdraw_history = {}

def final_balance():
    print(f"Your Balance is -- {balance:.2f}")

def depositing(d_v):                 #d_v is for deposit value
    global balance,depositing_history
    now = time.localtime()  # get local time object
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", now)

    balance += d_v
    print(f"You deposit of {d_v:.2f} is successfully completed ")
    print(f"New balance of your account is {balance:.2f}")

    #adiing to the dict
    depositing_history[formatted] = d_v

def withdrawing(w_v):                 #w_v is for withdraw value
    global balance,withdraw_history
    now = time.localtime()  # get local time object
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", now)

    balance -= w_v
    print(f"You withdraw of {w_v:.2f} is successfully completed ")
    print(f"New balance of your account is {balance:.2f}")

    # adding to the dict
    withdraw_history[formatted] = w_v
