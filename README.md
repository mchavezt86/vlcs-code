# VLCS (CS4425) Python code
This repository contains the Python code for the VLCS course at TU Delft (CS4425).

There are two files in this repository:

### vlcs_mobile.py

Contains the main code to be used for transferring video files recorded with *OpenCamera* to the computer. To execute it, you need to install the package `adb-shell` and its usb option as well. The following commands installs the required packages:
* `pip install adb-shell`
* `pip install adb-shell[usb]`

Your mobile phone is required to have the *developer options* enabled as well as the *usb debugging.*

**To use the module** download the file and copy it to the same location as your working Python directory.
Use `from vlcs_mobile import copyVideo`, and then you can just call the `copyVideo()` function, which copies the last recorded video to the same location.
