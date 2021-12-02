with open('./input.txt','r') as f:
  lines = list(f.readlines())

num_increases = 0
prev = None
for line in lines:
  if prev is not None and int(line) > prev:
    num_increases += 1
  
  prev = int(line)

print(num_increases)

prev_window = None
num_increases = 0
for i in range(2, len(lines)):
  curr_window = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
  if prev_window is not None and curr_window > prev_window:
    num_increases += 1
  prev_window = curr_window

print(num_increases)
