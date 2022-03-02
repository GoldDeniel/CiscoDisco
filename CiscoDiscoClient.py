import socket
import sys
import time
import string


#getting setting target ip
if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
    exit(1)






s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# sending
while True:

    letters = string.ascii_letters
    #send_data = ''.join(random.choice(letters) for i in range(random.randint(1,100)))
    send_data = 'package'
    time.sleep(.0001)
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print("Sent data: ", send_data)
s.close()