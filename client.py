from pynput.keyboard import Key, Listener
import socket
import json

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def on_press(key):
    
    if key == Key.up:
        s.sendall(bytes(json.dumps({'key':'w','action':'pressed'}),encoding="utf-8"))
        
    elif key == Key.down:
        s.sendall(bytes(json.dumps({'key':'s','action':'pressed'}),encoding="utf-8"))
        
    elif key == Key.left:
        s.sendall(bytes(json.dumps({'key':'a','action':'pressed'}),encoding="utf-8"))
        
    elif key == Key.right:
        s.sendall(bytes(json.dumps({'key':'d','action':'pressed'}),encoding="utf-8"))

def on_release(key):
    
    if key == Key.up:
        s.sendall(bytes(json.dumps({'key':'w','action':'released'}),encoding="utf-8"))
        
    elif key == Key.down:
        s.sendall(bytes(json.dumps({'key':'s','action':'released'}),encoding="utf-8"))
        
    elif key == Key.left:
        s.sendall(bytes(json.dumps({'key':'a','action':'released'}),encoding="utf-8"))
        
    elif key == Key.right:
        s.sendall(bytes(json.dumps({'key':'d','action':'released'}),encoding="utf-8"))

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
