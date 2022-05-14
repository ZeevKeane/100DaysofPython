# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code

# def greet():
#     print("Hi")
#     print("Hello")
#     print("World")

# greet()

# # Functions that allow input:
# def greet_with_name(name):
#     print(f"Hello {name}")

    
# greet_with_name("Athar")


# #Write your code below this line 👇

# def paint_calc(height, width, cover):
#     number_of_cans = round(height * width / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")





# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works. 
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



# Prime Checker:
#Write your code below this line 👇
def primer(number):
    for r in range(2, number):
        if number % r == 0:
            return False
    return True
    

def prime_checker(number):
    if primer(number):
        print("It's a prime number.")
    else:
        print("It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
