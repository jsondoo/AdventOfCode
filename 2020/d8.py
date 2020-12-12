from collections import defaultdict
import re

f = open('./d8.txt', 'r')
insts = f.read().split("\n")

def run_program(idx_to_change):
  accumulator = 0
  idx = 0 # position of instruction
  seen = set() # instructions done before

  while idx < len(insts):
    if idx in seen:
      break

    seen.add(idx)

    inst = insts[idx]
    op, value = inst.split()
    value = int(value)

    # only for part 2 (use a non-index for part 1)
    if idx == idx_to_change:
      if op == "jmp":
        idx += 1
      elif op == "acc":
        accumulator += value
        idx += 1
      elif op == "nop":
        idx += value
    else:
      if op == "nop":
        idx += 1
      elif op == "acc":
        accumulator += value
        idx += 1
      elif op == "jmp":
        idx += value

  if idx == len(insts):
    return accumulator
  else:
    return None

for i in range(len(insts)):
  if run_program(i) is not None:
    print(run_program(i))

