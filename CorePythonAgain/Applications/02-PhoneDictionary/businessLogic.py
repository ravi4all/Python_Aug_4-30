userList = []
users = {}

def create():
    userName = input("Enter user name : ")
    userNum = int(input("Enter user num : "))

    users['Name'] = userName
    users['Number'] = userNum

    userList.append(users.copy())

    print("User added Successfully....")


def read():
    counter = 0
    for user in userList:
        counter += 1
        print(counter,user)



def update():
    user_id = int(input("Which user you want to update : "))
    print(userList[user_id-1])

    user_ch = input("What do you want to update name or number ?")
    user_ch = user_ch.lower()

    if user_ch == "name":
        updatedName = input("Enter update name : ")
        userList[user_id-1]['Name'] = updatedName
        print("User updated successfully")
    elif user_ch == "number":
        updatedNum = int(input("Enter updated number : "))
        userList[user_id-1]['Number'] = updatedNum
        print("User updated successfully")
    else:
        print("Wrong choice")



def delete():
    user_id = int(input("Which user you want to delete : "))
    print(userList[user_id-1])
    del userList[user_id-1]
    print("User deleted successfully")

def search():
    pass

def sort():
    sortedList = sorted(userList, key=lambda a:a['Name'])
    for s in sortedList:
        print(s)

def save():
    pass

def load():
    pass
