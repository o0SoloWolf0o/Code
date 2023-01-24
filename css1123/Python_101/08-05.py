Number_Input1 = int(input())
result = {}
for i in range(Number_Input1):
    first , last , tel = input().split()
    name = first + ' ' + last
    result[name] = tel
    result[tel] = name

Number_Input2 = int(input())
for j in range(Number_Input2):
    question = input()
    if question in result:
        print(question + '-->' + result[question])
    else:
        print(question + '-->' + "Not found")