def calculator(opr,x,y):
    return eval(x+opr+y)

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

        num_1 = input("Enter first number : ")
        num_2 = input("Enter second number : ")

        todo = {
            "1" : "+",
            "2" : "-",
            "3" : "*",
            "4" : "/",
        }

        result = calculator(todo[user_choice], num_1, num_2)
        print(result)

main()
