from collections import defaultdict
from functools import lru_cache
import re
import itertools

f = open('./d19.txt', 'r')
rows = f.read().split("\n\n")

rules = {}
alphas = set()
for rule in rows[0].split('\n'):
  num, rule = rule.split(':')
  if 'a' in rule or 'b' in rule:
    alphas.add(int(num))
    rules[int(num)] = rule.strip().replace('"',"")
  else:
    rules[int(num)] = rule

lengths = set()
for s in rows[1].split('\n'):
  lengths.add(len(s))

# # PART 2: additional rules with loops
rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'

def generate(val, depth = 1): # number  -> set of strings
  # base case
  if rules[val] == 'a':
    return ['a']
  elif rules[val] == 'b':
    return ['b']

  parts = [p.strip() for p in rules[val].split('|')]
  
  top_results = []
  for part in parts:
    # concatenate result of all numbers in parts

    vals = [int(x) for x in part.split(' ')]
    results = []
    for val in vals:
      results.append(generate(val, depth + 1))

    for tup in itertools.product(*results):
      st = ''.join(tup)
      top_results.append(st)

  return top_results

# PART 1
# count = sum(map(lambda s: s in possible, rows[1].split('\n')))
# print(count)



# part 2
# 0: 8 11
# 8: 42 | 42 8 -> match (42)+
# 11: 42 31 | 42 11 31 -> match (42) n times and 31 n times

r42 = generate(42)
r31 = generate(31)

sz = len(r42[0])
def match42(s): # return num matches and remaining string
  curr = sz
  count = 0
  while curr <= len(s):
    if s[curr-sz:curr] in r42:
      count += 1
    else:
      break
    curr += sz
  return count

def match31(s):
  curr = sz
  count = 0
  while curr <= len(s):
    if s[curr-sz:curr] in r31:
      count += 1
    else:
      break
    curr += sz
  return count


ans = 0
for s in rows[1].split('\n'):
  r42_matches = match42(s)
  if r42_matches > 0:
    r31_matches = match31(s[(r42_matches*8):])
    total_matches = r42_matches + r31_matches
    if r31_matches > 0 and total_matches*8 == len(s) and r42_matches > r31_matches:
      ans += 1

print(ans)