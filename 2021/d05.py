with open('./input.txt','r') as f:
  lines = [x for x in list(f.readlines())]

points = []
for line in lines:
  p1, p2 = line.split(" -> ")
  r1, c1 = p1.split(",")
  r2, c2 = p2.split(",")
  point = [(int(r1),int(c1)),(int(r2),int(c2))]
  points.append(point)

sz = 1111
grid = [[0 for _ in range(sz)] for _ in range(sz)]   

def part1():
  # just run part 2 without the diagonal case for part 1
  return 0

def part2():
  for point in points:
    p1, p2 = point
    x1, y1 = p1
    x2, y2 = p2

    # y becomes row, x becomes column
    # horizontal e.g. (0,9) to (5,9), same row
    if y1 == y2:
      # make x1 <= x2
      if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
      
      for c in range(x1, x2+1):
        grid[y1][c] += 1

    elif x1 == x2: # vertical, e.g. (1,3) to (1,5), same column
      # make y1 <= y2
      if y1 > y2:
        temp = y1
        y1 = y2
        y2 = temp

      for r in range(y1, y2+1):
        grid[r][x1] += 1
    else: # diagonal cases
      # e.g. (1,1) to (3,3) pr (9,7) to (7,9)
      # make x1 <= x2, increasing column
      if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = temp

      if y2 < y1:
        # going up (+1, -1)
        curr_x, curr_y = x1, y1

        while True:
          grid[curr_y][curr_x] += 1
          if curr_x == x2 and curr_y == y2:
            break
          curr_x += 1
          curr_y -= 1
      else: 
        # going down (+1, +1)
        curr_x, curr_y = x1, y1

        while True:
          grid[curr_y][curr_x] += 1
          if curr_x == x2 and curr_y == y2:
            break
          curr_x += 1
          curr_y += 1
  
  count = 0

  for row in grid:
    for num in row:
      if num >= 2:
        count += 1

  return count

if __name__ == '__main__':
  print(part1())
  print(part2())