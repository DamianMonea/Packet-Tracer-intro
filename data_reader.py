import sys
import glob
import serial
import socket
import serial.tools.list_ports

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class DataReader:
    def _init_(self):
        this.ports = serial.tools.list_ports.comports()
        this.serialPort = serial.Serial(port="/dev/ttyACM0", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        while(True):
            serialString = serialPort.read()
            if (serialPort.in_waiting > 0):
                serialString = serialPort.readline()
                print(serialString.decode("ascii"))


if __name__ == '__main__':
    print(serial_ports())
    ports = serial.tools.list_ports.comports()
    serialPort = serial.Serial(port="/dev/ttyACM0", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    while(True):
        serialString = serialPort.read()
        if (serialPort.in_waiting > 0):
            serialString = serialPort.readline()
            print(serialString.decode("ascii"))
