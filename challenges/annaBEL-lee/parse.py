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

