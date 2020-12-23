from collections import defaultdict
import re

f = open('./d22.txt', 'r')
player1, player2 = f.read().split("\n\n")

player1 = [int(x) for x in player1.split("\n")[1:]]
player2 = [int(x) for x in player2.split("\n")[1:]]

assert(len(player1) == len(player2))

game_states = defaultdict(set) # game_id -> seen states
next_game_id = 0

def simulate_game(player1, player2, game_id=0):
  global next_game_id
  next_game_id += 1
  while player1 and player2:
    # check if this game state existed (if so player1 immediately wins)
    game_state = ''.join(str(v) for v in player1) + ":" + ''.join(str(v) for v in player2)
    if game_state in game_states[game_id]:
      return (0, True)

    # otherwise, save game state and continue
    game_states[game_id].add(game_state)

    p1_top, p2_top = player1.pop(0), player2.pop(0)

    # check if subgame needs to be played
    subgame = False
    if len(player1) >= p1_top and len(player2) >= p2_top:
      _, p1_winner = simulate_game(player1[:p1_top], player2[:p2_top], next_game_id)
      
      if p1_winner:
        player1.append(p1_top)
        player1.append(p2_top)
      else:
        player2.append(p2_top)
        player2.append(p1_top)

    else:
      # else continue with normal rules
      if p1_top > p2_top:
        player1.append(p1_top)
        player1.append(p2_top)
      else:
        player2.append(p2_top)
        player2.append(p1_top)

  def compute_winning_score(lst):
    total_score = 0
    multipler = 1
    for val in lst[::-1]:
      total_score += val * multipler
      multipler += 1
    return total_score

  part1 = None
  player1_won = True
  if player1:
    part1 = compute_winning_score(player1)
  else:
    player1_won = False
    part1 = compute_winning_score(player2)

  return (part1, player1_won)

print(simulate_game(player1, player2))