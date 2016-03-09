#!/usr/bin/env python
#coding:utf-8

import socket
import time

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    msg = '[%s] %s' % (time.ctime(), data)
    udpSerSock.sendto(msg, addr)
    print '...received from and returned to:', addr
udpSerSock.close()

