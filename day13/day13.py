import collections

memory = list(map(int,open('input.txt', 'r').read().split(',')))
memory = collections.defaultdict(int, enumerate(memory)) # infinite memory

# GAME (22 rows 42 columns)
grid = [[0 for _ in range(43)] for _ in range(23)]


def print_grid(arr):
  for r in arr:
    print(''.join(str(x) for x in r).replace('1', 'X').replace('0', ' ').replace('4', 'o').replace('3', '^').replace('2','#'))

def find_ball(arr):
  for r in range(len(arr)):
    for c in range(len(arr[0])):
      if arr[r][c] == 4:
        return (r,c)

def find_paddle(arr):
  for r in range(len(arr)):
    for c in range(len(arr[0])):
      if arr[r][c] == 3:
        return (r, c)

def intcode():
  global grid
  offset, pc = 0, 0
  outputs = collections.deque()
  br, bc, par, pac = None, None, None, None

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
      # get the paddle and ball position
      # figure out where to move paddle give it to input
      br, bc = find_ball(grid)
      par, pac = find_paddle(grid)
      print_grid(grid)
      if bc < pac:
        memory[p1] -= 1
      elif bc > pac:
        memory[p1] += 1
      else:
        memory[p1] = 0
      pc += 2
    elif opcode == 4: # print output
      p1 = read_val[modes[2]](pc+1)
      outputs.append(p1)
      if len(outputs) == 3:
        x, y, third = outputs
        if x == -1 and y == 0:
          print('score', third)
        else:
          grid[y][x] = third
        outputs.popleft()
        outputs.popleft()
        outputs.popleft()
        # print_grid(grid)
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
print_grid(grid)