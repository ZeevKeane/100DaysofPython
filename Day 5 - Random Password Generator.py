import random

#Exercise 1: Average Height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sumof_heights = 0
numberof_students = 0
for height in student_heights:
	sumof_heights += height
	numberof_students += 1

average_height = round(sumof_heights/numberof_students)

print(f"{average_height}")


#Exercise 2: High Score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
high_score = 0
for score in student_scores:
	if score > high_score:
		high_score = score
	else:
		continue

print(f"The highest score in the class is: {high_score}")



# #Exercise 3: Adding Even Numbers
# #Write your code below this row 👇
sumof_even_numbers = 0
for n in range(1, 101):
	if n % 2 == 0:
		sumof_even_numbers += n
	else:
		continue


# #OR

# # for n in range(2,101,2):
# # 	sumof_even_numbers += n
	
print(sumof_even_numbers)


#Exercise 4: FizzBuzz
#Write your code below this row 👇
for n in range(1,101):
	if n % 3 == 0 and n % 5 == 0:
		print("FizzBuzz")
	elif n % 3 == 0:
		print("Fizz")
	elif n % 5 == 0:
		print("Buzz")
	else:
		print(n)

#Final Project: Password Generator
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# general:
intial_seed = random.seed()
length_of_letters = len(letters)
length_of_numbers = len(numbers)
length_of_symbols = len(symbols)

# building the intial randomzied selections:
letters_randomized_selection = []
numbers_randomized_selection = []
symbols_randomized_selection = []


for letter in range(0, nr_letters):
	letters_randomized_selection.append(letters[random.randint(0, length_of_letters - 1)])
	
for number in range(0, nr_numbers):
	numbers_randomized_selection.append(numbers[random.randint(0, length_of_numbers - 1)])
	
for symbol in range(0, nr_symbols):
	symbols_randomized_selection.append(symbols[random.randint(0, length_of_symbols - 1)])

intial_randomized_selection = letters_randomized_selection + numbers_randomized_selection + symbols_randomized_selection
length_of_intial_randomization = len(intial_randomized_selection)
# print(intial_randomized_selection)
# asembling the password - randomized again:

password = ""
indices_used = []
for random_n in intial_randomized_selection:
	
	while True:
		random_index = random.randint(0, length_of_intial_randomization - 1)
		if random_index not in indices_used:
			break

	indices_used.append(random_index)
	password += intial_randomized_selection[random_index]

print(password)
