userList = []
users = {}
def create():
    userName = input("Enter user name : ")
    userNum = int(input("Enter user num : "))

    users['Name'] = userName
    users['Number'] = userNum

    userList.append(users)

    print("User added Successfully....")


def read():
    for user in userList:
        print(user)

def update():
    pass

def delete():
    pass

def search():
    pass

def sort():
    pass

def save():
    pass

def load():
    pass
