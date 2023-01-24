a, b = [float(i) for i in input().split()]
c = complex(a, b)
d = c.conjugate()+ c
print ("{:.0f}".format(d.real) 
    if d.real.is_integer() 
    else d.real)