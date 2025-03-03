import random
from game_data import data
from art import logo, vs

compare_A = random.choice(data)
against_B = random.choice(data)
game_over = True

compare = f"Compare A: {compare_A['name']}, {compare_A['description']}, {compare_A['country']}."
against = f"Against B: {against_B['name']}, {against_B['description']}, {against_B['country']}."

def game() :
  score = 0
  compare_a_count = compare_A['follower_count']
  against_b_count = against_B['follower_count']
  
  if compare_a_count > against_b_count :
    print(f"You're right! Current score: {score}.")
    score += 1
  else :
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")
    return False

while game_over :
  print(logo)
  print(compare)
  print(vs)
  print(against)
  question = input("Who has more followers? Type 'A' or 'B':   ").upper()
  
  if question=="A" :
    game()
  
  else :
    game()
    
    
