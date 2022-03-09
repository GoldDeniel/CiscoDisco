import socket
from struct import pack
import sys
import time
import string
import time

#getting setting target ip
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

import sounddevice as sd
import numpy as np

def send_packages(deci):

    #letters = string.ascii_letters
    #send_data = ''.join(random.choice(letters) for i in range(random.randint(1,100)))
    send_data = 'package'
    time.sleep(.0001)
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print("Sent data: ", send_data, " ", deci)

def print_sound(indata, outdata, frames, time_, status):
    volume_norm = np.linalg.norm(indata)*10
    
    #print ("|" * int(volume_norm - 6))
    #outputVolume = (int(volume_norm) * .0001)
    



    outputVolume = int(volume_norm)
    #print(outputVolume)

    for x in range(round(outputVolume * 0.25)):
        send_packages(outputVolume)
with sd.Stream(callback=print_sound):
    sd.sleep(100000)

#sending

#while True:
    #get_speaker_output_volume()

s.close()