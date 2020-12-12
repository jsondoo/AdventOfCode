from IntcodeComputer import IntcodeComputer
import copy
import sys

f = open("input.txt", "r")
def createMem(str): return list(map(int, str.strip("\n").split(",")))
machine = IntcodeComputer(createMem(f.readline()))

# PART 1
# curr = ""
# while not machine.halted:
# 	v = machine.run()
# 	# print(v)
# 	if v is not None:
# 		curr += chr(v)

# print(curr)
# rows = curr.split("\n")
# grid = list(filter(None,rows))

# intersections = []
# for r in range(len(grid)):
# 	for c in range(len(grid[0])):
# 		if grid[r][c] == '#' and 1 <= r < len(grid) - 1 and 1 <= c < len(grid[0]) - 1:
# 			if grid[r-1][c] == '#' and grid[r+1][c] == '#' and grid[r][c-1] == '#' and grid[r][c+1] == '#':
# 				intersections.append((r,c))

# alignment = 0
# for r,c in intersections:
# 	alignment += r*c
# print(f'Part 1: {alignment}')


def string_to_ascii_list(s):
	res = []
	for ch in s:
		res.append(ord(ch))
	res.append(10)
	return res

routine = "A,B,A,C,A,B,A,C,B,C"
funcA = "R,4,L,12,L,8,R,4"
funcB = "L,8,R,10,R,10,R,6"
funcC = "R,4,R,10,L,12"

routine = string_to_ascii_list(routine)
funcA = string_to_ascii_list(funcA)
funcB = string_to_ascii_list(funcB)
funcC = string_to_ascii_list(funcC)
no = string_to_ascii_list("n")
inpoot = routine + funcA + funcB + funcC + no
print(inpoot)
# input mem[0] from 1 -> 2 make robot woke

while not machine.halted:
	v = machine.run(inpoot)
	print(v)



