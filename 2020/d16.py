from collections import defaultdict
import re

f = open('./d16.txt', 'r')
rows = f.read().split("\n\n")

range_list = []
field_to_ranges = defaultdict(list)
parts = rows[0].split("\n")
for p in parts:
  numbers = p.split(':')
  ranges = numbers[1].strip().split("or")
  for r in ranges:
    num1, num2 = r.split("-")
    tup = (int(num1),int(num2))
    field_to_ranges[numbers[0]].append(tup)
    range_list.append(tup)

def check_valid(value):
  for r in range_list:
    if r[0] <= value <= r[1]:
      return True
  return False

valid_tickets = []

tickets = rows[-1].split('\n')[1:]

for ticket in tickets:
  valid = True
  values = ticket.split(',')
  for value in values:
    value = int(value)
    if not check_valid(value):
      valid = False
      break
  
  if valid:
    valid_tickets.append(ticket)

print(valid_tickets)
columns = list(zip(*[[int(x) for x in valid_ticket.split(',')] for valid_ticket in valid_tickets]))

possibles = []
for column in columns:
  possible = set(field_to_ranges.keys())

  for value in column:
    for field, ranges in field_to_ranges.items():
      # see if value works for current ranges
      rangeA, rangeB = ranges[0], ranges[1]
      if rangeA[0] <= value <= rangeA[1] or rangeB[0] <= value <= rangeB[1]:
        continue
      elif field in possible:
        possible.remove(field)

  possibles.append(possible)

ans = {}
while True:
  if len(ans) == 20:
    break
  for idx, p in enumerate(possibles):
    if len(p) == 1:
      field = list(p)[0]
      ans[idx] = field
      for idx, p in enumerate(possibles):
        if len(p) > 0:
          p.remove(field)
          possibles[idx] = p
      break

indexes = []
for k,v in ans.items():
  if "departure" in v:
    indexes.append(k)

total = 1
_, my_ticket = rows[1].split('\n')
vals = [int(x) for x in my_ticket.split(',')]
for idx in indexes:
  total *= vals[idx]
print(total)