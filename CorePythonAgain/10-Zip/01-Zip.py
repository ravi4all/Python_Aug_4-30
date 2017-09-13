countries = ['US','UK','CHINA','INDIA','PAK']
gold = [45,40,55,12,2]
silver = [56,43,87,10,5]
bronze = [76,56,100,21,12]

countriesWithGold = list(zip(countries, gold))

# for c in countriesWithGold:
#     print(c)

total = list(zip(countries, gold, silver, bronze))

# for t in total:
#     print(t)

for i in range(len(countries)):
    g = gold[i]
    s = silver[i]
    b = bronze[i]
    c = countries[i]
    print("Total medals by {} are {}".format(c, g+s+b))
