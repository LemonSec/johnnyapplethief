# johnnyapplethief
Proof of concept code for creating a malicious iphone charging station. 

The following code is proof of concept code for creating a malicious iphone charger that copies pictures from the victims phone. This isn't a one touch exploit and requires user interaction in order to grant the necessary permissions. Some clever social engineering can help with this, see the attached images. The code has been purposely incomplete as to not make a complete plug and play malicious device. The proof of concept copies a single folder but can be modified to copy all folders.


## Dependencies

Run the following command to install necessary packages:
sudo apt-get install libimobiledevice6 libimobiledevice-utils ifuse

## Manual exploitation

Execute the malicious script
Python3 charge.py

Execute the connect script
./connect.sh

This will mount the device and trigger the copy process.

After the data has been copied run the cleanup script
./clean.sh

## Automated exploitation

This section left intentionally vague.

UDEV rules can be leveraged to run the connect and cleanup scripts, An example rule would look something like this.
ACTION=="add", SUBSYSTEM=="net", NAME=="ipheth 1-1.1.2:4.2", RUN+="/home/pi/Desktop/connect.sh"

With UDEV rules in place you'll only need to run the charge.py script.
