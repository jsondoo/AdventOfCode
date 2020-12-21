from collections import defaultdict
from functools import lru_cache
import re
import itertools
import numpy as np

f = open('./d20.txt', 'r')
images = f.read().split("\n\n")

edges = {} # id: int -> (top, bottom , left, right): tup(str,str,str,str)

tiles = {}
# 12 by 12 grid
for image in images:
  lines = image.split('\n')
  id = int(lines[0][5:9])

  lines.pop(0) # tile line

  top = lines[0]
  right = ''.join([x[-1] for x in lines])
  bottom = lines[-1]
  left = ''.join([x[0] for x in lines])

  edges[id] = (top, right, bottom, left)

  tiles[id] = np.array([[ch for ch in x] for x in lines])


count_matches = defaultdict(int) # tile_id: int -> num_matches: int
matched_pieces = defaultdict(list) # tile_id: int -> matched_tile_ids: list(int)
for id,v in edges.items():
  for edge in v:
    for id2, v2 in edges.items():
      if id != id2:
        for edge2 in v2:
          if edge == edge2 or edge[::-1] == edge2:
            count_matches[id] += 1
            matched_pieces[id].append((id2,edge,edge2))

# sort by pieces
corners = []
outer = []
inner = []

for id, v in count_matches.items():
  if v == 2:
    corners.append(id)
  elif v == 3:
    outer.append(id)
  elif v == 4:
    inner.append(id)

assert(len(corners) == 4)
assert(len(outer) == 40)
assert(len(inner) == 100)

# PART 2

def rotateLeft(id):
  tile = tiles[id]
  tiles[id] = np.rot90(tile)

def rotateRight(id):
  tile = tiles[id]
  tiles[id] = np.rot90(tile, 3)

def flipHorizontal(id):
  tile = tiles[id]
  tiles[id] = np.fliplr(tile)

def flipVertical(id):
  tile = tiles[id]
  tiles[id] = np.flipud(tile)


def right(id):
  tile = tiles[id]
  return ''.join(tile[:,-1])

def left(id):
  tile = tiles[id]
  return ''.join(tile[:,0])

def top(id):
  tile = tiles[id]
  return ''.join(tile[0,:])

def bottom(id):
  tile = tiles[id]
  return ''.join(tile[-1,:])

# grid (final grid of tile ids), tiles
grid = {} # (r,c) => tile_id, use tile_id for tiles
# orient first corner piece
# corners[0] => 3607
flipHorizontal(3607)
rotateLeft(3607)
grid[(0,0)] = 3607

prev_tile_id = 3607
curr_tile_id = 1031
for r in range(12):
  for c in range(12):
    if (r,c) == (0,0):
      continue
    elif r == 0: # first row
      grid[(r,c)] = curr_tile_id

      # try to match left of curr tile to right of prev tile
      count = 0
      while left(curr_tile_id) != right(prev_tile_id) and count < 4:
        rotateRight(curr_tile_id)
        count += 1

      if (left(curr_tile_id)) != (right(prev_tile_id)):
        flipVertical(curr_tile_id)

      while (left(curr_tile_id)) != (right(prev_tile_id)) and count < 8:
        rotateRight(curr_tile_id)
        count += 1

      assert((left(curr_tile_id)) == (right(prev_tile_id)))

      # find next tile
      rightEdge = right(curr_tile_id)
      next_id = None
      for piece in matched_pieces[curr_tile_id]:
        (id, edge, _) = piece
        if rightEdge == edge or rightEdge[::-1] == edge:
          next_id = id
          break

      prev_tile_id = curr_tile_id
      curr_tile_id = next_id
    else: # subsequent rows
      # match with tile in prev row
      above_tile_id = grid[(r-1,c)]
      curr_tile_id = None
      for piece in matched_pieces[above_tile_id]:
        (id, _, _) = piece
        if id not in grid.values():
          curr_tile_id = id
          break

      # match bottom of above tile to top of curr tile
      count = 0
      while bottom(above_tile_id) != top(curr_tile_id) and count < 4:
        rotateRight(curr_tile_id)
        count += 1

      if bottom(above_tile_id) != top(curr_tile_id):
        flipVertical(curr_tile_id)

      while bottom(above_tile_id) != top(curr_tile_id) and count < 8:
        rotateRight(curr_tile_id)
        count += 1

      assert(bottom(above_tile_id) == top(curr_tile_id))

      # save to grid
      grid[(r,c)] = curr_tile_id

assert(len(set(grid.values())) == 144)

# contsuct grid
puzzle = None
for r in range(12):
  row = None
  for c in range(12):
    # remove borders from tile
    tile = tiles[grid[(r,c)]]
    tile = tile[1:-1,1:-1]
    if c == 0:
      row = tile
    else:
      row = np.concatenate((row, tile), axis = 1)
  if r == 0:
    puzzle = row
  else:
    puzzle = np.concatenate((puzzle, row), axis = 0)

def pretty_print(puzzle):
  print(*(' '.join(row) for row in puzzle), sep='\n')

assert(puzzle.shape == (96,96))
pretty_print(puzzle)

'''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''
valid = set()
def find_sea_monsters(puzzle):
  # (2,19) has to be valid
  num_monsters = 0
  monster = [(0,18),(1,18),(1,17),(1,19),(1,0),(1,5),(1,6),(1,11),(1,12),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]
  for r in range(96):
    for c in range(96):
      if (r+2) < 96 and (c+19) < 96:
        is_monster = True
        for dr, dc in monster:
          if puzzle[r+dr][c+dc] != '#':
            is_monster = False
        if is_monster:
          # mark the coordinates as being used for the monster
          for dr, dc in monster:
            valid.add((r+dr, c+dc))
          num_monsters += 1

  return num_monsters

# puzzle already has a monster without reorienting xD
count = 0
for r in range(96):
  for c in range(96):
    if puzzle[r][c] == '#' and (r,c) not in valid:
      count += 1
print(count)