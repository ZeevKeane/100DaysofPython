#Exercise 1: Odd or Even
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
	print("This is an even number.")
else:
	print("This is an odd number.")

Exercise 2: BMI 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

if bmi < 18.5:
	print("Your BMI is 18, you are underweight.")
elif bmi > 18.5 and bmi < 25:
	print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi < 30:
	print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi < 35:
	print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
	print(f"Your BMI is {bmi}, you are clinically obese.")


#Exercise 3: Leap Year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("Leap year.")
		else:
			print("Not leap year.")
	else:
		print("Leap year.")
else:
	print("Not leap year.")
	

#Exercise 4: Pizza Order Pratice
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0 
if size == "S":
	bill += 15
elif size == "M":
	bill += 20
elif size == "L":
	bill += 25

if add_pepperoni == "Y":
	if size == "M" or size == "L":
		bill += 3
	else:
		bill += 2

if extra_cheese == "Y":
	bill += 1

print(f"Your final bill is: ${bill}.")

#Exercise 5: Love Calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = (name1 + name2).lower()
score1 = 0
score2 = 0

for letter in combined_name:
	if letter in "true":
		score1 += 1
	if letter in "love":
		score2 += 1
		

score = int(str(score1) + str(score2))
if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")


	
#Final Boss:
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
leftorright = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'? ").lower()
if leftorright == "left":
	swimorwait = input("You have come to a lake, There is an island in the middle. Type 'swim' or 'wait'? to wait for a boat. ").lower()
	if swimorwait == "wait":
		whichdoor = input("There are 3 doors, which door would you like to open? red, blue, yellow, mystery?").lower()
		if whichdoor == "red":
			print("Burned by fire. Game Over.")
		elif whichdoor == "blue":
			print("Eaten by beasts. Game Over.")
		elif whichdoor == "yellow":
			print("You Win!")
		else:
			print("Game Over.")
	else:
		print("Attacked by trout. Game Over.")
else:
	print("Fall into a hole. Game over.")




