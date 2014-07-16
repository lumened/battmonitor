# Constants

ADS1015 = 0x00 # Address of the ADC
gain = 6144 # Max/Min Range of Readings
sps = 250 #Samples per second

#ADC Channels: 0-3
channel_battery = 0
channel_charger = 1

#Charger States
state = {'off':0, 'detected':1, 'charging':2, 'full':3}

#System States
active_discharge = 0x00 #Charges if power is connected
charging = 0x01 #Charging till full voltage or disconnected
passive_discharge = 0x02 #Does not charge even if power is connected

#Battery Range
bat_min = 11.0 #TBC
bat_max = 12.6 #TBC

# Variables
bat_volt = 0
led_volt = 0

#Initial bootup state is active discharge.
system_state = active_discharge


