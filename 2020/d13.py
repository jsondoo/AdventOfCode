from collections import defaultdict
import re

f = open('./d13.txt', 'r')
rows = f.read().split("\n")
inst = rows[1].split(',')

bus_ids = list(filter(lambda x: x != 'x', inst))
bus_ids = list(map(lambda x: int(x), bus_ids))
print(bus_ids)

offsets = []

prev_idx = None
for idx, ch in enumerate(inst):
  if ch != 'x':
    offsets.append(-idx)
print(offsets)

# Part 2: used chinese remainder theorem
# system of congruences:
# x = -0  (mod 19)
# x = -13 (mod 37)
# x = -19 (mod 523)
# x = -37 (mod 13)
# x = -42 (mod 23)
# x = -48 (mod 29)
# x = -50 (mod 547)
# x = -60 (mod 41)
# x = -67 (mod 17)



from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print(offsets)
print(bus_ids)
print(chinese_remainder(bus_ids, offsets))