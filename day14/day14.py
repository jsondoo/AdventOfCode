import collections
import math
reactions = open('input.txt', 'r').read().split('\n')

rules = {} # map ore name to amount needed and list of ores produced

for r in reactions:
  parts = r.split('=>')
  last = parts[-1].strip().split(' ')
  amount, name = last
  amount = int(amount)

  outputs = parts[0].split(',')
  produced = []
  for o in outputs:
    amounts, ore_name = o.strip().split(' ')
    produced.append((ore_name, int(amounts)))

  rules[name] = (amount, produced)

def has_only_ORE(arr):
  for name, _ in arr:
    if name != 'ORE':
      return False
  return True

def fuel_to_minimum_ores(n):
  global rules
  surplus = collections.defaultdict(int)
  queue = collections.deque()
  queue.append(('FUEL',n))

  while not has_only_ORE(queue):
    name, amount = queue.popleft()  # amount is how much we NEED
    if name == 'ORE':
      queue.append((name,amount))
      continue

    produced, reactants = rules[name]  # produced is amount we get from the reaction
    if amount % produced == 0:
      num_reactions = amount // produced # no excess produced
    else:
      num_reactions = math.ceil(amount / produced)
      excess = num_reactions * produced - amount
      surplus[name] += excess

    while surplus[name] >= produced: # use up excess by removing reactions required
      num_reactions -= 1
      surplus[name] -= produced

    for reactant_name, reactant_amount in reactants:
      queue.append((reactant_name, reactant_amount * num_reactions))

  total_ores = 0
  for _,v in queue:
    total_ores += v
  return total_ores

print(fuel_to_minimum_ores(1)) # PART 1 

# binary search for x fuel 
# such that it requires minimum of 1 trillion ores
target = 1000000000000
lo, hi = target // fuel_to_minimum_ores(1), 1000000000000
while lo < hi:
  mid = lo + (hi - lo) // 2
  if fuel_to_minimum_ores(mid) < target:
    lo = mid + 1
  else:
    hi = mid

print(lo - 1) # PART 2