import collections

memory = list(map(int,open('input.txt', 'r').read().split(',')))
memory = collections.defaultdict(int, enumerate(memory)) # infinite memory

def val(mode, index, offset):
  if mode == 0: # position mode
    return memory[memory[index]]
  elif mode == 1: # immediate mode
    return memory[index]
  elif mode == 2:
    return memory[memory[index] + offset]

def intcode(inp): 
  offset, pc = 0, 0

  while pc < len(memory):
    opcode = memory[pc] % 100
    modes = list(map(int,("%05d" % memory[pc])[0:3])) # modes[0] is A, modes[1] is B, modes[2] is C

    if opcode == 1: # add
      p1 = val(modes[2], pc+1, offset)
      p2 = val(modes[1], pc+2, offset)
      p3 = memory[pc+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = p1 + p2
      pc += 4
    elif opcode == 2: # multiply
      p1 = val(modes[2], pc+1, offset)
      p2 = val(modes[1], pc+2, offset)
      p3 = memory[pc+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = p1 * p2
      pc += 4
    elif opcode == 3: # get input
      p1 = memory[pc+1] + (offset if modes[2] == 2 else 0)
      memory[p1] = inp
      pc += 2
    elif opcode == 4: # print output
      p1 = memory[pc+1] + (offset if modes[2] == 2 else 0)
      if modes[2] == 1:
        print(p1)
      else:
        print(memory[p1])
      pc += 2
    elif opcode == 5: # jump if true
      p1 = val(modes[2], pc+1, offset)
      p2 = val(modes[1], pc+2, offset)
      pc = p2 if p1 != 0 else pc + 3
    elif opcode == 6: # jump if false
      p1 = val(modes[2], pc+1, offset)
      p2 = val(modes[1], pc+2, offset)
      pc = p2 if p1 == 0 else pc + 3
    elif opcode == 7: # less than
      p1 = val(modes[2], pc+1, offset)
      p2 = val(modes[1], pc+2, offset)
      p3 = memory[pc+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = 1 if p1 < p2 else 0
      pc += 4
    elif opcode == 8: # equal to
      p1 = val(modes[2], pc+1, offset)
      p2 = val(modes[1], pc+2, offset)
      p3 = memory[pc+3] + (offset if modes[0] == 2 else 0)
      memory[p3] = 1 if p1 == p2 else 0
      pc += 4
    elif opcode == 9: # adjust offset
      p1 = val(modes[2], pc+1, offset)
      offset += p1
      pc += 2
    elif opcode == 99:
      return
    else:
      print(f'opcode {opcode} does not exist')
      return

intcode(1) # PART 1
intcode(2) # PART 2


