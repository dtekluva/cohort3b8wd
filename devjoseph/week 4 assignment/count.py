import time
from winsound import Beep
fg = int(input("Please enter time: "))
while fg:
    fgt = 60
    fg -= 1
    time.sleep(1)

    while fgt:
        fgt -= 1
        print(f"{fg}:{fgt} \r", end="")
        time.sleep(1)
        Beep(1000, 200)

print("End")
        
