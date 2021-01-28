#!/usr/bin/env python3

import serial
import sys
import glob

def listSerialPorts():
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/cu.usbserial-*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        result.append(port)
    return result

def setupSerial(serPort):
    global ser
    
    print('Connected')
    ser = serial.Serial(serPort, baudrate=9600, timeout=1)

def closeSerial():
    global ser
    try:
        print('Disconnected')
        ser.__del__()
    except Exception as e:
        print(e)
        pass

def recvData():
    data = ser.readline()
    if data != b'':
        print(data.decode().rstrip())
