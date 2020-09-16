import serial
from triggerbox import *
from psychopy import core

# check in "device manager"/"enhetshanteraren" which com port the trigger box is
# for future implementation of auto detect: 
# https://stackoverflow.com/questions/53214304/python-pyserial-auto-detect-com-ports
trigger = TriggerBox('COM6')

# send a 'T' over digital channel 2 for 10 msec
trigger.send_digital(channel = 2, message = 'T', duration = 10)

# send a 5V signal over analog channel 3 until it is switched off
trigger.send_analog(channel = 3, voltage = 5, duration = 0)

# wait 5 seconds
core.wait(5) 

# cancel the previously sent analog signal
trigger.send_cancel(channel = 3)