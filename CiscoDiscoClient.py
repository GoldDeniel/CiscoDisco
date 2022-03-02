from random import randint, random
import socket
import sys
import time
import string
import random

#getting up and stuff
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)




s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program !!")

# sending
while True:

    letters = string.ascii_letters
    #send_data = ''.join(random.choice(letters) for i in range(random.randint(1,100)))
    send_data = 'test'
    time.sleep(.0001)
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print("\n1. Client Sent : ", send_data)
s.close()