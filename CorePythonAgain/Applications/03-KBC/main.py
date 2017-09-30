import time

options = [['Modi','Arvind','Yogi','Lalu'],
           ['Mumbai', 'Delhi', 'Lucknow', 'Goa'],
           ['Global Service Tax', 'Goods and Simple Tax', 'Goods and Services Tax', 'General Service Tax'],
           ['1000','200','50','400']]

money = [1000,5000,10000,50000]

answers = ['Modi','Delhi','Goods and Simple Tax',200,'Delhi']

with open('ques.txt') as file:
    qs = file.readlines()
    while True:

        for i in range(len(qs)):
            print(qs[i])
            print(options[i])

            ans = input("Enter answer : ")

            if ans == answers[i]:
                time.sleep(3)
                print("Corrent Answer...")
                print("You won",money[i])
            else:
                time.sleep(3)
                print("Wrong Answer...")
                print("Total Amount",money[i-1])
                break
        break

print("Game Over...")
