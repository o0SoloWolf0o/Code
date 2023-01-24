def somefunc(temp):
    for e in temp:
        a = str(temp[e])
        count = 0
        for i in range(len(a)-1):
            if a[i] != a[i+1]:
                count += 1
        temp[e] = count
    return temp 


temp = {'t1': 1010101, 't2': 1100110110}
temp_count = somefunc(temp)
print(temp_count)