import random as rand

nums = {
    1: "első",
    2: "második",
    3: "harmadik",
    4: "negyedik",
    5: "ötödik",
    6: "hatodik",
    7: "hetedik"
}

def egyediPontszam()->int:
    return (rand.randint(1, 5)*10)

def csapatPontszam()->list:
    return [egyediPontszam() for i in range(7)]

def pontOsszesites(pontok:list)->int:
    return sum(pontok)

def gyoztes(csapat1:list, csapat2:list, i:int)-> bool:
    draw=True
    while draw:
        csapat1Pont = pontOsszesites(csapat1)
        csapat2Pont = pontOsszesites(csapat2)
        if csapat1Pont == csapat2Pont:
            draw=True
            print(f"{i}. kör végeredménye döntetlen lett, ezért újra jönnek a csapatok!")
            csapat1 = csapatPontszam()
            csapat2 = csapatPontszam()
        else:
            draw=False
            print(f"{i}. kör:")
            stri=''.join(str(e)+" " for e in csapat1)
            print(f"Ürmacskák: {stri} -> {csapat1Pont}")
            stri=''.join(str(e)+" " for e in csapat2)
            print(f"Szuperegerek: {stri} -> {csapat2Pont}")
            print(f"Az {nums[i]} kört a Szuperegerek nyerték") if csapat2Pont > csapat1Pont else print(f"Az {nums[i]} kört a Ürmacskák nyerték")
            return True if csapat1Pont < csapat2Pont else False
    
def jatek()->int:
    urmacskak=0
    for i in range(1, 8):
        if gyoztes(csapatPontszam(), csapatPontszam(), i):
            urmacskak+=1
    return urmacskak
    

if __name__ == "__main__":  
    urmacskak=jatek()
    print("*"*50)
    print("Az Ürmacskák nyerték a játékot!") if urmacskak > 3 else print("A Szuperegerek nyerték a játékot!")
    print("*"*50)
   
