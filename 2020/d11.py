from collections import defaultdict
import re

f = open('./d11.txt', 'r')
rows = f.read().split("\n")

curr = [list(x) for x in rows]

num_rows = len(curr)
num_cols = len(curr[0])


# def no_adjacent_occupied(curr, r, c):
#   for r1 in range(r-1,r+2):
#     for c1 in range(c-1,c+2):
#       if 0 <= r1 < num_rows and 0 <= c1 < num_cols:
#         if curr[r1][c1] == '#':
#           return False

#   return True

def eight_direction_no_occupied(curr,r,c):
  # check in 8 directions and see if there are any occupied seats
  # true if there no occupied in the 8 directions
  # (r,c)
  slopes = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  for (dr, dc) in slopes:
    curr_r, curr_c = r,c
    
    while True:
      # advance once in the direction
      curr_r += dr
      curr_c += dc

      if 0 <= curr_r < num_rows and 0 <= curr_c < num_cols:
        if curr[curr_r][curr_c] == '#':
          return False
        elif curr[curr_r][curr_c] == 'L':
          break
      else: # reached end
        break

  return True

def five_plus_occupied(curr, r, c):
  count = 0
  slopes = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  for (dr, dc) in slopes:
    curr_r, curr_c = r,c
    
    while True:
      # advance once in the direction
      curr_r += dr
      curr_c += dc

      if 0 <= curr_r < num_rows and 0 <= curr_c < num_cols:
        if curr[curr_r][curr_c] == '#':
          count += 1
          break
        elif curr[curr_r][curr_c] == 'L':
          break
      else: # reached end
        break

  return count >= 5


def pretty_list(lst):
  for row in lst:
    print(''.join(row))

def get_next(curr):
  after = [[0] * num_cols for i in range(num_rows)]

   # figure out next state
  for r, row in enumerate(curr):
    for c, ch in enumerate(row):
      if ch == '.':
        after[r][c] = '.'
      elif ch == 'L':
        res = eight_direction_no_occupied(curr, r,c)
        if res:
          after[r][c] = '#'
        else:
          after[r][c] = 'L'
      elif ch == '#':
        res = five_plus_occupied(curr,r,c)
        if res:
          after[r][c] = 'L'
        else:
          after[r][c] = '#'

  return after

while True:
  after = get_next(curr)
  if curr == after:
    break
  else:
    curr = after

pretty_list(curr)

count = 0 
for r in curr:
  for ch in r:
    if ch == '#':
      count += 1
print(count)