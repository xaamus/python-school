a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))
if a>b and b>c:
    print(a)
    print(b)
    print(c)
if a>c and c>b:
    print(a)
    print(c)
    print(b)
if b>a and a>c:
    print(b)
    print(a)
    print(c)
if b>c and c>a:
    print(b)
    print(c)
    print(a)
if c>a and a>b:
    print(c)
    print(a)
    print(b)
if c>b and b>a:
    print(c)
    print(b)
    print(a)