# use this to try to read an incoming digital signal from the trigger box
#adapted from https://jc-bell.com/blog/2011/01/serial-port-monitor-20-loc/

import serial

ser = serial.Serial('COM4', baudrate=1200, timeout=0.2) # opens, too.
print("Monitoring serial port " + ser.name)
data = []
while True:
	ch = ser.read(1)
	if len(ch) == 0:
		# rec'd nothing print all
		if len(data) > 0:
			s = ''
			for x in data:
				s += ' %02X' % ord(x)
			print('%s [len = %d]' % (s, len(data)))
		data = []
	else:
		data.append(ch)