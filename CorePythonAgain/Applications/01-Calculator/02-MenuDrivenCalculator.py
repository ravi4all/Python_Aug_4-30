def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x/y

def errHandler(x,y):
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
            "1" : add,
            "2" : sub,
            "3" : mul,
            "4" : div,
            "5" : quit
        }

        calc = todo.get(user_choice, errHandler)(num_1, num_2)
        print(calc)

main()
