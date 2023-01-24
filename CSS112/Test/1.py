number_input1 = int(input())
subject_room = {}
for i in range(number_input1):
    department, room_left = input().split()
    subject_room[department] = int(room_left)

students = []
number_input2 = int(input())
for j in range(number_input2):
    x = input().split()
    x[0], x[1] = float(x[1]), x[0]
    students.append(x)

students = sorted(students)[::-1]
results = {}
for k in students:
    for l in k[2:]:
        if subject_room[l] > 0:
            results[k[1]] = l
            subject_room[l] -= 1
            break

sort_results = sorted(results)
for m in sort_results:
    print(m, results[m])