import collections

memory = list(map(int,open('input.txt', 'r').read().split(',')))
memory = collections.defaultdict(int, enumerate(memory)) # infinite memory

def intcode(inp): 
  offset, pc = 0, 0

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
      memory[p1] = inp
      pc += 2
    elif opcode == 4: # print output
      p1 = write_val[modes[2]](pc+1) 
      print(memory[p1])
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

intcode(1) # PART 1
intcode(2) # PART 2


