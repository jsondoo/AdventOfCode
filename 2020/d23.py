input_string = "952316487"
num_moves = 10000000

# PART 1 using circular linked list
class Cup:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def print(self):
    print(val)

class CircularCups:
  def __init__(self):
    self.curr = None
    self.val_to_cup = {}
    self.tail = None

  def push(self, val):
    cup = Cup(val)
    self.val_to_cup[val] = cup
    if self.curr is None:
      self.curr = cup
      self.curr.next = self.curr
      self.tail = self.curr
    else:
      self.tail.next = cup
      cup.next = self.curr
      self.tail = cup

  def print(self):
    temp = self.curr
    if temp is not None:
      formatted_string = str(temp.val)
      while temp.next != self.curr:
        formatted_string += " -> " + str(temp.next.val)
        temp = temp.next
      print(formatted_string)
    

cups = CircularCups()
for ch in input_string:
  cups.push(int(ch))

for i in range(10, 1000000+1):
  cups.push(i)

for move in range(num_moves):
  if move % 1000000 == 0:
    print(move)
  # start from current cup 
  current_cup = cups.curr

  # get the value of the next three cups
  three_cups_values = set()
  temp = current_cup.next
  for i in range(3):
    three_cups_values.add(temp.val)
    temp = temp.next

  # temporarily remove the next three cups
  three_cups = current_cup.next
  current_cup.next = current_cup.next.next.next.next

  # find the label
  next_cup_val = current_cup.val - 1

  while next_cup_val == 0 or next_cup_val in three_cups_values:
    next_cup_val -= 1
    if next_cup_val <= 0:
      next_cup_val = 1000000

  # insert at label
  label_cup = cups.val_to_cup[next_cup_val]
  label_cup_next = label_cup.next
  label_cup.next = three_cups
  three_cups.next.next.next = label_cup_next

  # update new current cup
  cups.curr = cups.curr.next


cup_1 = cups.val_to_cup[1]
# temp = cup_1.next
# part_1 = ""
# while temp.val != 1:
#   part_1 += str(temp.val)
#   temp = temp.next
# print(part_1)

part_2 = cup_1.next.val * cup_1.next.next.val
print(part_2)
