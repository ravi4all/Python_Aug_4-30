file = open('ques.txt')

correct_ans = "modi"

# q = file.readline()

qs = file.readlines()

for i in qs:
    print(i, end='')
    ans = input(">> ")
    if ans == correct_ans:
        print("Correct Ans...")
    else:
        print("Wrong Ans...")


# print(q)
# print(qs)
