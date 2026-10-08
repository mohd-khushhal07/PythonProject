# for variable in range(start , stop , step)
        #code to repeat

#for i in range(5,0 , -1):
   #print(i)

#while condition:
    #code to repeat

# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# import time

# for i in range (5, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Happy New Year!")

#count down Timer

import time
#step1: Get user input for the countdown start

start = int(input("Enter the number to start the countdwon from: "))

#step 2: Countdown using a while loop 
print("\n -- Countdown Begins --")
while start > 0:
    print(start)
    time.sleep(1)
    start -= 1

#step3: Print final message

print("Countdown Complete")