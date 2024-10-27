dictionary = {"axe":"this is a type of tool for cutting woods.",
              "utensils":"this is mainly used in kitchen."}

print(dictionary["axe"])

dictionary["axe"]= "this is another form of meaning."
# print(dictionary["axe"])

# print(dictionary)

# loop through dictionary

for key in dictionary:
    print(key)
    print(dictionary[key])
