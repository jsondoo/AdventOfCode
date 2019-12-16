thing = open('input.txt', 'r').read()
offset = int(thing[:7])
input_list = [int(x) for x in list(thing)]

def get_pattern2(pos, n):
  return [0]*pos + [1]*(n-pos)

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
print(inp[:8]) # PART 2