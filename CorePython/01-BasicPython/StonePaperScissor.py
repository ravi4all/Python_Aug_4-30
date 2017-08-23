import random
import time

cpu_choice = ['stone', 'paper', 'scissor']

cpu_ch = random.choice(cpu_choice)


user_choice = input("Enter your choice : ")

print("Cpu choice is",cpu_ch)

time.sleep(2)

if user_choice == cpu_ch:
    print("Match Tie")
elif user_choice == 'scissor' and cpu_ch == 'paper':
    print("You win")
elif user_choice == 'stone' and cpu_ch == 'scissor':
    print("You win")
elif user_choice == 'paper' and cpu_ch == 'stone':
    print("You win")
elif user_choice == 'scissor' and cpu_ch == 'stone':
    print("CPU win")
elif user_choice == 'stone' and cpu_ch == 'paper':
    print("CPU win")
elif user_choice == 'paper' and cpu_ch == 'scissor':
    print("CPU win")
else:
    print("Wrong Choice")
