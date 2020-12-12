from IntcodeComputer import IntcodeComputer
import copy
import collections

f = open("input.txt", "r")
def createMem(str): return list(map(int, str.strip("\n").split(",")))
machine = IntcodeComputer(createMem(f.readline()))

def print_maze(arr):
	for r in arr:
		print(''.join([str(x) for x in r]).replace('1',' ').replace('0','#').replace('2','O'))

def bfs(machine, coords):
	visited = set() # these are nodes that were processed already
	maze = collections.defaultdict(int) # map coordinate to its block (0,1,2)
	queue = collections.deque() # list of (coords, intcode computer)
	direction = {1: (0,-1), 2: (0,1), 3: (-1,0), 4: (1,0)}

	queue.append((coords, copy.deepcopy(machine)))
	maze[coords] = 1

	while queue:
		coords, computer = queue.popleft()

		if coords in visited:
			continue

		visited.add(coords)
		x,y = coords

		for d in range(1,5):
			computer_copy = copy.deepcopy(computer)
			res = computer_copy.run([d])
			computer_copy.output = []
			nx = x + direction[d][0]
			ny = y + direction[d][1]
			maze[(nx,ny)] = res
			if res != 0:
				queue.append(((nx,ny), computer_copy))
			else:
				visited.add((nx,ny))

	return maze

def fill_maze(maze):
	# find oxygen
	ox, oy = None, None
	for r in range(len(maze)):
		for c in range(len(maze[0])):
			if maze[r][c] == 2:
				ox, oy = c, r
				break

	time = 0
	visited = set()
	queue = collections.deque([(ox,oy,0)])
	while queue:
		x,y,t = queue.popleft()
		print(x,y,t)
		time = t

		if (x,y) not in visited:
			visited.add((x,y))
			for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
				if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] == 1:
					queue.append((nx,ny,t+1))

	return time - 1




init_coords = (21,21)
maze = bfs(machine, init_coords)

# turn dictinary into 2d grid
max_x = max(maze.keys(),key=lambda k: k[0])[0]
max_y = max(maze.keys(),key=lambda k: k[1])[1]

grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
for y in range(max_y + 1):
	for x in range(max_x + 1):
		grid[y][x] = maze[(x,y)]

print_maze(grid)
print(fill_maze(grid))


