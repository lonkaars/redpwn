#!/bin/python3
file = open("./round-the-bases")
content = file.read()
file.close()

n = 30
arr = [ content[i : i + n] for i in range(0, len(content), n) ]

arr2 = []
gert = set()
for line in arr:
  sub = line[16:20]
  if sub == 'IIcu':
    arr2.append('0')
  else:
    arr2.append('1')

arr2 = ''.join(arr2)

for i in range(0, len(arr2), 8):
  print(chr(int(arr2[i:i+8], 2)), end='')

print("\n", end='')
