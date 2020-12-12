f = open('./d5.txt', 'r')
rows = f.read().split()

max_seat_id = 0

all_seats = list()

for partition in rows:
	r, c = None, None

	# 7 characters
	row_front = 0
	row_end = 127
	chunk = 64

	for ch in partition[:7]:
		if ch == 'F':
			row_end -= chunk
		elif ch == 'B':
			row_front += chunk

		# smaller chunk
		chunk = chunk // 2

	r = row_front

	# figure out c now
	col_front = 0
	col_end = 7
	chunk = 4
	for ch in partition[7:]:
		if ch == 'R':
			col_front += chunk
		elif ch == 'L':
			col_end -= chunk
		chunk = chunk // 2

	c = col_front
	
	seat_id = r*8 + c
	max_seat_id = max(max_seat_id, seat_id)
	all_seats.append(seat_id)

print(max_seat_id)

all_seats.sort()

for i in range(1,len(all_seats)):
	if all_seats[i] - all_seats[i-1] == 2:
		# Part 2 answer
		print(all_seats[i] - 1)
