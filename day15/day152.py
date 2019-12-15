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

def dfs(path, prev, mac, coords):
	global grid, visited
	if prev != 'S':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([1])
		mac_n.output = []
		p = path.copy()
		if res == 0:
			pass
		elif res == 2:
			p.append('N')
			print(path)
			print(len(p))
			return
		else:
			p.append('N')
			dfs(p,'N',mac_n,(0,0))

	if prev != 'N':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([2])
		mac_n.output = []
		p = path.copy()
		if res == 0:
			pass
		elif res == 2:
			p.append('S')
			print(path)
			print(len(p))
			return
		else:
			p.append('S')
			dfs(p,'S',mac_n,(0,0))

	if prev != 'E':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([3])
		mac_n.output = []
		p = path.copy()

		if res == 0:
			pass
		elif res == 2:
			p.append('W')
			print(path)
			print(len(p))
			return
		else:
			p = path.copy()
			p.append('W')
			dfs(p,'W',mac_n,(0,0))

	if prev != 'W':
		mac_n = copy.deepcopy(mac)
		res = mac_n.run([4])
		mac_n.output = []
		p = path.copy()

		if res == 0:
			pass
		elif res == 2:
			p.append('E')
			print(path)
			print(len(p))
			return
		else:
			p = path.copy()
			p.append('E')
			dfs(p,'E',mac_n,(0,0))

visited.add((0,0))
grid[(0,0)] = 0
dfs([], None, machine, (0,0))