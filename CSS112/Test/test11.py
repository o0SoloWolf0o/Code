def f1():
    a = input()
    b = int(input())
    for i in range (b):
        print(a)

def f2():
    a = input()
    b = int(input())
    c = [a]*b
    print(c)

def g():
    m = int(input())
    b = int(input())
    n = int(input())
    c = int(input())
    x = (c-b)/(m-n)
    y = m*x + b
    if m == n and b != c: return 1
    elif m == n and b == c: return 2
    return x,y

def h():
    x = int(input())
    for i in range(x):
        if i%2==0:
            print(i)
