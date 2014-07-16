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

def update_state:
    '''
    This function inputs the LED state from the charger and interprets the result
    '''
    
    config.led_volt = api_adc.get_charger_value(sps=3300)

    if led_volt<0.5: return config.state['off']
    elif led_volt>1.0 and led_volt<1.5: return config.state['detected']
    elif led_volt>2.3 and led_volt<2.6: return config.state['charging']
    #elif led_volt>1.0 and led_volt<1.5: return config.state['full']
    
    
    
# Battery State

def update_battery():
    '''
    This function inputs the battery voltage and updates the shared file
    '''

    config.bat_volt = api_adc.get_battery_value()
    
    bat_percent = 100*(bat_volt - config.bat_min)/(config.bat_max - config.bat_min)
    
    f = open('/home/pi/touch-flux/src/battmonitor/data.txt', "w")
    f.write(bat_percent)
    f.close()

    
def check_bat_volt_high():
    '''
    Returns a boolean that identifies whether the battery has reached the threshold
    '''
    if config.bat_volt > config.bat_max: return True
    return False
        

def check_bat_volt_low():
    '''
    Returns a boolean that identifies whether the battery has reached the threshold
    '''
    if config.bat_volt < config.bat_min: return True
    return False
 
