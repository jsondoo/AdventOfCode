f = open('./day03.txt', 'r')
rows = list(f.readlines())
rows = list(map(lambda x: x.replace("\n",""), rows))

# coordinates
r1 = 1
c1 = 3

for r,c in ((1,3),(1,1),(1,5),(1,7),(2,1)):
	print(r,c)
	r1 = r
	c1 = c

	trees = 0
	while r1 < len(rows):
		if rows[r1][c1] == '#':
			trees += 1

		r1 = r1 + r
		c1 = (c1 + c) % len(rows[0])

	print(trees)

