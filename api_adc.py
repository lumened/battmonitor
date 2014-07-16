# This handles ALL ADC manipulations. 
# WARNING: Do not initialise or use ADC anywhere else. 

import time, signal, sys
from adafruitlibs.Adafruit_ADS1x15.Adafruit_ADS1x15 import ADS1x15
import config



def init():
    global adc
    # Initialise the ADC using the default mode (use default I2C address)
    # Set this to ADS1015 or ADS1115 depending on the ADC you are using!
    adc = ADS1x15(ic=config.ADS1015)

def get_battery_value(gain=config.gain, sps=config.sps):
    global adc
    # Read channel 0 in single-ended mode using the settings above
    volts = adc.readADCSingleEnded(0, gain, sps) / 1000

    # To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
    # volts = adc.readADCSingleEnded(3, 1024, 860)

    return volts

def get_charger_value(gain=config.gain, sps=config.sps):
    global adc
    # Read channel 0 in single-ended mode using the settings above
    s=0
    for i in range(1,1000):
        s += adc.readADCSingleEnded(1, gain, sps)
    
    return (s/(1000*1000))
    
    # To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
    # volts = adc.readADCSingleEnded(3, 1024, 860)

    #print "%.6f" % (volts)


#init()
#print(get_charger_value(sps=3300))
