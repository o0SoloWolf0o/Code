# Define the set of characters
characters = "  0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Set the desired length of the combinations
length = 8

# Generate all possible combinations
for i in range(len(characters)):
    for j in range(len(characters)):
        for k in range(len(characters)):
            for l in range(len(characters)):
                for m in range(len(characters)):
                    for n in range(len(characters)):
                        for o in range(len(characters)):
                            for p in range(len(characters)):
                                combination = characters[i] + characters[j] + characters[k] + characters[l] + characters[m] + characters[n] + characters[o] + characters[p]
                                print(combination)
