print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if road == "left":
  swim1 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
  if swim1 == "wait":
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
    if door == "red":
      print("You are burned by fire. Game over.")
    elif door == "yellow":
      print("You found the treasure. You win!")
    elif door == "blue":
      print("You are eaten by beasts. Game over.")
    else:
      print("Game over.")
  else:
    print("You are attacked by a trout. Game over.")  
else:
  print("You fall into the hole. Game over.")