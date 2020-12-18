from collections import defaultdict
import re
import numpy

f = open('./d18.txt', 'r')
rows = f.read().split("\n")

def evaluate(exp):
  if "(" in exp:
    opening, ending = 0,0
    for idx, ch in enumerate(exp):
      if ch == '(':
        opening = idx
      elif ch == ')':
        ending = idx
        break
    sub_exp = exp[opening+1:ending]
    sub_total = evaluate(sub_exp)
    new_exp = exp[:opening] + str(sub_total) + exp[ending+1:]
    return evaluate(new_exp)
  else:
    total = 0
    parts = exp.split(" ")

    if '+' not in parts:
      total = 1
      # reduce mult
      for val in parts:
        if val != '*':
          total *= int(val)

      return total

    reduced = None
    curr = 0
    for ch in parts:
      if ch != '+' and ch != '*':
        curr += int(ch)
      elif ch == '*':
        if reduced is None:
          reduced = curr
        else:
          reduced *= curr
        curr = 0

    if reduced is None:
      return curr
    else:
      return reduced * curr

total = 0
for expression in rows:
  res = evaluate(expression)
  total += res

print(total)