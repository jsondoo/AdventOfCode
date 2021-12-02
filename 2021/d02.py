with open('./input.txt','r') as f:
  lines = list(f.readlines())

h = 0 
d = 0
a = 0

for line in lines:
  inst, amount = line.split()
  amount = int(amount)
  if inst == "forward":
    h += amount
    d += a * amount
  elif inst == "up":
    a -= amount
  elif inst == "down":
    a += amount

print(h * d)