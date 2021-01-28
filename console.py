#!/usr/bin/env python3

import arduinoComms as com
import time

if __name__ == '__main__':
    print(f'{"*"*10}\tWELCOME TO NELSON\'S DEBUG CONSOLE!!!\t{"*"*10}\n')

    try:
        i = 1
        ports = com.listSerialPorts()

        print('Choose a port:')
        for port in ports:
            print(f'{i}. {port}')
            i = i+1

        selectedPort = int(input())
        if selectedPort > 0: port = ports[selectedPort-1]
        else: port = ''
    except (KeyboardInterrupt, IndexError, ValueError):
        print('\nGoodbye')
        port = ''

    if port != '':
        try:
            com.setupSerial(port)
            time.sleep(2)
        except Exception as e:
            print(e)
            pass

        while True:
            try:
                com.recvData()
            except KeyboardInterrupt:
                break

        com.closeSerial()
