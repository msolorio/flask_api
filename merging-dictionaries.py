from collections import defaultdict

dict1 = {
    'a': 12,
    'b': 11,
    'c': 9
}

dict2 = {
    'a': 24,
    'b': 22,
    'd': 31
}

################################################
# Looping over second dictionary
# dict3 = dict1.copy()

# for key, value in dict2.items():
#     dict3[key] = value


# print(dict3)


################################################
# Using .update() method

dict4 = dict1.copy()

dict4.update(dict2)

print(dict4)