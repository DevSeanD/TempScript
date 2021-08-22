# TempScript
TempScript is an easy to use, easy to install, and a modular, temperature monitoring script

Installation:

	1.Run the command "git clone https://github.com/DevSeanD/TempScript.git"
	2.Run the install script with "sudo ./install.sh"
	3.Run "tempscript" to test if installation was successful


Before creating an implementation of the script an understanding of the way Linux store and measures CPU temperatures is needed. 

Linux stores the CPU's thermal information in "/sys/devices/platform/coretemp.0/hwmon/hwmon5/tempX_input". This file reports the temperature in celsius and multiplied by 1000:

	Ex. "cat /sys/class/thermal/thermal_zone0/temp" => "46000" => 46 celsius

After obtaining the values of each core it will be time to sort them based on these celsius temperature ranges:

	Low: 0 - 59
	Moderate: 60 - 79
	High: 80+

Depending on the range the core temperature falls into the color will vary. Low => Green, Moderate => Yellow, High => Red.

This program relies on the python library colorama to add color to the terminal. 

It can be manually installed with the command:

	"pip install colorama"

Or Via the install script
