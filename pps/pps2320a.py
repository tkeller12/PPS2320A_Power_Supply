import serial
from serial.tools import list_ports
import time

class pps(object):

    def __init__(self, port = None):

        # Automatically detect serial port
        if port == None:
            print('Automatically Detecting Port...')
            comports = list_ports.comports()
            for comport in comports:
                print(comport)
                if "Silicon Labs CP210x USB to UART Bridge" in comport.description:
                    port = comport.device

        print('here')
        print('Initializing Serial Port')
        if port == None:
            print('Could not identify com Port')
        self.ser = serial.Serial(port, baudrate = 9600, timeout = 0.1)
        print('Done.')
    

    def send_command(self, command, bytes_to_read = 3):
        '''
        '''

        if command[-1] != '\n':
            command += '\n'

        self.ser.write(command.encode('utf-8'))

        data = self.ser.read(bytes_to_read).decode('utf-8')

        data = data.strip()

        return data
        
    def voltage(self, value = None, channel = 1):
        ''' Set power supply voltage

            Args:
                value (int, float): Voltage value to set in volts
                channel (int): Power supply channel to set

            Returns:
                data (float): If value is None, power supply voltage in volts
        '''

        if channel not in (1,2):
            raise ValueError('Channel not valid')

        if value is not None:
            if channel == 1:
                command = 'su'
            elif channel == 2:
                command = 'sa'
        else:
            if channel == 1:
                command = 'ru'
            else:
                command = 'rk'

        if value is not None:
            value = int(value * 100)
            if (value > 3200) or (value < 0):
                raise ValueError('Value out of range')

            command += '%04i'%value

        data = self.send_command(command)

        if value is not None:
            if data != 'ok':
                raise ValueError('Communication fail')

        else:
            output = float(data.strip())/100.
            return output

    def current(self, value = None, channel = 1):
        ''' Set power supply voltage

            Args:
                value (int, float): Voltage value to set in volts
                channel (int): Power supply channel to set
                
            Returns:
                data (float): If value is None, returns power supply current value in Amps

        '''

        if channel not in (1,2): #NOTE FIX this
            ValueError('channel %s not valid'%str(channel))

        if value is not None:
            if channel == 1:
                command = 'si'
            elif channel == 2:
                command = 'sd'
        else:
            if channel == 1:
                command = 'ri'
            if channel == 2:
                command = 'rq'

        if value is not None:
            value = int(value * 1000)
            if (value > 3100) or (value < 0):
                raise ValueError('Value out of range')

            command += '%04i'%value

        data = self.send_command(command)

        if value is not None:
            if data != 'ok':
                raise ValueError('Communication fail')

        else:
            output = float(data.strip())/1000.
            return output


    def output(self, enabled):
        ''' Enable or disable power supply output

            enable (bool): True to enable, False to disable
        '''

        if enabled:
            data = self.send_command('o1')
        else:
            data = self.send_command('o0')


        if data != 'ok':
            raise ValueError('Communication fail')

