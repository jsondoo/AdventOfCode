f = open('./day04.txt', 'r')
rows = f.read().replace("\n\n", "-")

passports = rows.split("-")

valid_passports = 0

for passport in passports:
	fields = passport.split()
	#           0      1      2      3     4      5      6         7
	#          byr    iyr    eyr    hgt   hcl    ecl     pid     cid (optional)
	checks = [0] * 7
	data = [0] * 7
	for field in fields:
		code = field[:3]
		value = field[4:]


		if code == "byr":
			checks[0] = 1
			if 1920 <= int(value) <= 2002:
				data[0] = 1

		if code == "iyr":
			checks[1] = 1
			if 2010 <= int(value) <= 2020:
				data[1] = 1

		if code == "eyr":
			checks[2] = 1
			if 2020 <= int(value) <= 2030:
				data[2] = 1

		if code == "hgt":
			checks[3] = 1
			units = value[-2:]

			if value[:-2]:
				number = int(value[:-2])

				if units == "cm" and 150 <= number <= 193:
					data[3] = 1
				if units == "in" and 59 <= number <= 76:
					data[3] = 1

		if code == "hcl":
			checks[4] = 1

			if value[0] == "#" and value[1:].isalnum():
				data[4] = 1

		if code == "ecl":
			checks[5] = 1

			if value in ("amb","blu","brn","gry","grn","hzl","oth"):
				data[5] = 1 

		if code == "pid":
			checks[6] = 1

			if len(value) == 9 and value.isdecimal():
				# do i need to check all number?
				data[6] = 1

		print(data)

	if sum(checks) == 7 and sum(data) == 7:
		valid_passports += 1

print(valid_passports)



