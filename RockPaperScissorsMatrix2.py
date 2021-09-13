rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game = [rock, paper, scissors]
print(game[choice])
game1 = random.randint(0,2)
game2 = game[game1]
print(f"Computer chose\n {game2}") 


winning1 = [["Draw!", "You lose!", "You win!"],  ["You win!", "Draw!", "You lose!"], ["You lose!", "You win!", "Draw!"]]
print(winning1[choice][game1])









# if choice == 0:
#   if game1 == 0:
#     print("Draw!")
#   elif game1 == 1:
#     print("You lose!")
#   else:
#     print("You win!")
# elif choice == 1:
#   if game1 == 0:
#     print("You win!")
#   elif game1 == 1:
#     print("Draw!")
#   elif game1 == 2:
#     print("You lose!")
# else:
#   if game1 == 0:
#     print("You lose!")
#   elif game1 == 1:
#     print("You win!")
#   else:
#     print("Draw!")