# name = input("Enter your name: ")
#print(f"Hello , {name} ") 

#num1 = input("Enter a number: ")
#num1 = int(num1)
#print(f"Number doubled: {num1 * 2}")

#num1 = int(input("Enter first Number: "))
#num2 = int(input("Enter Second number: "))
#result = num1 + num2

#print(f"The sum of {num1} and {num2} is {result}")


# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))

# print(f"Addition: {a+b}")
# print(f"Subtraction : {a-b}")
# print(f"Multiplication: {a*b}")
# print(f"Division : {a/b}")
# print(f"Floor Division : {a//b}")
# print(f"Modulus : {a%b}")
# print(f"Exponentiation : {a**b}")

#simple Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1*num2
divition = num1/num2 if num2 != 0 else "Cannot divide by Zero"

print("\n ----Calculator Results ---")

print(f"\nAddition: {num1} + {num2} = {addition}")

print(f"Subtraction: {num1} - {num2} ={subtraction}")

print(f"Multiplication:{num1} * {num2} ={multiplication}")

print(f"Division:{num1}/{num2} = {divition}\n")
