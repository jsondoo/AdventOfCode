import collections
thing = open('input.txt', 'r').read()
offset = int(thing[:7]) # for part 2
input_list = [int(x) for x in list(thing)]

def get_pattern(pos, n): # 1-based position, length of pattern list
  base_pattern = [0,1,0,-1]
  bn = len(base_pattern)
  pattern = []

  bi = 0
  while len(pattern) <= n :
    val = base_pattern[bi]
    pattern.extend([val] * pos)
    bi = (bi + 1) % bn

  return pattern[1:(n+1)]


def run_phase(inp):
  n = len(inp)
  out = []
  for i in range(len(inp)):
    p = get_pattern(i+1, n)

    total = 0
    for j in range(len(p)):
      total += p[j] * inp[j]
    out.append(abs(total) % 10)

  return out

num_phases = 100
inp = input_list
for i in range(num_phases):
  inp = run_phase(inp)

print(f'Part 1: {inp[:8]}') # PART 1


def run_phase2(inp):
  total = 0
  out = []
  for i in range(len(inp)-1,-1,-1):
    total += inp[i]
    out.append(abs(total) % 10)

  out.reverse()
  return out

# PART 2
inp2 = input_list * 10000
inp = inp2[offset:]
n = len(inp)

num_phases = 100
for i in range(num_phases):
  inp = run_phase2(inp)
print(f'Part 2: {inp[:8]}') # PART 2



