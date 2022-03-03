t1=input()
t2=input()
def porownanie(t1,t2):
    t1_len = len(t1)
    t2_len = len(t2)
    if t1_len < t2_len:
        n=len(t1)
        wynik=0
        for i in range(n):
            if t1[i]!=t2[i]:
                wynik+=1
        return wynik
    else:
        n=len(t2)
        wynik=0
        for i in range(n):
            if t1[i]!=t2[i]:
                wynik+=1
        return wynik
print(porownanie(t1,t2))
