import math
import collections

data = open('input.txt', 'r').read().split('\n')
data = [list(r) for r in data]

# print(data)

# (x,y) -> data[y][x]

aesteroid = [] # coordinates of all the aesteroids

for r in range(len(data)):
  for c in range(len(data[0])):
    if data[r][c] == '#':
      aesteroid.append((c,r))

num_rows = len(data)
num_cols = len(data[0])
# print(aesteroid)

ans = float('-inf')
best_a = None
for a1 in aesteroid:
  mapp = data.copy()
  distances = []
  for a2 in aesteroid:
    dx, dy = abs(a1[0] - a2[0]), abs(a1[1] - a2[1])
    c = math.sqrt(dx*dx + dy*dy)
    distances.append((a2, c)) # coords, distance tuple
  
  # go through aesteroids in sorted order
  distances.sort(key=lambda x: x[1])
  can_see = 0
  distances.pop(0) # first aesteroid is itself
  visited = collections.defaultdict(bool)

  print('curr aesteroid', a1)

  for a2, _ in distances:
    if not visited[a2]:
      # print(a2)
      can_see += 1

      dx, dy = a2[0] - a1[0], a2[1] - a1[1]
      if dx == 0:
        cx, cy = a2[0], a2[1]
        while 0 <= cx < num_cols and 0 <= cy < num_rows:
          visited[(cx,cy)] = True
          cy += -1 if dy < 0 else 1
      elif dy == 0:
        cx, cy = a2[0], a2[1]
        while 0 <= cx < num_cols and 0 <= cy < num_rows:
          visited[(cx,cy)] = True
          cx += -1 if dx < 0 else 1
      else:
        cx, cy = a2[0], a2[1]
        while 0 <= cx < num_cols and 0 <= cy < num_rows:
          visited[(cx,cy)] = True
          cx += dx
          cy += dy
  print(can_see)

  if can_see > ans:
    ans = can_see
    best_a = a1


print('ans', ans)
print(best_a)