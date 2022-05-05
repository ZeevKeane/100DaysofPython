# Exercise 1: Data Types:

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

# ###################################
# Write your code below this line 👇
first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])

print(first_num + second_num)


#Exercise 2: BMI Calculator:
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(int(weight/height ** 2))


#Exercise 3: Life in Weeks
# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_90 = 90- age
days = age_90 * 365
weeks = age_90 * 52
months = age_90 * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left")



#Tip calculator:
print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
result = (bill / split) * (tip / 100) + bill / split
result_rounded = round(result, 2)
final_result = "{:.2f}".format(result_rounded)
print(f"Each person should pay: ${final_result}")
