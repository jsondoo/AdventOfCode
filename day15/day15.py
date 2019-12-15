import collections

memory = list(map(int,open('input.txt', 'r').read().split(',')))
memory = collections.defaultdict(int, enumerate(memory)) # infinite memory



def intcode():
  offset, pc = 0, 0
  outputs = collections.deque()

  rx, ry = 0, 0
  # graph 
  queue = collections.deque()
  queue.append((0,0,0)) # cx, cy, dist
  cx, cy, dist = None, None, None
  visited = set()
  visited.add((0,0))
 
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
      if cx is None and cy is None and dist is None:
        cx, cy, dist = queue.popleft()
        visited.add((cx,cy))
        # print('here')
        print(cx,cy,dist)
      
      if cx != rx:
        if cx < rx:
          memory[p1] = 3
          rx -= 1
        else:
          memory[p1] = 4
          rx += 1
      elif cy != ry:
        # print('cy != ry')
        if cy < ry:
          memory[p1] = 1
          ry -= 1
        else:
          memory[p1] = 2
          ry += 1
      elif len(outputs) == 0:
        # query north
        memory[p1] = 1
      elif len(outputs) == 1:
        # query south
        memory[p1] = 2
      elif len(outputs) == 2:
        # query west
        memory[p1] = 3
      elif len(outputs) == 3:
        # query east
        memory[p1] = 4
      elif len(outputs) == 4:
       # print(outputs)
        for i, q in enumerate(outputs):
          # print(i,q)
          if q == 0:
            continue
          elif q == 2:
            return dist + 1
          else: # add to queue
            if i == 0: # N
              if (cx,cy-1) not in visited:
                # print('N')
                queue.append((cx,cy-1,dist+1))
            elif i == 1: # S
              if (cx,cy+1) not in visited:
                queue.append((cx,cy+1,dist+1))
            elif i == 2: # W
              if (cx-1,cy) not in visited:
                queue.append((cx-1,cy,dist+1))
            elif i == 3: # E
              if (cx+1,cy) not in visited:
                queue.append((cx+1,cy,dist+1))

        # print('queue',queue)
        cx, cy, dist = None, None, None
        outputs = collections.deque()

      pc += 2
    elif opcode == 4: # print output
      p1 = read_val[modes[2]](pc+1)
      if cx is not None and cy is not None and cx == rx and cy == ry:
        outputs.append(p1)
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


print(intcode())