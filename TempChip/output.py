import serial
import time

ser = serial.Serial('COM4', 9800, timeout=1)


for i in range(10):
    with serial.Serial('COM4', 9800, timeout=1) as ser:
        time.sleep(0.5)
        ser.write(b'H')   # send the pyte string 'H'
        time.sleep(0.5)   # wait 0.5 seconds
        ser.write(b'L')   # send the byte string 'L'




def read_cold_reservior():
    """

    :return:
    """
    return cold_reservior_temp


def read_hot_reservior():
    """

    :return:
    """
    return hot_reservior_temp


def read_chip():
    """

    :return:
    """
    return chip_temp


def feedback_cold_res():



def feedback_hot_res():


