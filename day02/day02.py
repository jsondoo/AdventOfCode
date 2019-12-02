with open('input.txt', 'r') as file:
    data = file.read().split(',')

data = list(map(int, data))

def intcode(arr, noun, verb):
	pos = 0
	arr[1] = noun
	arr[2] = verb
	while arr[pos] != 99:
		if arr[pos] == 1:
			val = arr[arr[pos+1]] + arr[arr[pos+2]]
			arr[arr[pos+3]] = val
		elif arr[pos] == 2:
			val = arr[arr[pos+1]] * arr[arr[pos+2]]
			arr[arr[pos+3]] = val
		else:
			print("shouldn't be here")
		pos += 4

	return arr[0]

# PART 1
print("PART 1")
print(intcode(data.copy(), 12, 2))

# PART 2
target = 19690720

for noun in range(100):
	for verb in range(100):
		if intcode(data.copy(), noun, verb) == target:
			print("PART 2")
			print(100*noun + verb)



