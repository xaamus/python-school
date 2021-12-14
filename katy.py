print("Podaj miary kątów")
a=int(input("Podaj a: "))
b=int(input("Podaj b: "))
c=int(input("Podaj c: "))
if (a+b+c!=180) or (a==0 or b==0 or c==0):
    exit("Wprowadź poprawne dane!")
if (a==90 and b<90 and c<90) or (b==90 and a<90 and c<90) or (c==90 and a<90 and b<90):
    print("Trójkąt prostokątny")

if (a>90 and b<90 and c<90) or (b>90 and a<90 and c<90) or (c>90 and a<90 and b<90):
    print("Trójkąt rozwartokątny")

if (a<90 and b<90 and c<90):
    print("Trójkąt ostrokątny")