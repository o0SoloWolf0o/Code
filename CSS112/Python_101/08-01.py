def reverse(dictionary):
    new_dictionary = {value: key for key, value in dictionary.items()}
    return new_dictionary

def keys(dictionary, value):
    new_dictionary = []
    for key in dictionary:
        if dictionary[key] == value:
            new_dictionary.append(key)
    return new_dictionary

#exec(input().strip())

#print(reverse({3:"A", 2:"B"}) == {"A":3, "B":2})
#print(keys({3:33, 4:33, 5:55, 2:33}, 33)) 
#print(keys({3:33, 4:33, 5:55, 2:33}, 9999))
