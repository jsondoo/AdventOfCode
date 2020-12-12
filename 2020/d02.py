f = open('./day02.txt', 'r')
pw = list(f.readlines())

count = 0
for p in pw:
	a = p.split()
	least, most = a[0].replace("-", " ").split(" ")
	least, most = int(least), int(most)
	ch = a[1].replace(":","")

	password = a[2].replace("\n","")

	# least and most are indexes

	count_ch = 0 # need exactly one character
	if password[least-1] == ch:
		count_ch += 1
	if password[most-1] == ch:
		count_ch += 1

	if count_ch == 1:
		count += 1

	print(least ,most, ch, password)

print(count)