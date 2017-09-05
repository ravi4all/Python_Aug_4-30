# *args and **kwargs

def emp(id, name, **address):
    print("ID is {} and Name is {}".format(id, name))
    print("Address is {}".format(address))

# emp(101, 'Ram', 'Home Address', 'Office Address', 'Office_2 Address')

addr = ['Home Address', 'Office Address', 'Office_2 Address']

addr_dict = {'address_1':"Home Address", 'address_2':'Office Address'}

# emp(102, 'Shyam', *addr)

emp(103, 'Gopal', **addr_dict)
