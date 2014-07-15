# This handles all interactions needed for interpreting and controlling the charger


import time
import api_adc
import apigpio.api_gpio as api_gpio


# Charger Control

def init_control():
    api_gpio.init_pin(21)
    api_gpio.on_pin(21) # Set line to High

def deinit_control():
    api_gpio.deinit_pin(21)

def line_high_control():
    api_gpio.on_pin(21)
    

def line_low_control():
    api_gpio.off_pin(21)

def line_falling_control():
    line_low()
    time.sleep(0.10)
    line_high()    
    

# Charger Status

