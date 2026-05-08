# ============================================================
# Python Final Project 2026
# Name: 
# Date: 
# Project Title: 
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""



# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome!")
print("This is my calc.")


# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.
operation=input("What operation will you be using? (Multiplication, Division, Subtraction, Addition, Exponentation)")
number1=float(input("What is the first number in the problem?"))
number2=float(input("What is the second number in the problem?"))
#Asks the user for the problem
# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))



# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.
if operation=="Addition":
    Answer=round(number1+number2)
elif operation=="Subtraction":
    Answer=round(number1-number2)
elif operation=="Division":
    Answer=round(number1/number2)
elif operation=="Multiplication":
    Answer=round(number1*number2)
elif operation=="Exponentation":
    Answer=round(number1**number2)
else: print("Please input a valid operation.")
# Checks all of the valid operations and will solve when one of the operations is true
# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")



# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

print(f"The solution is: {Answer}. Thanks for using my program!")
#Outputs the solution to the problem