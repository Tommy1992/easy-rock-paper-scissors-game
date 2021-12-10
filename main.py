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

#Write your code below this line 👇
import random as rnd
# 0 = rock
# 1 = paper
# 2 = scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
npc_choice = rnd.randint(0,2)

if user_choice == 0:
  print ("You chose: ROCK\n" + rock)
  if npc_choice == 0:
    print ("Your enemy chose: ROCK\n" + rock)
    print ("It's a draw.")
  elif npc_choice == 1:
    print ("Your enemy chose: PAPER\n" + paper)
    print ("You lose.")
  elif npc_choice == 2:
    print ("Your enemy chose: SCISSORS\n" + scissors)
    print ("You win.")
elif user_choice == 1:
  print ("You chose: PAPER\n" + paper)
  if npc_choice == 0:
    print ("Your enemy chose: ROCK\n" + rock)
    print ("You win.")
  elif npc_choice == 1:
    print ("Your enemy chose: PAPER\n" + paper)
    print ("It's a draw.")
  elif npc_choice == 2:
    print ("Your enemy chose: SCISSORS\n" + scissors)
    print ("You lose.")
elif user_choice == 2:
  print ("You chose: SCISSORS\n" + scissors)
  if npc_choice == 0:
    print ("Your enemy chose: ROCK\n" + rock)
    print ("You lose.")
  elif npc_choice == 1:
    print ("Your enemy chose: PAPER\n" + paper)
    print ("It's a win.")
  elif npc_choice == 2:
    print ("Your enemy chose: SCISSORS\n" + scissors)
    print ("It's a draw.")
else: print ("Please put in 0, 1 or 2 next time... You lose.")
