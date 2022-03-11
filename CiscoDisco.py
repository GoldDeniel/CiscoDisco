import socket
from struct import pack
import sys
import time
import time
import sounddevice as sd
import numpy as np

# getting setting target ip

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    ip = "127.0.0.1"
    port = 500
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# getting the terminal length in a way that doesn't crash ALSA

def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])

(rows, height) = getTerminalSize() # saving them in variables

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
    time.sleep(10000)

s.close()