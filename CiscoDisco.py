import socket
from struct import pack
import sys
import time
import string
import time
import os
import sounddevice as sd
import numpy as np

#getting setting target ip
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
rows, columns = os.popen('stty size', 'r').read().split()


def send_packages(deci):

    send_data = 'package'
    time.sleep(.0001)
    s.sendto(send_data.encode('utf-8'), (ip, port))

    print(' ' * int(rows))
    print("|" * deci, end="\r")
def print_sound(indata, outdata, frames, time_, status):
    volume_norm = np.linalg.norm(indata)*10
    outputVolume = int(volume_norm)
    for x in range(round(outputVolume * 0.25)):
        send_packages(outputVolume)

with sd.Stream(callback=print_sound):
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(10000)

s.close()