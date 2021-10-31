# TempScript
TempScript is an easy to use, easy to install, and lightweight, temperature monitoring script for Linux Machines

Installation:

	1.Run the command "git clone https://github.com/DevSeanD/TempScript.git"
	2.Run the command "chmod +x tempscript"
	3.Run the command "chmod +x install.sh"
	4.Run "sudo tempscript" to test if installation was successful
	5. After the initial "sudo tempscript" command you will be able to simply run it using the "tempscript" command


Before creating an implementation of the script an understanding of the way Linux store and measures CPU temperatures is needed. 

Linux stores the CPU's thermal information in "/sys/devices/platform/coretemp.0/hwmon/hwmon5/tempX_input". This file reports the temperature in celsius and multiplied by 1000:

	Ex. "cat /sys/devices/platform/coretemp.0/hwmon/hwmon5/temp2_input" => "46000" => 46 celsius

After obtaining the values of each core it will be time to sort them based on these celsius temperature ranges:

	Low: 0 - 59
	Moderate: 60 - 79
	High: 80+

Depending on the range the core temperature falls into the color will vary. Low => Green, Moderate => Yellow, High => Red.

This program relies on the python library colorama to add color to the terminal. 

It can be manually installed with the command:

	"pip install colorama"

Or Via the install script

TempScript is also a very light weight program! Here is a example of a resource use:

	*This htop readout was captured on a 2011 Lenovo Thinkpad X220T with an i5 dual core CPU and 8gb of RAM*
	
![htop-resource-use](https://user-images.githubusercontent.com/39039620/138452006-9b3ad16a-5103-4e6d-9812-e52759dfe3f5.png)

