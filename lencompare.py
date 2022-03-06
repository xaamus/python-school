tx1=input('Podaj pierwszy tekst\n')
tx2=input('Podaj drugi tekst\n')
def porownanie(tx1,tx2):
    tx1len = len(tx1)
    tx2len = len(tx2)
    if tx1len < tx2len:
        n=len(tx1)
        wyn=0
        for i in range(n):
            if tx1[i]!=tx2[i]:
                wyn+=1
        return wyn
    else:
        n=len(tx2)
        wyn=0
        for i in range(n):
            if tx1[i]!=tx2[i]:
                wyn+=1
        return wyn
print(porownanie(tx1,tx2))
