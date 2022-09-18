
ccc = dict()
ccc['csev'] = 1

# to check if key exists, use in operator

names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

count = dict()

# how we usually do:

# for name in names :
#     # checking key in dictionary
#     if name in count :
#         count[name] = count[name] + 1
#     else :
#         count[name] = 1


# pro method, compress above into 1 line:

for name in names :
    count[name] = count.get(name, 0) + 1

print(count)


# loop through dictionary:

foods = { 'rice': 5, 'noodle': 7, 'sauce' : 8, 'avocado': 3 }

highest_food = None
highest_amount = None

# for item in foods :
#     if highest_food is None or foods[item] > highest_amount :
#         highest_food = item
#         highest_amount = foods[item]

# better py version for above loop using very cool dict method .items() to directly key value pairs :
# other dict methods for to convert to list: list(dict), dict.keys(), dict.values()

for item, amount in foods.items() :
    if highest_food is None or amount > highest_amount :
        highest_food = item
        highest_amount = amount

# print(foods.keys())

print ('highest food is', highest_food, 'and amount is', highest_amount)