import random as rand


def CheckPassword(psswd):
    while True:
        if input("kérlek add meg a jelszót! ")==psswd:
            print("Sikeres bejelentkezés!")
            break
    
def HeadOrTail():
    while True:
        try: 
            isHead = float(input("Fej(1) vagy írás(0)? "))
            if isHead != 1 and isHead != 0:
                raise ValueError            
        except ValueError:
            print("Kérlek számot adj meg(1 vagy 2)!")            
        else:
            if isHead==rand.randint(0,1):
                print("Gratutálok, eltaláltad!")
                break
            else:
                print("Sajnos ez most nem sikerült.:(")
                input("Kilépéshez ird be: [q], továbblépés: [Enter]")


def AddChecks():
    added = 0
    i=1
    while True:
        try:
            val=int(input(f"Kérlek add meg az {i}. összeget! "))
            if val%100:
                raise ValueError
        except ValueError:
            print("Kérlek ellenőrizd, jó számot írtál-e be!")
        else:
            added+=val
            i+=1
            if i==7:
                    print(f"A {i} hónap alatt befizetett összeg: {added}")
                    break



def status(stats):
    print(f"""
{stats["JHp"]} - Játékos életereje
{stats["SzHp"]} - Szörny életereje
""")
    
def Game():
    stats={"JHp":100,
        "JDobasok":0,
        "SzHp":100
    }

    while True:
        #kezdodik a jatek
        while True:
                    inp=input("A játékos támad![dobáshoz nyomd meg az [enter]-t, ha nem akarsz dobni, írd be: [q]]")
                    if inp!="q":
                        dobas=rand.randint(1,6)
                        print(f"A játékos dobása: {dobas}")
                        if dobas==1:
                            print(f"sajnos mivel egyest dobtál, megbotlottál, és a szörny támadhat! okozott sebzés {stats['JDobasok']}")
                            status(stats)
                            break
                        else:
                            stats["JDobasok"]+=dobas
                            print(f"Eddigi sebzés: {stats['JDobasok']}")
                    else:
                       status(stats)
                       break
                    
        stats["SzHp"]-=stats["JDobasok"]
        stats["JDobasok"]=0

        print("A szörny támad!")
        dobasok=[]
        for i in range(3):
            dobasok.append(rand.randint(1,6))
        print(f"A szörny dobásai: {dobasok[0]}, {dobasok[1]}, {dobasok[2]}")

        stats["JHp"]-=sum(dobasok)
        status(stats)
        if stats["JHp"]<=0:
            print("Sajnos vesztettél, a szörny megölt!")
            break
        elif stats["SzHp"]<=0:
            print("Gratulálok, legyőzted a szörnyet!")
            break
          


def main():
    CheckPassword("Alma*")
    HeadOrTail()
    AddChecks()
    Game()

main()