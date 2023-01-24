n = int(input())
faculty = {}
for i in range(n):
    name,fac = input().split()
    if fac in faculty:
        faculty[fac].add(name)
    else:
        faculty[fac] = {name}
find_fac = input().split()
answerset = set()
for j in find_fac:
    if j in faculty:
        answerset = answerset.union(faculty[j])
print(' '.join(sorted(answerset)))