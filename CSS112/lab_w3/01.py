# Count the number of times a word appears in a string.
# # Python

q = input()
s = input()
t = ''
for c in s:
    if c in ['"', '(', ')', ',', '.', "'"]:
        t += ' '
    else:
        t += c
c = 0
for w in t.split():
    if w == q:
        c += 1
print(c)
