#!/usr/bin/env python
#coding:utf-8

import socket
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:
    while True:
        print "waiting for connection..."
        tcpCliSock, addr = tcpSerSock.accept()
        print "...connected from:", addr

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send('[%s] %s' % (ctime(), data))
except EOFError:
    tcpCliSock.close()
except KeyboardInterrupt:
    tcpCliSock.close()

tcpSerSock.close()
