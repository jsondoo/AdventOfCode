from collections import defaultdict
f = open('./d6.txt', 'r')
rows = f.read().replace("\n\n","-").split("-")

num_questions = 0

for row in rows:
	num_groups = row.count("\n") + 1
	r = row.replace("\n","")
	seen = defaultdict(int)
	for ch in r:
		seen[ch] = seen[ch] + 1


	for k,d in seen.items():
		if d == num_groups:
			num_questions += 1


print(num_questions)
# 10:17pm

