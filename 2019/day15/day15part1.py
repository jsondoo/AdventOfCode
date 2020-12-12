from IntcodeComputer import IntcodeComputer
import copy
import sys
sys.setrecursionlimit(1000000000)
import collections

f = open("input.txt", "r")
def createMem(str): return list(map(int, str.strip("\n").split(",")))
machine = IntcodeComputer(createMem(f.readline()))


grid = collections.defaultdict(int)
visited = set()
oxygen = None
longest = float('-inf')
def dfs(path, prev, mac, coords):
	global grid, visited, oxygen, longest
	x,y = coords

	if prev != 'S':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([1])
		mac_n.output = []
		p = path.copy()
		if res == 0:
			visited.add((x,y-1))
			grid[(x,y-1)] = 0
			longest = max(len(path), longest)
			pass
		elif res == 2:
			p.append('N')
			print(path)
			print(len(p))
			if (x,y-1) not in visited:
			visited.add((x,y-1))
			grid[(x,y-1)] = 2
			oxygen = (x,y-1)
			return 
		else:
			p.append('N')
			visited.add((x,y-1))
			grid[(x,y-1)] = 1
			dfs(p,'N',mac_n,(x,y-1))

	if prev != 'N':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([2])
		mac_n.output = []
		p = path.copy()
		if res == 0:
			visited.add((x,y+1))
			grid[(x,y+1)] = 0
			longest = max(len(path), longest)
			pass
		elif res == 2:
			p.append('S')
			print(path)
			print(len(p))
			visited.add((x,y+1))
			grid[(x,y+1)] = 2
			oxygen = (x,y+1)
			return 
		else:
			p.append('S')
			visited.add((x,y+1))
			grid[(x,y+1)] = 1
			dfs(p,'S',mac_n,(x,y+1))

	if prev != 'E':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([3])
		mac_n.output = []
		p = path.copy()

		if res == 0:
			visited.add((x-1,y))
			grid[(x-1,y)] = 0
			longest = max(len(path), longest)
			pass
		elif res == 2:
			p.append('W')
			print(path)
			print(len(p))
			visited.add((x-1,y))
			grid[(x-1,y)] = 0
			oxygen = (x-1,y)
			return 
		else:
			p = path.copy()
			p.append('W')
			visited.add((x-1,y))
			grid[(x-1,y)] = 0
			dfs(p,'W',mac_n,(x-1,y))

	if prev != 'W':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([4])
		mac_n.output = []
		p = path.copy()

		if res == 0:
			visited.add((x+1,y))
			grid[(x+1,y)] = 0
			longest = max(len(path), longest)
			pass
		elif res == 2:
			p.append('E')
			print(path)
			print(len(p))
			visited.add((x+1,y))
			grid[(x+1,y)] = 0
			oxygen = (x+1,y)
			pass
		else:
			p = path.copy()
			p.append('E')
			visited.add((x+1,y))
			grid[(x+1,y)] = 0
			dfs(p,'E',mac_n,(x+1,y))

init = (30,30)
visited.add(init)
grid[init] = 0
dfs([], None, machine, init)
print(oxygen)


max_x = float('-inf')
max_y = float('-inf')
for k,_ in grid.items():
	x1, y1 = k
	max_x = max(max_x, x1)
	max_y = max(max_y, y1)
print(max_x,max_y)

maze = [[0 for _ in range(50)] for _ in range(50)]
for x in range(50):
	for y in range(50):
		maze[y][x] = grid[(x,y)]

for m in maze:
	print(''.join([str(x) for x in m]).replace('1','@').replace('0','#').replace('0','@'))

print(longest)

