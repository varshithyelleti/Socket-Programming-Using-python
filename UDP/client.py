import socket
import time
import random

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 8080
##Message = "10"
import struct
while True:
    Message=str(1.22222)
    
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(Message.encode('ascii'), (UDP_IP_ADDRESS, UDP_PORT_NO))
##    time.sleep(1)
