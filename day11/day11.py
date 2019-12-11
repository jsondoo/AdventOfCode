import collections

memory = list(map(int,open('input.txt', 'r').read().split(',')))
memory = collections.defaultdict(int, enumerate(memory)) # infinite memory

# class Robot:
hull = collections.defaultdict(int) # 0 (black) by default
painted = set()
cx, cy = 0, 0
direction = (0,-1)
left = {(0,-1): (-1,0), (-1,0): (0,1), (0,1): (1,0), (1,0): (0,-1)}
right = {(0,-1): (1,0), (1,0): (0,1), (0,1): (-1,0), (-1,0): (0,-1)}

def intcode(): 
  global cx, cy, hull, painted, direction, left, right
  offset, pc = 0, 0
  outputs = collections.deque()

  while pc < len(memory):
    opcode = memory[pc] % 100
    modes = list(map(int,("%05d" % memory[pc])[0:3])) # modes[0] is A, modes[1] is B, modes[2] is C
    read_val = {0: lambda idx: memory[memory[idx]], 1: lambda idx: memory[idx], 2: lambda idx: memory[memory[idx] + offset]} 
    write_val = {0: lambda idx: memory[idx], 2: lambda idx: memory[idx] + offset} # should never be 1 (immediate mode)

    if opcode == 1: # add
      p1, p2, p3 = read_val[modes[2]](pc+1), read_val[modes[1]](pc+2), write_val[modes[0]](pc+3)
      memory[p3] = p1 + p2
      pc += 4
    elif opcode == 2: # multiply
      p1, p2, p3 = read_val[modes[2]](pc+1), read_val[modes[1]](pc+2), write_val[modes[0]](pc+3)
      memory[p3] = p1 * p2
      pc += 4
    elif opcode == 3: # get input
      p1 = write_val[modes[2]](pc+1)
      memory[p1] = 1 if cx == 0 and cy == 0 else hull[(cx,cy)]
      pc += 2
    elif opcode == 4: # print output
      p1 = read_val[modes[2]](pc+1) 
      outputs.append(p1)
      if len(outputs) == 2:
        first, second = outputs
        print(f'painting {cx},{cy} with color {first}')
        hull[(cx,cy)] = first # paint with color
        painted.add((cx,cy))
        if second == 0: # turn left 90
          direction = left[direction]
        else: # turn right 90
          direction = right[direction]
        cx, cy = cx + direction[0], cy + direction[1]
        outputs.popleft()
        outputs.popleft()
      pc += 2
    elif opcode == 5: # jump if true
      p1, p2 = read_val[modes[2]](pc+1), read_val[modes[1]](pc+2)
      pc = p2 if p1 != 0 else pc + 3
    elif opcode == 6: # jump if false
      p1, p2 = read_val[modes[2]](pc+1), read_val[modes[1]](pc+2)
      pc = p2 if p1 == 0 else pc + 3
    elif opcode == 7: # less than
      p1, p2, p3 = read_val[modes[2]](pc+1), read_val[modes[1]](pc+2), write_val[modes[0]](pc+3)
      memory[p3] = 1 if p1 < p2 else 0
      pc += 4
    elif opcode == 8: # equal to
      p1, p2, p3 = read_val[modes[2]](pc+1), read_val[modes[1]](pc+2), write_val[modes[0]](pc+3)
      memory[p3] = 1 if p1 == p2 else 0
      pc += 4
    elif opcode == 9: # adjust offset
      p1 = read_val[modes[2]](pc+1)
      offset += p1
      pc += 2
    elif opcode == 99:
      return
    else:
      print(f'opcode {opcode} does not exist')
      return

intcode() 

print(len(painted)) # PART 1

# for k,v in sorted(hull.items()):
#   print(k)
# 40 columns 6 rows
painting = [[0 for _ in range(41)] for _ in range(6)]
for y in range(6):
  for x in range(41):
    painting[y][x] = hull[(x,y)]
print(painting)

for row in painting:
  print(''.join(str(x) for x in row).replace('0','.').replace('1','#')) # PART 2