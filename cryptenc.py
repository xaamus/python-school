#0  4  8  12      1  3  5  7  9  11      2  6  10

def szyfruj(tekst):
    wynik=''
    n=len(tekst)
    for i in range(0,n,4):
        wynik+=tekst[i]
    for i in range(1,n,2):
        wynik+=tekst[i]
    for i in range(2,n,4):
        wynik+=tekst[i]
    return wynik

def deszyfruj(tekst):
    wynik=''
    n=len(tekst)
    for i in range(0,n):
        if

print(szyfruj('KRYPTOANALIZA'))
print(deszyfruj('KTAARPONLZYAI'))
