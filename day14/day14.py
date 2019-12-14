import collections
import math
reactions =open('input.txt', 'r').read().split('\n')
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

queue = collections.deque()
_, elements = rules['FUEL']
for e in elements:
  queue.append(e)

ore_maker = set()
ore_maker.add('KRSK')
ore_maker.add('TKMGN')
ore_maker.add('WCWLK')

def ore_check(arr):
  global ore_maker
  for name, _ in arr:
    if name not in ore_maker:
      return False
  return True



while not ore_check(queue):
  name, amount = queue.popleft()
  if name in ore_maker:
    continue

  produced, reactants = rules[name]
  if amount % produced == 0:
    num_reactions = amount // produced
  else:
    num_reactions = math.ceil(amount / produced)

  for reactant_name, reactant_amount in reactants:
    queue.append((reactant_name, reactant_amount * num_reactions))

print(queue)