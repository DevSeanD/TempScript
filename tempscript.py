import time
import sys
from colorama import Fore, Style

"""
TODO: Fix the display of core temps with no digit in the hundreds place
"""


def colorTemp(coreTemp):
    sys.stdout.flush()
    displayString = ""
    if len(str(coreTemp)) == 4:
        coreTemp += 0
    if coreTemp <= 59:
        displayString = f'CPU: {Fore.GREEN}' + str(coreTemp)
    if coreTemp >= 60 and coreTemp <= 79:
        displayString = f'CPU: {Fore.YELLOW}' + str(coreTemp)
    if coreTemp >= 80:
        displayString = f'CPU: {Fore.RED}' + str(coreTemp)

    displayString = displayString[0:15:1]
    displayString += u'\N{DEGREE SIGN}' + 'C'
    print(displayString,end='\r')

def main():
    # Scan for core quantity
    coreTempList = [] # Stores core temperature values

    for x in range(0,127): # Supports up to 128 cores
        try: 
            with open("/sys/class/thermal/thermal_zone{}/temp".format(x)) as file:
                coreTempList.append(float(file.read()))
        except: 
            pass
    
    coreAvgTemp = 0 # Store the result after average calculation
    numOfCores = len(coreTempList)

    for temp in coreTempList:
        coreAvgTemp += float(temp)
    
    coreAvgTemp = coreAvgTemp / numOfCores
    colorTemp(coreAvgTemp / 1000)

    time.sleep(1) 

if __name__ == "__main__":
    main()
