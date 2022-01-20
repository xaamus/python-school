print("Jaki system podajesz?")
print("1. Dziesiętny")
print("2. Dwójkowy")
print("3. Ósemkowy")
print("4. Szesnastkowy")
sys=int(input())
print("Podaj liczbę")
lic=int(input())
def dec(val):
    if val>=1:
        dec(val//2)
    print(val%2,end='')
if sys==1:
    print("System 2: ",bin(lic)[2:])
    print("System 8: ",oct(lic)[2:])
    print("System 16: ",hex(lic)[2:])
if sys==2:
    print("System 10: ",dec(lic)[2:])
    print("System 8: ",oct(lic)[2:])
    print("System 16: ",hex(lic)[2:])
if sys==3:
    print("System 10: ",dec(lic)[2:])
    print("System 2: ",bin(lic)[2:])
    print("System 16: ",hex(lic)[2:])
if sys==4:
    print("System 10: ",dec(lic)[2:])
    print("System 2: ",bin(lic)[2:])
    print("System 8: ",oct(lic)[2:])
