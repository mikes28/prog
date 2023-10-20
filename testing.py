import random

szam =random.randint(1,10)
tipp=0
while tipp != szam:
    tipp=int(input("Tippelj: "))
    if tipp > szam:
        print("A tipp túl kicsi!")
    else:
        print("A tipp túl nagy!")
else: 
    print(f"A szam {szam} volt, és a tipp jó!")