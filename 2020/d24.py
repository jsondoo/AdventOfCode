from collections import defaultdict
import re

f = open('test.txt', 'r')
rows = f.read().split("\n")

# default is white (False)
# True if coordinate is black
hex_grid = defaultdict(bool)

for row in rows:
  idx = 0
  q,r = 0,0
  while idx < len(row):
    if row[idx] == 'e':
      q += 1
      idx += 1
    elif row[idx] == 'w':
      q -= 1
      idx += 1
    elif row[idx] == 'n':
      if row[idx+1] == 'e':
        q += 1
        r -= 1
        idx += 2
      elif row[idx+1] == 'w':
        r -= 1
        idx += 2
    elif row[idx] == 's':
      if row[idx+1] == 'e':
        r += 1
        idx += 2
      elif row[idx+1] == 'w':
        q -= 1
        r += 1
        idx += 2
  hex_grid[(q,r)] = not hex_grid[(q,r)]

print(sum(hex_grid.values())) # PART 1

# add neighbors of all current tiles
num_days = 100
neighbors = [(-1,0),(1,0),(0,-1),(1,-1),(-1,1),(0,1)]

def expand(grid):
  # add neighbors
  for (q,r) in list(grid.keys()):
    for (dq,dr) in neighbors:
      if (q+dq, r+dr) not in grid:
        grid[(q+dq, r+dr)] = False

for day in range(num_days):
  expand(hex_grid)

  # create next state
  next_hex_grid = {}

  for (q,r) in list(hex_grid.keys()):
    blacks = 0
    for (dq,dr) in neighbors:
      if (q+dq, r+dr) in hex_grid and hex_grid[(q+dq, r+dr)]:
        blacks += 1
      
    if hex_grid[q,r]:
      next_hex_grid[(q,r)] = not (blacks == 0 or blacks > 2)
    else: 
      next_hex_grid[(q,r)] = blacks == 2
  
  hex_grid = next_hex_grid

print(sum(hex_grid.values()))