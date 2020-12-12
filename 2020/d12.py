from collections import defaultdict
import re

f = open('./d12.txt', 'r')
rows = f.read().split("\n")

LL = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
RR = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

direction = 'E'

# way point position (relative distance from ship)
wx, wy = 10,1

# ships position (relative to origin)
dx, dy = 0,0

for line in rows:
  op = line[0]
  val = int(line[1:])

  if op == 'F':
    while val > 0:
      dx += wx
      dy += wy
      val -= 1
  elif op == 'N':
    wy += val
  elif op == 'S':
    wy -= val
  elif op == 'W':
    wx -= val
  elif op == 'E':
    wx += val
  elif op == 'R':
    while val >= 90:
      temp_wx, temp_wy = None, None

      temp_wy = -1 * wx
      temp_wx = wy
      
      wx = temp_wx
      wy = temp_wy
      
      val -= 90
  elif op == 'L':
    while val >= 90:
      temp_wx, temp_wy = None, None
      if wx >= 0:
        temp_wy = wx
      elif wx < 0:
        temp_wy = wx
      if wy >= 0:
        temp_wx = -1 * wy
      elif wy < 0:
        temp_wx = -1 * wy
      
      wx = temp_wx
      wy = temp_wy
      val -= 90

print(abs(dx) + abs(dy))
