import serial

port = 'COM6' # check in "device manager"/"enhetshanteraren" which com port the trigger box is
baudrate = 1200 # according to trigger box documentation

triggerBox = serial.Serial(port, baudrate, timeout = 0.5) # set up the triger box object

# construct a command according to trigger box documentation
# example, send an ongoing 5 Volt signal on analog output number 3
commandNumber = 2
analogOutput = 3
outputLevel = 50
time1 = 0
time2 = 0
command = bytearray(['S',commandNumber, analogOutput, outputLevel, time1, time2])

# send the command to the triger box
triggerBox.write(command)