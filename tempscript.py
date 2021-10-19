import time
import sys
from colorama import Fore, Style

def colorTemp(coreTemp):
    sys.stdout.flush()
    displayString = ""

    if coreTemp <= 59:
        displayString = f'CPU: {Fore.GREEN}' + str(coreTemp)
    if coreTemp >= 60 and coreTemp <= 79:
        displayString = f'CPU: {Fore.YELLOW}' + str(coreTemp)
    if coreTemp >= 80:
        displayString = f'CPU: {Fore.RED}' + str(coreTemp) 

    displayString += u'\N{DEGREE SIGN}' + 'C'
    print(displayString,end='\r')

def main():
    core0 = open("/sys/devices/platform/coretemp.0/hwmon/hwmon5/temp2_input")
    core1 = open("/sys/devices/platform/coretemp.0/hwmon/hwmon5/temp3_input")
    core0Temp = int(core0.read())
    core1Temp = int(core1.read())

    coreAvgTemp = (core0Temp + core1Temp) / 2
    colorTemp(coreAvgTemp / 1000)
    time.sleep(1)
    
if __name__ == "__main__":
    main()
