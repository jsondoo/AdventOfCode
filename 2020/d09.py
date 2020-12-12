from collections import defaultdict
import re

f = open('./d9.txt', 'r')
rows = f.read().split("\n")
rows = [int(x) for x in rows]

preamble = 25

print(rows)

def is_valid(num, start, end):
  for i in range(start,end):
    for j in range(i+1,end):
      if rows[i] != rows[j] and rows[i] + rows[j] == num:
        return True
  return False

# 0-24 are the first 25 numbers
for i in range(25, len(rows)):
  curr = rows[i]
  if not is_valid(curr, i-25, i):
    print(curr)

# Part 1: 15690279

target = 15690279

# try all subarrays 
curr_sum = 0

start, end = None, None
for i in range(0,len(rows)):
  curr_sum += rows[i]
  for j in range(i+1, len(rows)):
    curr_sum += rows[j]
    if curr_sum == target:
      start = i
      end = j

  curr_sum = 0

print(max(rows[start:end+1]) + min(rows[start:end+1]))

# Part 2: 2174232