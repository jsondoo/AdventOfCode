from typing import Dict, Tuple
# import time
# start_time = time.time()

with open('input.txt', 'r') as file:
    path1, path2 = file.read().split('\n')

dr = {'U': 1, 'D': -1, 'L': 0, 'R': 0}
dc = {'R': 1, 'L': -1, 'U': 0, 'D': 0}

visited: Dict[Tuple[int,int], int]
visited = {} # maps coordinates to steps taken to get there

r = c = length = 0

for command in path1.split(','):
    op = command[0] # def not copying leo
    steps = int(command[1:])

    for step in range(steps):
        r += dr[op]
        c += dc[op]
        length += 1
        visited[(r,c)] = length

min_distance = float('inf')
r = c = length = 0

for command in path2.split(','):
    op = command[0]
    steps = int(command[1:])

    for step in range(steps):
        r += dr[op]
        c += dc[op]
        length += 1

        if (r,c) in visited:
            min_distance = min(min_distance, length + visited[(r,c)])
            print(min_distance)

# print("--- %.6f seconds ---" % (time.time() - start_time))

# > time python3 day03.py 
# 0.220s