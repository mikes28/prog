def readData():
    dataCsucs, dataHegy, dataMagasság=[], [], [] #a harom lista letrehozasa
    with  open("inputs/hegyekMo.txt", encoding="UTF-8") as data: #csak addig van megnyitva, ameddog hasznaljuk
        header=data.readline()#header leszedése
        for i in data: #adatok kicsomagolasa
            data=i.strip().split((";"))
            dataCsucs.append(data[0])
            dataHegy.append(data[1])
            dataMagasság.append(int(data[2]))
        return dataCsucs, dataHegy, dataMagasság #adatok returnolasa a main ciklusba
def avg(data):
    return sum(data)/len(data) #lista szamainak atlaga

def getHighestIndex(data):
    return data.index(max(data)) #legnagyobb erteku elem indexenek vissazadasa

def validNumer(inp_text): #input validalasa
    while True: #addig fut, mig nem lepunk ki belole
        inp=input(inp_text)  #input kerese megadott szoveggel
        try: 
            num=int(inp) #megprobani atalakitani
            return num
        except ValueError: #ha hibat dob
            print("Érvénytelen szám, kérlek adj meg egy pozitív egész számot! ")
        
def getIndexesOfdata(data, name): #megkeresi a listaban a megadott erteku osszes elemet
    indexes=[i for i ,e in enumerate(data) if e == name]
    return(indexes) #visszadja oket egy listaban

def borzsony(dataHegy, dataMagasság, input_value): 
    borzsony_indexes=getIndexesOfdata(dataHegy, "Börzsöny") #megszerzi a borzsonyi adatok indexeit
    for i in borzsony_indexes: #borzsony_indexes osszes indexevel megnezi a feltetelt
        if dataMagasság[i] > input_value: #teszteli az egyenloseget
            return f"Van {input_value} méternél magasabb hegycsúcs a Börzsönyben!"
    else: return  f"Nincs {input_value} méternél magasabb hegycsúcs a Börzsönyben!"

def convertToFeet(data): #labba konvertalja a bemeno adatot
    number=round(data*3.280839895, 2) #kerekit
    if str(number)[-2:]==".0": #ha hatulrol szamult ket karaktere .0 levagja a veget
        number=int(str(number)[:-2]) 
    return number #visszaadja a szamot atkonvertalva

def higerThan3000(dataMagasság): #teszteli jpogy a szam nagyobb e 3000nel
    higher=0 #lista letrehozasa
    for i in range(len(dataMagasság)): #lefut dataMagassag elemeinek szamaszor
        if data:=convertToFeet(dataMagasság[i])>3000: #teszteli hogy dataMagassa feetben merve > 3000 és ebbol keszít egy valtozot, hogy azt utanna meg lehessen szamolnui
            higher+=1 #ha igaz, +1
    return higher #a a szamot returnoli

def getStatistics(dataHegy, dataCsucs): #statisztikak letrehozasa
    statistics={} #dictionary letrehozasa
    for i in range(len(dataHegy)): #lefut dataHegy elemeinek szamaszor
        if dataHegy[i] not in statistics: #ha meg nincs a szotarban hozzaadja 1es kezdeti ertekkel
            statistics[dataHegy[i]]=1
        elif dataHegy[i] in statistics: #ha benne van, akkor updateli es a value++
            statistics.update({dataHegy[i]: statistics[dataHegy[i]]+1})
    return statistics #return statistics

def outputFile(dataCsucs, dataMagasság): #kimeneti file
    with open("output.txt", "w", encoding="UTF-8") as data:   #csak addig van megnyitva, ameddog hasznaljuk
        data.write("Hegycsúcs neve; Magasság láb\n") #header
        for i in range(len(dataCsucs)): #lefut dataHegy elemeinek szamaszor
            data.write(f"{dataCsucs[i]};{convertToFeet(dataMagasság[i])}\n") #soronkent beleirja es atkonvertalja a szamot


def main():
    dataCsucs, dataHegy, dataMagasság = readData() #listak ertekkel allatasa

    print(f"A hegyekcsúcsok száma: {len(dataCsucs)}")#heygek megszamolasa

    print(f"A hegyek magasságainak átlaga: {avg(dataMagasság)}") #magasságok atlaganak megadasa a def avg()vel

    res= getHighestIndex(dataMagasság) #legmagasabb ertek indexenek megkeresese majd a harom listabol valo kivalsztasa
    print(f"""A legmagasabb hegycsúcs adatai: 
    neve: {dataCsucs[res]}
    Hegység:{dataHegy[res]}
    Magasság:{dataMagasság[res]}""")

    input_value=validNumer("Kérek egy magasságot: ") #szamm tesztelese
    print(borzsony(dataHegy, dataMagasság, input_value)) #borzsony hegysegeinek magassagaval valo osszehasonlitas

    print(f"3000 lábnál magasabb hegyek száma: {higerThan3000(dataMagasság)}") #3000labnal nagyob  hegysegek megkeresese

    print(getStatistics(dataHegy, dataCsucs)) #statisztikak kiirasa
    
    outputFile(dataCsucs, dataMagasság)#file végén test;0. hogy látható legyen, a .0 eltüntetése

main() #main ciklus elinditasa