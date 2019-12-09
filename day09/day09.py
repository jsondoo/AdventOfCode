memory = list(map(int,open('input.txt', 'r').read().split(',')))

memory.extend([0] * 10000)

def val(mode, index, offset):
  if mode == 0: # position mode
    return memory[memory[index]]
  elif mode == 1: # immediate mode
    return memory[index]
  elif mode == 2:
    return memory[memory[index] + offset]

def intcode(inp): 
  offset, i = 0, 0

  while i < len(memory):
    inst = str(memory[i]) 
    inst = list('0'* (5 - len(inst)) + inst)

    opcode = int(''.join(inst[-2:]))  # opcode
    modes = list(map(int,inst[0:3]))  # parameter modes
                                      # modes[0] = A
                                      # modes[1] = B
                                      # modes[2] = C
    
    # Parameters that an instruction writes to will never be in immediate mode

    if opcode == 1: # add
      p1 = val(modes[2], i+1, offset)
      p2 = val(modes[1], i+2, offset)
      p3 = memory[i+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = p1 + p2
      i += 4
    elif opcode == 2: # multiply
      p1 = val(modes[2], i+1, offset)
      p2 = val(modes[1], i+2, offset)
      p3 = memory[i+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = p1 * p2
      i += 4
    elif opcode == 3: # get input
      p1 = memory[i+1] + (offset if modes[2] == 2 else 0)
      memory[p1] = inp
      i += 2
    elif opcode == 4: # print output
      p1 = memory[i+1] + (offset if modes[2] == 2 else 0)
      if modes[2] == 1:
        print(p1)
      else:
        print(memory[p1])
      i += 2
    elif opcode == 5: # jump if true
      p1 = val(modes[2], i+1, offset)
      p2 = val(modes[1], i+2, offset)
      i = p2 if p1 != 0 else i + 3
    elif opcode == 6: # jump if false
      p1 = val(modes[2], i+1, offset)
      p2 = val(modes[1], i+2, offset)
      i = p2 if p1 == 0 else i + 3
    elif opcode == 7: # less than
      p1 = val(modes[2], i+1, offset)
      p2 = val(modes[1], i+2, offset)
      p3 = memory[i+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = 1 if p1 < p2 else 0
      i += 4
    elif opcode == 8: # equal to
      p1 = val(modes[2], i+1, offset)
      p2 = val(modes[1], i+2, offset)
      p3 = memory[i+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = 1 if p1 == p2 else 0
      i += 4
    elif opcode == 9: # adjust offset
      p1 = val(modes[2], i+1, offset)
      offset += p1
      i += 2
    elif opcode == 99:
      return
    else:
      print('opcode does not exist')
      return

# intcode(1) # PART 1
intcode(2) # PART 2


