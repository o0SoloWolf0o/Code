n1 = list(input().split())
n1 = [int(i) for i in n1]
strings1 = [str(integer) for integer in n1]
a_string1 = "".join(strings1)
an_integer1 = int(a_string1)
n2 = list(input().split())
n2 = [int(i) for i in n2]
strings2 = [str(integer) for integer in n2]
a_string2 = "".join(strings2)
an_integer2 = int(a_string2)
n3 = an_integer1 + an_integer2
res = [int(x) for x in str(n3)]
res.reverse()
print(res)