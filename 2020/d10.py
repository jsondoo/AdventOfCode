from collections import defaultdict
import re

f = open('./d10.txt', 'r')

# each row as a string, splits by all whitespaces (spaces, newlines, tab)
rows = f.read().split("\n")
jolts = [int(x) for x in rows]

jolts.append(0)
jolts.sort()
jolts.append(max(jolts) + 3)

# one_jolts = 0
# three_jolts = 0
# for i in range(1, len(jolts)):
#   if jolts[i] - jolts[i-1] == 1:
#     one_jolts += 1
#   elif jolts[i] - jolts[i-1] == 3:
#     three_jolts += 1

# print(one_jolts, three_jolts)
# print(one_jolts * three_jolts)

print(jolts)

def to_string(lst):
  return ','.join(str(x) for x in lst)

def to_list(st):
  return [int(x) for x in st.split(',')]


dic = {}
def num_jolts(js):
  if len(js) == 1: # 1 item in list
    return 1

  # write to memo
  if to_string(js) in dic:
    print('yo')
    return dic[to_string(js)]

  first = js[0]
  
  total_ways = 0
  # look at the next three elements, at index 1,2,3
  for i in range(1,min(4,len(js))):
    if js[i] - first <= 3:
      res = num_jolts(js[i:])
      total_ways += res

  # read from memo
  dic[to_string(js)] = total_ways
  
  return total_ways

print(num_jolts(jolts))