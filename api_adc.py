import time, signal, sys
from adafruitlibs.Adafruit_ADS1x15.Adafruit_ADS1x15 import ADS1x15
import config



def init():
    global adc
    # Initialise the ADC using the default mode (use default I2C address)
    # Set this to ADS1015 or ADS1115 depending on the ADC you are using!
    adc = ADS1x15(ic=config.ADS1015)

def get_value():
    global adc
    # Read channel 0 in single-ended mode using the settings above
    volts = adc.readADCSingleEnded(0, config.gain, config.sps) / 1000

    # To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
    # volts = adc.readADCSingleEnded(3, 1024, 860)

    print "%.6f" % (volts)



init()
get_value()