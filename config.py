# Constants

#Developer
DEBUG = False

#ADC
ADS1015 = 0x00 # Address of the ADC
gain = 6144 # Max/Min Range of Readings
sps = 250 #Samples per second

#ADC Channels: 0-3
channel_battery = 0
channel_charger = 1

#Charger States
state = {'off':0, 'detected':1, 'charging':2, 'full':3}

#Sleep Time
delay = 10 #Seconds

#Lag between switching and output
lag = 2 #Seconds

#System States
active_discharge = 0x00 #Charges if power is connected
charging = 0x01 #Charging till full voltage or disconnected
passive_discharge = 0x02 #Does not charge even if power is connected

#Battery Range
bat_min = 10.0
bat_max = 12.60

# Variables
bat_volt = 0
led_volt = 0
led_state = 0

#Initial bootup state is active discharge.
system_state = active_discharge


