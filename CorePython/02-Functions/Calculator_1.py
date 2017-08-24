def add():
    return num_1 + num_2

def sub():
    return num_1 - num_2

def mul():
    return num_1 * num_2

def div():
    return num_1/num_2

main = True

while main:

    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    5. Square
    6. Sqrt
    7. Quit
    """)

    user_choice = int(input("Enter your choice : "))

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    if user_choice == 1:
        print(add())
    elif user_choice == 2:
        print(sub())
    elif user_choice == 3:
        print(div())
    elif user_choice == 4:
        print(mul())
    else:
        print("Wrong Choice")
        main = False
