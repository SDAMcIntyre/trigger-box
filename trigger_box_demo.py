from triggerbox import *
from psychopy import core

BAUDRATE_ANOTHER = 115200
# BAUDRATE = 1200

# connect to the trigger box via serial port
trigger = TriggerBox()

# send a 5V signal over analog channel 3 until it is switched off
goInfinite = trigger.make_analog_signal(channel = 3, voltage = 5, duration = 0)
trigger.ser.write(goInfinite) 

# wait 5 seconds
core.wait(5) 

# cancel the previously sent analog signal
cancel = trigger.make_cancel_signal(channel = 3) # does work now
trigger.ser.write(cancel) 
# stop = trigger.make_analog_signal(3,0,0) # this works 
# trigger.ser.write(stop) 

# wait 5 seconds
core.wait(5) 
# send a 5V signal over analog channel 3 for 100 ms
go = trigger.make_analog_signal(channel = 3, voltage = 5, duration = 100)
# send the signal
trigger.ser.write(go) 

# wait 5 seconds
core.wait(5) 
# send a message over the USB channel and read it back
label = trigger.make_digital_signal(channel = 1, message = 'T', duration = 0)
trigger.ser.write(label) 
trigger.ser.readline().decode('utf-8')

# # send signal to winSC
# winSC_msg = trigger.make_winsc_signal()
# trigger.ser.write(winSC_msg)


# # wait 5 seconds
# core.wait(5) 
# # set up another serial port to read the output from channel 2 
# output = serial.Serial('COM10', BAUDRATE_ANOTHER, timeout = 0.5)

# # send message over channel 2 and then read it in output chaqnnel
# message = trigger.make_digital_signal(channel = 2, message = 'j', duration = 1000)  # WORKS SOMETIMES ?!
# trigger.ser.write(message) 
# x = 0
# while x < 5:
#     print("COM9 says:",output.readline().decode('utf-8'))
#     x+=1

# # output.readline().decode('utf-8') # DOESN'T WORK, GET NO SIGNAL OR 0 BYTE


###########################################
# CLEAN UP
try:
    # close the serial connections
    trigger.ser.close()
except:
    print("Did not close trigger")
# try:
#     output.close()
# except:
#     print("Did not close DSUB")
