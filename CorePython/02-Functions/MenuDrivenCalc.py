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

    todo = {
        '1' : add,
        '2' : sub,
        '3' : div,
        '4' : mul,
        'q' : quit
    }


    user_choice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    print(todo.get(user_choice)())
