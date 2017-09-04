import random

a = ['Stone', 'Paper', 'Scissor']
counter = 0
game = True
while game:

    cpu_choice = random.choice(a)

    user_input = input("Enter your choice : ")

    print("CPU -",cpu_choice)

    if cpu_choice == user_input:
        print("Match Tie")
    elif cpu_choice == "Stone" and user_input == "Paper":
        print("User Win")
        counter += 1
        print("Counter",counter)
    elif cpu_choice == "Paper" and user_input == "Stone":
        print("CPU Win")
        counter -= 1
        print("Counter",counter)
    elif cpu_choice == "Scissor" and user_input == "Stone":
        print("User Win")
        counter += 1
        print("Counter",counter)
    elif cpu_choice == "Stone" and user_input == "Scissor":
        print("CPU Win")
        counter -= 1
        print("Counter",counter)
    elif cpu_choice == "Paper" and user_input == "Scissor":
        print("User Win")
        counter += 1
        print("Counter",counter)
    elif cpu_choice == "Scissor" and user_input == "Paper":
        print("CPU Win")
        counter -= 1
        print("Counter",counter)
    else:
        print("Wrong Choice")
        game = False
