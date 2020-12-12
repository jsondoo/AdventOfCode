from collections import defaultdict
import re

f = open('./d7.txt', 'r')
rows = f.read().split("\n")
dic = defaultdict(list)

# construct mapping
for r in rows:
  if "no other bags." in r:
    # nothing to do
    continue
  else:
    parts = r.replace("contain ","").replace("bags","bag").split("bag")
    root_color = parts[0].strip()
    parts2 = [x.replace(".","").replace(",","").strip() for x in parts[1:]]
    parts2 = list(filter(None, parts2))
    # PART 1
    for other_color in parts2:
      no_number = re.sub('\d','',other_color).strip()
      dic[no_number].append(root_color)

    # for other_color in parts2:
    #   number = other_color.split()[0]
    #   print(number)
    #   no_number = re.sub('\d','',other_color).strip()
    #   dic[root_color].append((no_number,number))

print(dic)

# PART 1
# BFS
seen = set() # 'b', 'c'
queue = ['shiny gold']

while queue:
  curr = queue.pop(0)
  for n in dic[curr]:
    if n not in seen:
      queue.append(n)
      seen.add(n)
# print(seen)
# print(len(seen))


# PART 2
# def find_bags_in(root):
#   if len(dic[root]) == 0:
#     return 0

#   total = 0 
#   for n in dic[root]:
#     bag_name = n[0]
#     num_bags = int(n[1])
#     total += num_bags
#     total += num_bags * find_bags_in(bag_name)

#   return total


# print(find_bags_in('shiny gold'))