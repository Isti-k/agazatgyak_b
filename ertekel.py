def ertekeles():
    Het_napja:str=(input("Adja meg a hét egyik napját!"))

    Ora_neve:str=(input("Adja meg az óra nevét!"))

    Ertekeles:int=int(input("Adja meg az értékelést!"))

    if 0 < Ertekeles <=5:
        print("Köszönjük az értékelést!")
    elif Ertekeles > 0:
        print("Az értékelés nem lehet negatív!")
    elif Ertekeles < 5:
        print("5 pont feletti értékelés nem elfogadható!")

        print(f"Hét napja:{Het_napja}\n,Óra neve:{Ora_neve}\n,Értékelés:{Ertekeles}")

