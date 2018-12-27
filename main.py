#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import subprocess

def LEDon():
    """on led"""
    led_cmd = "echo 1 > /dev/myled0"
    subprocess.call(led_cmd, shell=True)

def LEDoff():
    """off led"""
    led_cmd = "echo 0 > /dev/myled0"
    subprocess.call(led_cmd, shell=True)

def wait(self):
    """wiat time"""
    time.sleep(self)

def SATO():
    """SATO"""
    #S
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)
    
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)
    
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.5)
    
    #A
    LEDon()
    wait(0.1)
    LEDoff()
    wait(0.1)
    
    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.5)
    

    #T
    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.5)
    
    #O
    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.1)

    LEDon()
    wait(0.5)
    LEDoff()
    wait(0.5)
def main():

	SATO()
		
if __name__ == "__main__":
	main()
