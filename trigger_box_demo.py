from triggerbox import *
from psychopy import core

# connect to the trigger box via serial port
trigger = TriggerBox()

# send a 5V signal over analog channel 3 until it is switched off
trigger.send_analog(channel = 3, voltage = 5, duration = 0)

# wait 5 seconds
core.wait(5) 

# cancel the previously sent analog signal
# trigger.send_cancel(channel = 3) # doesn't work
trigger.send_analog(3,0,0) # this works 

# send a message over the USB channel and read it back
trigger.send_digital(channel = 1, message = 'T', duration = 0)
trigger.ser.readline().decode('utf-8')

# set up another serial port to read the output from channel 2 
output = serial.Serial('COM8', 1200, timeout = 0.5)

# send message over channel 2 and then read it
trigger.send_digital(channel = 2, message = 'T', duration = 0)
output.readline().decode('utf-8') # DOESN'T WORK, GET NO SIGNAL OR 0 BYTE

# close the serial connections
trigger.ser.close()
output.close()
