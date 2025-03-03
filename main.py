import random
from game_data import data
from art import logo, vs

compare_A = random.choice(data)
against_B = random.choice(data)
score = 1
game_over = True

compare = f"Compare A: {compare_A['name']}, {compare_A['description']}, {compare_A['country']}."
against = f"Against B: {against_B['name']}, {against_B['description']}, {against_B['country']}."

while game_over :
  print(logo)
  print(compare)
  print(vs)
  print(against)
  question = input("Who has more followers? Type 'A' or 'B':   ").upper()
  
  if question=="A" :
    compare_A_count = compare_A['follower_count']
    against_B_count = against_B['follower_count']
    
    if compare_A_count > against_B_count :
      print(f"You're right! Current score: {score}.")
      score += 1
    else :
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}.")
      game_over = False
  
  else :
    compare_A_count = compare_A['follower_count']
    against_B_count = against_B['follower_count']
    
    if compare_A_count > against_B_count :
      print(f"You're right! Current score: {score}.")
      score += 1
    else :
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}.")
      game_over = False

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Eran2001/python_game.git
git push -u origin main