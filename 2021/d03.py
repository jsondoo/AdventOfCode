with open('./input.txt','r') as f:
  lines = [x for x in list(f.readlines())]


def part1():
  # construct binary strings
  gamma, epsilon = "", ""

  for i in range(12):
    zeros = 0
    ones = 0
    for line in lines:
      if line[i] == '0':
        zeros += 1
      else:
        ones += 1
    
    if zeros > ones:
      gamma += "0"
      epsilon += "1"
    else:
      gamma += "1"
      epsilon += "0"
  
  return int(gamma, 2) * int(epsilon, 2)


def part2():
  # find oxygen generator rating
  prev_lines = lines

  for i in range(12):
    new_lines = []
    zeros = 0
    ones = 0
    for line in prev_lines:
      if line[i] == '0':
        zeros += 1
      else:
        ones += 1
    
    most_common_bit = "0" if zeros > ones else "1"

    if zeros == ones:
      most_common_bit = "1"

    for line in prev_lines:
      if line[i] == most_common_bit:
        new_lines.append(line)

      prev_lines = new_lines

    if len(prev_lines) == 1:
      break

  n1 = prev_lines[0]

  # find co2 scrubber rating
  prev_lines = lines

  for i in range(12):
    new_lines = []
    zeros = 0
    ones = 0
    for line in prev_lines:
      if line[i] == '0':
        zeros += 1
      else:
        ones += 1
    
    most_common_bit = "1" if zeros > ones else "0"

    if zeros == ones:
      most_common_bit = "0"

    for line in prev_lines:
      if line[i] == most_common_bit:
        new_lines.append(line)

      prev_lines = new_lines

    if len(prev_lines) == 1:
      break
    
  n2 = prev_lines[0]

  return int(n1, 2) * int(n2, 2)


if __name__ == '__main__':
  print(part1())
  print(part2())