import serial
import os
import sys
import time
import serial
import serial.tools.list_ports
# working with bytes https://www.devdungeon.com/content/working-binary-data-python 
# https://stackoverflow.com/questions/53214304/python-pyserial-auto-detect-com-ports

class TriggerBox():
    def __init__(self):      
        self.startCharacter = 'S'.encode('utf-8')
        print('Connecting to trigger box...')
        connected = False
        ports = serial.tools.list_ports.comports(include_links=False)
        for port in ports :
            print('Checking port '+ port.device)
            ser = serial.Serial(port.device)
            if ser.isOpen():
                ser.close()
            self.ser = serial.Serial(port.device, 1200, timeout=0.5)
            self.ser.flushInput()
            self.ser.flushOutput()
            self.send_digital(channel = 1, message = 'T', duration = 0)
            testmessage = self.ser.readline().decode('utf-8')
            if testmessage == 'T':
                connected = True
                print('Connected to ' + ser.name)
                break
        if not connected: print('Could not find trigger box. Is it plugged in?')
    
    def send_digital(self, channel, message, duration):
        '''
        channel = the digital channel to send the signal on (1 USB back to this computer, 2 DSUB-9)
        message = the byte to send, 0-255 or a single character
        duration = 10 - 655350 ms in 10 ms steps; 0 means infinite
        '''
        # construct a command according to trigger box documentation
        commandNumber = 1
        ms_div10 = int(duration/10)
        time_bytes = ms_div10.to_bytes(2, byteorder='big', signed=True)
        command = bytearray(self.startCharacter)
        for i in [commandNumber, channel, message]:
            if type(i) == int:
                command.extend(i.to_bytes(1,'big', signed=True))
            elif type(i) == str:
                command.extend(i.encode('utf-8'))
        command.extend(time_bytes)

        # send the command to the trigger box
        self.ser.write(command)
    
    def send_analog(self, channel, voltage, duration):
        '''
        channel = the analog BNC channel to send the signal on (3-7)
        voltage = 0 - 5 V in 0.1 V steps
        duration = 10 - 655350 ms in 10 ms steps; 0 means infinite
        '''
        # construct a command according to trigger box documentation
        commandNumber = 2
        outputLevel = int(voltage*10)
        ms_div10 = int(duration/10)
        time_bytes = ms_div10.to_bytes(2, byteorder='big', signed=True)
        command = bytearray(self.startCharacter)
        for i in [commandNumber, channel, outputLevel]:
            command.extend(i.to_bytes(1,'big', signed=True))
        command.extend(time_bytes)

        # send the command to the trigger box
        self.ser.write(command)
        
    def send_cancel(self, channel):
        '''
        cancel a previously activated trigger on a given channel (1-7)
        '''
        # construct a command according to trigger box documentation
        commandNumber = 3
        command = bytearray(self.startCharacter)
        for i in [commandNumber, channel, 0, 0, 0]:
            command.extend(i.to_bytes(1,'big', signed=True))       

        # send the command to the trigger box
        self.ser.write(command)
        