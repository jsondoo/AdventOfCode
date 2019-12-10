import math
import collections

data = open('input.txt', 'r').read().split('\n')
data = [list(r) for r in data]
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
  can_see = 0
  visited = set()
  ax, ay = a1[0], a1[1]
  # print('curr aesteroid', a1)

  for a2 in aesteroid:
    if a1 == a2:
      continue

    dx, dy = a2[0] - a1[0], a2[1] - a1[1]
    gcd = math.gcd(dx, dy)
    dx /= gcd
    dy /= gcd

    if (dx,dy) not in visited:
      can_see += 1
      visited.add((dx,dy))

  if can_see > ans:
    ans = can_see
    best_a = a1

print(best_a)

# PART 2
mx, my = best_a[0], best_a[1]

# compute all angles and sort from up and clockwise
angles = []
for a in aesteroid:
  if a == monitor:
    continue
  
  dx, dy = a[0] - mx, a[1] - my
  dy *= -1
  angle = math.atan2(dy,dx)
  if angle > math.pi / 2.0:
      angle -= 2 * math.pi
  angles.append((angle,a))

angles.sort(key=lambda x: x[0], reverse=True)

# rotate and vaporize
curr = 1
aesteroid_num = 200
seen = set() # seen angles

for angle, a in angles:
  if angle in seen:
    continue

  if curr == aesteroid_num:
    # get all aetroids with this angle, find the closest one
    p = []
    # print(angles)
    for xx, yy in angles:
      if xx == angle:
        p.append(yy)

    dist = []
    for ast in p: 
      dx, dy = abs(ast[0] - mx), abs(ast[1] - my)
      dist.append((ast, math.sqrt(dx*dx + dy*dy)))
    dist.sort(key=lambda x : x[1])
    print(f'vaporized aesteroid # {curr} at {dist[0][0]} at angle {angle}')
    break
  else:
    print(f'vaporized aesteroid # {curr} at angle {angle}')
    seen.add(angle)
    curr += 1







  
  