from collections import defaultdict
import re

f = open('./d17.txt', 'r')
rows = f.read().split("\n")

grid = {} # triplet to a state (# or .)

num_rows = len(rows)
num_cols = len(rows[0])
print(num_cols)

# initialize inactive dimension
for w in range(-10,10): 
  for z in range(-10,10):
    for r in range(-10,num_rows+10):
      for c in range(-10, num_cols+10):
        grid[(r,c,z,w)] = '.'

# initial given input
for r, row in enumerate(rows):
  for c,ch in enumerate(row):
    grid[(r,c,0,0)] = ch

def compute_next_grid(grid):
  next_grid = {}
  for coordinate, state in grid.items():
    # count active neighbors
    count_active = 0

    for dw in (-1,0,1):
      for dz in (-1,0,1):
        for dr in (-1,0,1):
          for dc in (-1,0,1):
            tup = (dr,dc,dw,dz)
            if tup != (0,0,0,0):
              res = res = tuple(map(lambda i, j: i + j, coordinate, tup)) 
              if res in grid and grid[res] == '#': # should be big enoguh to get anything
                count_active += 1

    if state == '#':
      if count_active == 2 or count_active == 3:
        next_grid[coordinate] = '#'
      else:
        next_grid[coordinate] = '.'
    elif state == '.':
      if count_active == 3:
        next_grid[coordinate] = '#'
      else:
        next_grid[coordinate] = '.'

  return next_grid


for i in range(6):
  next_grid = compute_next_grid(grid)
  grid = next_grid


count = 0
for _, state in grid.items():
  if state == '#':
    count += 1

print(count)