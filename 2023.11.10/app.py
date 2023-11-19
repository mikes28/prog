from operator import attrgetter
import numpy

class Struct:
    def __init__(self, city, name1, name2, size):
        self.city=city
        self.name1=name1
        self.name2=name2
        self.size=size

def readFile(file):
    list=[]
    with open(file, encoding="UTF-8") as file:
        file.readline()
        for line in file:
            data=line.strip().split(";")
            list.append(Struct(data[0],data[1],data[2],data[3]))
    return list


def inputValidation(ques):
    inp=" "
    while len(inp)<3:
        inp=input(ques)
    else:
        return inp
        
def searchForCity(file_data):
    wcity=inputValidation("Kérem a város nevét: ")
    for item in file_data:
        if str(item.city).lower() == wcity.lower():
            return True

    return False
            


def main():
    file_data=readFile("vb2018.txt")
    print(f"Összesen {len(file_data)} stadionban volt játék megszervezve.")

    smallest_size = min(file_data,key=attrgetter('size'))
    print(f"""Legkissebb stadion:
    neve:{smallest_size.name1}, {smallest_size.name2}
    város: {smallest_size.city}
    férőhely: {smallest_size.size}
    """)
    a= list(int(obj.size) for obj in file_data)
    avg=round(sum(a)/len(a), 1)
    print(f"Átlagos férőhely: {avg}")

    print(f"""Két névvel rendelkező stadionok: {len(list(b.name1 for b in file_data if b.name2!="n.a."))}""")


    if searchForCity(file_data):
        print("igen, volt itt esemény!")
    else:
        print("Nem, nem volt itt esemény.")
    
    uniq=set()
    for i in file_data:
        uniq.add(i.city)
    
    

    print(f"Összesen {len(uniq)} városban volt esemény.")




main()