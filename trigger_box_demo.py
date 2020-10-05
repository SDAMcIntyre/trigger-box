from triggerbox import *
from psychopy import core

# connect to the trigger box via serial port
trigger = TriggerBox()

# send a 5V signal over analog channel 3 until it is switched off
goInfinite = trigger.make_analog_signal(channel = 3, voltage = 5, duration = 0)
trigger.ser.write(goInfinite) 

# wait 5 seconds
core.wait(5) 

# cancel the previously sent analog signal
# cancel = trigger.make_cancel_signal(channel = 3) # doesn't work
# trigger.ser.write(cancel) 
stop = trigger.make_analog_signal(3,0,0) # this works 
trigger.ser.write(stop) 

# send a 5V signal over analog channel 3 for 100 ms
go = trigger.make_analog_signal(channel = 3, voltage = 5, duration = 100)
# send the signal
trigger.ser.write(go) 

# send a message over the USB channel and read it back
label = trigger.make_digital_signal(channel = 1, message = 'T', duration = 0)
trigger.ser.write(label) 
trigger.ser.readline().decode('utf-8')

# set up another serial port to read the output from channel 2 
output = serial.Serial('COM8', 1200, timeout = 0.5)

# send message over channel 2 and then read it
message = trigger.make_digital_signal(channel = 2, message = 'T', duration = 0)
trigger.ser.write(message) 
output.readline().decode('utf-8') # DOESN'T WORK, GET NO SIGNAL OR 0 BYTE

# close the serial connections
trigger.ser.close()
output.close()
