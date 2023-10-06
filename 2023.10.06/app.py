import math

def readF(file):
    return open(f"inputs/{file}", encoding="UTF-8")

def formatData(data):
    dataCsucs, dataHegy, dataMagasság=[], [], []
    header=data.readline()
    for i in data:
        data=i.strip().split((";"))
        dataCsucs.append(data[0])
        dataHegy.append(data[1])
        dataMagasság.append(int(data[2]))
    return(dataCsucs, dataHegy, dataMagasság)

def avg(data):
    return sum(data)/len(data)

def highest(cs, he, ma):
    highest= max(ma)
    indexOfBiggest=ma.index(highest)
    return [cs[indexOfBiggest], he[indexOfBiggest], ma[indexOfBiggest]]

def higherThan(cs, he, ma, num)



def main():
    data=readF("hegyekMo.txt")
    dataCsucs, dataHegy, dataMagasság = formatData(data)
    print(f"A hegyek száma: {len(dataCsucs)}")
    print(f"A hegyek magasságainak átlaga: {avg(dataMagasság)}")
    res= highest(dataCsucs, dataHegy, dataMagasság)
    print(f"""A legmagasabb hegycsúcs adatai:
    neve: {res[0]}
    Hegység:{res[1]}
    Magasság:{res[2]}""")

main()