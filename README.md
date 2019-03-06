# pyvjoy

pyvjoy is a set of python binding for <a href='vjoystick.sourceforge.net'>vJoy</a>. This repo is based off <a href="https://github.com/tidzo/pyvjoy">tidzo</a>'s package.

### Requirements

Install vJoy from http://vjoystick.sourceforge.net/site/

### Installation

1. pip install git+https://github.com/maxofbritton/pyvjoy

### Usage





pyvjoy is a set of Python bindings for vJoy (vjoystick.sourceforge.net)

With this library you can easily set Axis and Button values on any vJoy device.  
Low-level bindings are provided in pyvjoy._sdk as well as a (hopefully) slightly more 'Pythonic' API in the pyvjoy.VJoyDevice() object.

Currently vJoyInterface.dll is looked for inside the pyvjoy directory only so place the desired version of that file there to use. (Note: this library currently only works with the x86 dll!)

USAGE
-----

import pyvjoy

#Pythonic API, item-at-a-time

j = pyvjoy.VJoyDevice(1)

#turn button number 15 on
j.set_button(15,1)

#Notice the args are (buttonID,state) whereas vJoy's native API is the other way around.


#turn button 15 off again
j.set_button(15,0)

#Set X axis to fully left
j.set_axis(pyvjoy.HID_USAGE_X, 0x1)

#Set X axis to fully right
j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)

#Also implemented:

j.reset()
j.reset_buttons()
j.reset_povs()


#The 'efficient' method as described in vJoy's docs - set multiple values at once

j.data
>>> <pyvjoy._sdk._JOYSTICK_POSITION_V2 at 0x....>


j.data.lButtons = 19 # buttons number 1,2 and 5 (1+2+16)
j.data.wAxisX = 0x2000 
j.data.wAxisY= 0x7500

#send data to vJoy device
j.update()


#Lower-level API just wraps the functions in the DLL as thinly as possible, with some attempt to raise exceptions instead of return codes.



