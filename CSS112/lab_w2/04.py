marks = {}

for i in range(3):
    name,age = input().split()
    age = int(age)
    marks[name] = age

print(marks[input()])