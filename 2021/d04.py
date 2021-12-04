with open('./input.txt','r') as f:
  lines = [seen for seen in list(f.readlines())]

numbers = [int(seen) for seen in lines[0].split(",")]

def has_bingo(board):
  bingo = True
  for r in range(5):
    for c in range(5):
      if board[r][c] != "y":
        bingo = False

    if bingo:
      return board
    bingo = True
    
  for c in range(5):
    for r in range(5):
      if board[r][c] != "y":
        bingo = False
    
    if bingo:
      return board
    bingo = True

  return None


def has_completed_board(boards):
  for board in boards:
    if (winner := has_bingo(board)) is not None:
      return winner
  return None

def mark_number(num, boards):
  for board in boards:
    for r in range(5):
      for c in range(5):
        if board[r][c] == num:
          board[r][c] = "y"
  return

def part1():
  boards = []

  for i in range(2, len(lines), 6):
    board = []
    for j in range(0,5):
      board.append([int(seen) for seen in lines[i+j].split()])
    boards.append(board)
  

  for num in numbers:
    mark_number(num, boards)
    if has_completed_board(boards) is not None:
      winner = has_completed_board(boards)
      last_num = num
      break

  unmarked = 0
  for r in range(5):
    for c in range(5):
      if winner[r][c] != "y":
        unmarked += winner[r][c]

  return unmarked * last_num

seen = set([])
last_board = None
def has_completed_boards(boards):
  for idx, board in enumerate(boards):
    if idx not in seen:
      if has_bingo(board) is not None:
        seen.add(idx)
        if len(boards) == len(seen):
          return board
  return None

def part2():
  boards = []
  for i in range(2, len(lines), 6):
    board = []
    for j in range(0,5):
      board.append([int(seen) for seen in lines[i+j].split()])
    boards.append(board)
  
  for num in numbers:
    mark_number(num, boards)
    if (last_board := has_completed_boards(boards)) is not None:
      last_num = num
      winner = last_board
      break

  unmarked = 0
  for r in range(5):
    for c in range(5):
      if winner[r][c] != "y":
        unmarked += winner[r][c]

  return unmarked * last_num

if __name__ == '__main__':
  print(part1())
  print(part2())