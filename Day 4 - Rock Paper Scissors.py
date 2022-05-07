import random

# Exercise 1: Heads or Tails
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0,1)
if random_side == 1:
	print("Heads")
else: 
	print("Tails")




# Exercise 2: Banker Roulette - Who will pay the bill?
#thinking of the index of a list as the offset from the start of the list.
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_index = random.randint(0,len(names)-1)

this could also be done by using .choice in random:
print(random.choice(names) + " is going to buy the meal today!")
print(names[random_index] + " is going to buy the meal today!")


# Exercise 3: Treasure map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position[0])
row = int(position[1])

map[row-1][column-1] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# Day 4 Project: Rock Paper Scissors
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
possibilities = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

computer_choice = random.randint(0,3)

print(f"You chose: \n{possibilities[player_choice]}")

print(f"Computer chose: \n{possibilities[computer_choice]}")

#worse way of writing this:
# if player_choice == 0:
# 	if computer_choice == 1:
# 		print("You lose.")
# 	elif computer_choice == 2:
# 		print("You win.")
# elif player_choice == 1:
# 	if computer_choice == 0:
# 		print("You win.")
# 	elif computer_choice == 2:
# 		print("You lose.")
# elif player_choice == 2:
# 	if computer_choice == 0:
# 		print("You lose.")
# 	elif computer_choice == 1:
# 		print("You win.")

#better way of writing this:
if player_choice >= 3 or player_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif player_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and player_choice == 2:
  print("You lose")
elif computer_choice > player_choice:
  print("You lose")
elif player_choice > computer_choice:
  print("You win!")
elif computer_choice == player_choice:
  print("It's a draw")
