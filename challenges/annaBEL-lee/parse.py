#!/bin/python3
file = open("./gedoe.txt")
content = file.read()
file.close()

lines = content.split("+---------+---------------+----------+")

packets = []

for line in lines:
  trim = line.strip()
  split = trim.split("\n")
  if len(split) < 2: continue
  time = split[0].split(" ")[0]
  data = split[1].strip()[5:]
  packets.append({ 'time': time, 'data': data })

def hexdump(bytes):
  print("|", end="")
  for byte in bytes:
    n = int(byte, 16)
    print(chr(n) if 32 <= n <= 127 else ".", end="")
  print("|", end="")

for packet in packets:
  print(packet['time'] + "  ", end="")
  bytes = packet['data'][1:-1].split("|")
  for i in range(0, len(bytes), 16):
    if i != 0: print(" " * ( len(packet['time']) + 2 ), end="")
    print(' '.join(bytes[i:i+16]), end="")
    print("  ", end="")
    hexdump(bytes[i:i+16])
    print("\n", end="")
