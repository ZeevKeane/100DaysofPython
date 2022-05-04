#print exercise:
print('''Day 1 - Python Print Function
The function is declared like this:
print('what to print')''')

print("\n")
#debugging exercise:
#Fix the code below 👇
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print("\n")
#input function exercise:
user_name = input("What is your name?")
print(len(user_name))

print("\n")
#variables exercise:
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
a_holder = a
a = b
b = a_holder



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#Band Name Generator Project:
#1. Create a greeting for your program.
print("Welcome to the Awesome Band Name Generator")
#2. Ask the user for the city that they grew up in.
city_name = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city_name + " " + pet_name)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
