import random
veletlen_szamok=[]

def sorozat():
    for i in range(0,8,1):
        szam: int=random.randint(-100,859)
        veletlen_szamok.append(str(szam))
        if szam < 7:
            print(szam,end=";")
        else:
            print(szam,end=" ")
        

    