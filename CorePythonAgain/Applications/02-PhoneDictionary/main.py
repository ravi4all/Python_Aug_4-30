# from . import businessLogic as bl
import businessLogic as bl

def main():

    mainLoop = True
    while mainLoop:

        print("""
        1. Create
        2. Read
        3. Update
        4. Delete
        5. Search
        6. Sort
        7. Save
        8. Load
        9. Quit
        """)

        todo = {
            "1" : bl.create,
            "2" : bl.read,
            "3" : bl.update,
            "4" : bl.delete,
            "5" : bl.search,
            "6" : bl.sort,
            "7" : bl.save,
            "8" : bl.load,
            "9" : quit
        }

        user_ch = input("Enter your choice : ")

        todo.get(user_ch)()

if __name__ == '__main__':
    main()
