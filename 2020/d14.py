from collections import defaultdict
import re

f = open('./d14.txt', 'r')
rows = f.read().split("\n")

memmap = defaultdict(int)

curr_mask = 0
for instruction in rows:
  parts = instruction.split()
  if parts[0] == 'mask':
    curr_mask = parts[2]
  else:
    val = int(parts[2]) 
    mem, address = parts[0].split("[")
    address = int(address.replace("]",""))
    bin_address = format(address, 'b').zfill(36)

    new_address = ""
    for idx, ch in enumerate(curr_mask):
      if ch == '0':
        new_address += bin_address[idx]
      elif ch == '1':
        new_address += "1"
      elif ch == 'X':
        new_address += "X"
    
    def write_to_address(addr):
      if addr.count('X') == 0:
        memmap[addr] = val

      for idx, ch in enumerate(addr):
        if ch == 'X':
          write_to_address(addr[:idx] + "1" + addr[idx+1:])
          write_to_address(addr[:idx] + "0" + addr[idx+1:])
          return

    write_to_address(new_address)
                                                                                                                                          
print(sum(memmap.values()))