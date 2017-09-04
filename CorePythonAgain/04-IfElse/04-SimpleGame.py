import random

a = ['rock', 'paper', 'scissor']

wins = ['rockscissor', 'paperrock', 'scissorpaper']

while True:

    cpu_choice = random.choice(a)

    user_choice = input("Enter your choice : ")
    print("CPU -",cpu_choice)
    if user_choice == cpu_choice:
        print("Match Tie")
    elif user_choice+cpu_choice in wins:
        print("User Win")
    else:
        print("CPU Wins")
