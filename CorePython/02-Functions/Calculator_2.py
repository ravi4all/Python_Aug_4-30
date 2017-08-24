def calculator():
    pass

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

    todo = {
        '1' : calculator,
        '2' : calculator,
        '3' : calculator,
        '4' : calculator,
        'q' : quit
    }


    user_choice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    print(todo.get(user_choice)())
