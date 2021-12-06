from collections import defaultdict

file_name = './example.txt' if False else './input.txt'
with open(file_name,'r') as f:
  lines = [x for x in list(f.readlines())]

fish = [int(x) for x in lines[0].split(",")]

def part1():
  for _ in range(80):
    new_fish = 0
    for i in range(len(fish)):
      if fish[i] == 0:
        fish[i] = 6
        new_fish += 1
      else:
        fish[i] -= 1


    # add new fish
    for _ in range(new_fish):
      fish.append(8)
    

  return len(fish)

def part2():
  # timer from 0-8
  counts = defaultdict(int)

  for i in range(len(fish)):
    counts[fish[i]] += 1

  for day in range(256):
    new_counts = defaultdict(int)
    for k, v in counts.items():
      if k == 0:
        new_counts[6] += v
        new_counts[8] += v
      else:
        new_counts[k-1] += v
    counts = new_counts

  total = 0
  for k, v in counts.items():
    total += v    
  return total

if __name__ == '__main__':
  # print(part1())
  print(part2())