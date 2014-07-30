#!/usr/bin/python
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
    
    while volts > 5 : volts = adc.readADCSingleEnded(0, gain, sps) / 1000
    # To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
    # volts = adc.readADCSingleEnded(3, 1024, 860)

    return volts

def get_charger_led_value(gain=config.gain, sps=config.sps):
    global adc
    # Read channel 0 in single-ended mode using the settings above
    adc.startContinuousConversion(3,6144,2400)
    s=0
    count=1
    start_time = time.time()

    while time.time() <= start_time + 4.00:
        value = adc.getLastConversionResults()/1000
        if value<6:
            s+=value
        count+=1
            
    adc.stopContinuousConversion()
    if config.DEBUG: print("Readings:" + str(count))
    return (s/(count))
    
    # To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
    # volts = adc.readADCSingleEnded(3, 1024, 860)

    #print "%.6f" % (volts)

#Debugging Function for LED
def get_charger_led_value_data():
    global adc
    # Read channel 0 in single-ended mode using the settings above
    adc.startContinuousConversion(3,6144,2400)
    s=0
    #count=1
    start_time = time.time()

    while time.time() <= start_time + 10.00:
        value = adc.getLastConversionResults()/1000
        print(str(time.time()) + ',' + str(value))
        #if value<6:
        #    s+=value
        #    count+=1
            
    adc.stopContinuousConversion()
    #if config.DEBUG: print("Readings:" + str(count))
    sys.exit(0)
    #return (s/(count))
    
    # To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
    # volts = adc.readADCSingleEnded(3, 1024, 860)

    #print "%.6f" % (volts)



#init()
#get_charger_led_value()
