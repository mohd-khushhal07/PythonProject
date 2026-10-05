# Welcome Message Genrator
# Step1: Ask for user Details

name = input("Whats your name? ")
age = int(input("How old are you? "))
color = input("What is your favorite color? ")
hobby = input('Whats your favorite hobby? ')

#step 2: Genrate a personalized welcome massage

print("\n-- Wlcome Message ---\n")
print(f"Hello , {name}! 👋")
print(f"You are {age} years old and {color} is a beautiful color!")
print("Welcome to the world of Python Programming. ")
print(f"your favorite hobby is {hobby}")