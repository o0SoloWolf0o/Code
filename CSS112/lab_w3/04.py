# The code checks if the length of the solution is the same as the answer. If it is, it checks if each
# character in the solution is equal to the corresponding character in the answer. If it is, it adds
# one to the counter. If it is not, it prints the number of correct characters.
sol = input()
ans = input()
if len(sol) != len(ans):
    print('Incomplete answer')
else:
    c = 0
    for i in range(len(sol)):
        if ans[i] == sol[i]:
            c += 1
    print(c)
