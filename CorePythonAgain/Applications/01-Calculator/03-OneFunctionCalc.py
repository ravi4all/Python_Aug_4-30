def calculator(ch,x,y):
    if ch == "1":
        return x + y
    elif ch == "2":
        return x - y
    elif ch == "3":
        return x * y
    elif ch == "4":
        return x/y
    else:
        print("Wrong Choice")


def main():
    while True:

        print("""
1. Add
2. Sub
3. Mul
4. Div
5. Quit
        """)

        user_choice = input("Enter your choice : ")

        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))

        todo = {
            "1" : calculator,
            "2" : calculator,
            "3" : calculator,
            "4" : calculator,
        }

        calc = todo.get(user_choice)(user_choice,num_1, num_2)
        print(calc)

main()
