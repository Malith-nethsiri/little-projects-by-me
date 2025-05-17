# the timer


import time
print("***   THE TIMER   ***")

the_time = int(input("give the time in seconds-- "))

for x in reversed(range(1,the_time+1)) :
    seconds = x % 60
    minutes = (x // 60)%60
    hours = (x //3600)%24
    days = (x//216000)%7
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("***  TIMES UP  ***")