from collections import defaultdict
import re

# start = [17,1,3,16,19,0]
start = [17,1,3,16,19,0]

seen = defaultdict(list) # which turns the number was seen 0:[1,2,3]
counts = defaultdict(int)
for idx, num in enumerate(start):
  seen[num].append(idx+1)
  counts[num] += 1

turn = len(start) + 1
last_number = start[-1]

while turn <= 30000000:
  if counts[last_number] == 1:
    last_number = 0
  else:
    last_number = seen[last_number][-1] - seen[last_number][-2]

  counts[last_number] += 1
  seen[last_number].append(turn)
  turn += 1

print(last_number)