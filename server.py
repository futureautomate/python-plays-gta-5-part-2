#!/usr/bin/env python3

import socket
import json
from keyboard import PressKey,ReleaseKey

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

KeyboardDict = {'w':0x11,'a':0x1E,'s':0x1F,'d':0x20}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True: 
            data = conn.recv(1024)
            if data:
                if json.loads(data.decode('utf8'))['action'] == 'pressed':
                    PressKey(KeyboardDict[json.loads(data.decode('utf8'))['key']])
                else:
                    ReleaseKey(KeyboardDict[json.loads(data.decode('utf8'))['key']])

