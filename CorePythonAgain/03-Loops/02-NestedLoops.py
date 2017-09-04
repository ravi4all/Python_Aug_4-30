# for i in range(6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()
#
#
# for i in reversed(range(6)):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

# for i in range(6):
#     print("*" * i)

# for i in range(6):
#     print(" " * (6-i) + "*" * (2*i+1))

for i in reversed(range(6)):
    print(" " * (6-i) + "*" * (2*i+1))
