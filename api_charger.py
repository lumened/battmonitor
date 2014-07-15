import time

import apigpio.api_gpio as api_gpio

def init():
    api_gpio.init_pin(21)
    api_gpio.on_pin(21) # Set line to High

def deinit():
    api_gpio.deinit_pin(21)

def line_high():
    api_gpio.on_pin(21)
    

def line_low():
    api_gpio.off_pin(21)

def line_falling():
    line_low()
    time.sleep(0.10)
    line_high()    
    
    
