battmonitor
===========

This is a battery monitoring utility for the Raspberry Pi. It interfaces with ADS1015 which is an analog to digital converter. The ADS1015 provides two inputs, one from the battery, and another from the charging circuit. Thus, the utility is able to monitor the battery value, detect when supply is connected, and initiate and stop charging as per requirements of the battery.

It updates the status into data.txt at frequent intervals, which can then be read by a GUI application to display to the user.

This utility should be run as a daemon. There is an Upstart job file that can be used for that purpose.
