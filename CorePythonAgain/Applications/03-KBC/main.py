options = [['Modi','Arvind','Yogi','Lalu'],
           ['Mumbai', 'Delhi', 'Lucknow', 'Goa'],
           ['Global Service Tax', 'Goods and Simple Tax', 'Goods and Services Tax', 'General Service Tax'],
           ['1000','200','50','400']]

answers = ['Modi','Delhi','Goods and Simple Tax',200]

with open('ques.txt') as file:
    qs = file.readlines()
    while True:

        for i in range(len(qs)):
            print(qs[i])
            print(options[i])

            ans = input("Enter answer : ")

            if ans in answers:
                print("Corrent Answer...")
            else:
                print("Wrong Answer...")
