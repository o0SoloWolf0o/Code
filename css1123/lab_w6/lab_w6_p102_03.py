x = input()
dictionary = {}
for i in x:
    dictionary[i] = dictionary.get(i, 0) + 1
print(dictionary)