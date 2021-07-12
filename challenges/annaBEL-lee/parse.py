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
  packets.append({ 'time': time, 'data': data[1:-1].split("|") })

def hexdump(bytes):
  print("|", end="")
  for byte in bytes:
    n = int(byte, 16)
    print(chr(n) if 32 <= n <= 127 else ".", end="")
  print("|", end="")

def filter(packet):
  if packet['data'][0x2f][1] == "0": return False # filter ack only packets
  return True

for packet in packets:
  if not filter(packet): continue
  print(packet['time'] + "  ", end="")
  bytes = packet['data']
  print(" ".join(packet['data'][-2:]))
