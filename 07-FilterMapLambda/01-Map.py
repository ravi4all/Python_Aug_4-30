cel = [34.5, 28.1, 39.3, 33.2, 37.5]

def tempConv(c):
    return float(9/5 * c+32)

F = list(map(tempConv, cel))

print(F)
