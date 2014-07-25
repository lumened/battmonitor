# This handles all interactions needed for interpreting and controlling the charger


import time
import api_adc, config
import apigpio.api_gpio as api_gpio


# Charger Control

def init_control():
    api_gpio.init_pin(27)
    api_gpio.off_pin(27) # Set line to low

def deinit_control():
    api_gpio.deinit_pin(27)

def line_high_control():
    api_gpio.on_pin(27)
    

def line_low_control():
    api_gpio.off_pin(27)

def line_falling_control():
    line_high_control()
    time.sleep(0.10)
    line_low_control()    
    

# Charger Status

def update_state(write_to_file=False):
    '''
    This function inputs the LED state from the charger and interprets the result
    '''
    
    config.led_volt = api_adc.get_charger_value(sps=3300)

    if config.led_volt<0.5: config.led_state = config.state['off']
    elif config.led_volt>1.0 and config.led_volt<1.5: config.led_state = config.state['detected']
    elif config.led_volt>2.3 and config.led_volt<2.6: config.led_state = config.state['charging']
    elif config.led_volt>4.8: config.led_state = config.state['full']

    if write_to_file:
        f = open('/home/pi/touch-flux/src/battmonitor/data.txt', "a")
        if config.led_state==config.state['off']: f.write('U')
        else: f.write('P')
        f.close()
        
    return None
    

# Battery State

def update_battery(write_to_file=False):
    '''
    This function inputs the battery voltage and updates the shared file
    '''

    config.bat_volt = api_adc.get_battery_value()*3
    
    bat_percent = 100*(config.bat_volt - config.bat_min)/(config.bat_max - config.bat_min)
    
    if bat_percent<0 : bat_percent = 0
    elif bat_percent>100 : bat_percent = 101

    if write_to_file:
        f = open('/home/pi/touch-flux/src/battmonitor/data.txt', "w")
        f.write("%.3d" % bat_percent)
        if config.DEBUG: print("%.3d" % bat_percent)
        f.close()

    return None
    
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
 
