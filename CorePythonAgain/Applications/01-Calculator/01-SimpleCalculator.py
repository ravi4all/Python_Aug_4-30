def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x/y

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

        if user_choice == "1":
            print(add(num_1, num_2))
        elif user_choice == "2":
            print(sub(num_1, num_2))
        elif user_choice == "3":
            print(mul(num_1, num_2))
        elif user_choice == "4":
            print(div(num_1, num_2))
        elif user_choice == "5":
            quit()
        else:
            print("Wrong Choice")

main()
