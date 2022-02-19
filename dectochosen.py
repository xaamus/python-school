nmb=input('Wpisz liczbę\n')
sys=int(input('Wpisz podstawę systemu\n'))
if sys==2:
    con=int(nmb,2)
    print(con)
elif sys==8:
    con=int(nmb,8)
    print(con)
elif sys==16:
    con=int(nmb,16)
    print(con)
else:
    print('Podaj poprawny system')
