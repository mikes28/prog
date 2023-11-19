def penzFelvaltas(osszeg, aprok):
    i=0
    couts={f"{aprok[i]}":0 for i in range(len(aprok))}
    while osszeg > 1:
        if osszeg//aprok[i] == 0:
            i+=1
        else: 
            couts[f"{aprok[i]}"]+=1
            osszeg -= aprok[i]
    if osszeg == 1:
        couts["1"]+=1
    return couts


def safeInput(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Kérlek számot adj meg!")

def main():
    aprok=[500, 200, 100, 50, 20, 10, 5, 2, 1]
    adatok=penzFelvaltas(int(safeInput("Kérlek add meg az összeget, amit fel szeretnél váltani!")),aprok)

    for a in range(len(adatok)):
        if adatok[f"{aprok[a]}"] != 0:
            print(f"""{adatok[f"{aprok[a]}"]}db {aprok[a]}ft-os""")

if __name__ == "__main__":
    main()
