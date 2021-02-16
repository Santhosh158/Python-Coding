'''18(Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
current time in GMT. Revise the program so that it prompts the user to enter the
time zone in hours away from (offset to) GMT and displays the time in the specified
time zone. Here is a sample run:

Enter the time zone offset to GMT:
The current time is 4:50:34
'''

import time, math
CT = time.time()
CurrTime = int(CT)
print(CurrTime)
CurrSec = CurrTime % 60
TotalMin = CurrTime / 60
CurrMin = int(TotalMin % 60)
TotalHour = TotalMin / 60
CurrHour = int(TotalHour % 24)
Timezone = (eval(input("Enter the time zone offset to GMT:")))
CurrHour += Timezone
if (CurrHour < 0):
    CurrHour += 12

ActualTime =  ("{0}:{1}:{2}".format(CurrHour,CurrMin,CurrSec))

print("The current time is ",ActualTime)
