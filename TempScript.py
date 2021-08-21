import time
import sys
from colorama import Fore, Style

def colorTemp(coreTemp):
    if coreTemp <= 59:
        print(f'{Fore.GREEN}' + str(coreTemp),end='\r')
    if coreTemp >= 60 and coreTemp <= 79:
        print(f'{Fore.YELLOW}' + str(coreTemp),end='\r')
    if coreTemp >= 80:
        print(f'{Fore.RED}' + str(coreTemp),end='\r')

def main():
    while(True):
        core0 = open("/sys/devices/platform/coretemp.0/hwmon/hwmon5/temp2_input")
        core1 = open("/sys/devices/platform/coretemp.0/hwmon/hwmon5/temp3_input")
        core0Temp = int(core0.read())
        core1Temp = int(core1.read())

        coreAvgTemp = (core0Temp + core1Temp) / 2
        colorTemp(coreAvgTemp / 1000)

        sys.stdout.flush()
        time.sleep(3)
    
if __name__ == "__main__":
    main()
