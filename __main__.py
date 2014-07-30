#!/usr/bin/python

# This is the main battery monitor daemon file

import time

import config, api_charger, api_adc

def attempt_switch(target, attempts=4):
    '''
    Function that attempts to switch charger state to target. 
    If #attempts are made and switch has not been succesful, then it returns False; 
    otherwise returns True.
    '''  
    count = 0
    while config.led_state != config.state[target] and count<attempts:
        api_charger.line_falling_control()
        time.sleep(config.lag)
        count += 1
        api_charger.update_state()
        
    if count==attempts: 
        if config.DEBUG: print("Attempt to switch to " + target + " state failed. Will try again on next wakeup.")
        return False #no state change
    return True
    


def handle_active_discharge():
    
    if config.led_state == config.state['detected']:
        if config.DEBUG: print("Start charging")
        if attempt_switch('charging'): config.system_state = config.charging
        return None
    
    if api_charger.check_bat_volt_low():
        if config.DEBUG: print("Shutdown")
        #Attempt Shutdown
        #Will be handled by Touch Flux
        #from subprocess import call
        #call(["sudo", "shutdown", "-h", "now"])
        config.system_state = config.active_discharge
        return None

def handle_passive_discharge():
    
    #Check if low voltage and power available Switch back to charging mode
    #Not needed
    
    if config.led_state == config.state['off']:
        config.system_state = config.active_discharge
        return None
        

def handle_charging():
    
    #if api_charger.check_bat_volt_high() or config.led_state == config.state['full']:
    if config.led_state == config.state['full']:
        if config.DEBUG: print("Stop charging")
        if attempt_switch('detected'): config.system_state = config.passive_discharge
        return None
        
    if config.led_state == config.state['detected']:
        if config.DEBUG: print("Restart charging")
        if attempt_switch('charging'): config.system_state = config.charging
        return None
    
    if config.led_state == config.state['off']:
        if config.DEBUG: print("Charger unplugged")
        config.system_state = config.active_discharge
        return None

def main():
    
    #Initialization
    api_adc.init()
    api_charger.init_control()
    config.system_state = config.active_discharge

    while 1:
        #Run Invariants
        #api_charger.update_state()
        api_charger.update_battery(True) #HAS TO RUN FIRST
        api_charger.update_state(True) #HAS TO RUN SECOND

        #config.bat_volt = config.bat_volt*3
        
        old_state = config.system_state
        
        if config.DEBUG: print("LED"); print(config.led_volt)
        if config.DEBUG: print("Bat"); print(config.bat_volt)
        if config.DEBUG: print("State"); print(config.system_state)

        #Run state handlers
        if config.system_state == config.active_discharge: handle_active_discharge()
        elif config.system_state == config.charging: handle_charging()
        elif config.system_state == config.passive_discharge: handle_passive_discharge()
        #State switching happens inside state handlers
        
        if old_state != config.system_state: continue
        
        time.sleep(config.delay)
        

#Run the main function
main()
