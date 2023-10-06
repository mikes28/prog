
readData= []  #globalis: mindenhol elérem
usedTimes=[]
lists=[]
writeData=[]
def beolvas():
     
    data= open("kiallit.be", encoding="UTF-8")
    dataOut= open("kiallit.ki", "w",  encoding="UTF-8")

    numOfPeople=int(data.readline())
    for item in data:
        reszek= item.strip().split(' ') #making the string values into number to be able to sort
        readData.append( [int(reszek[0]), int(reszek[1])])
    # print(readData)
    readData.sort() 
    usedTimes=list(readData[0])
    print(readData)
    for i in readData:
        lists=list(range(i[0], i[1]))
        lists.append(i[1])
        usedTimes+=lists

    usedTimes=list(set(usedTimes))
    print (usedTimes)

    res= list(set(usedTimes))

    for i in range(len(res)-1):
        if  (res[i-1]+1) is not res[i]:
            writeData.append(res[i])
        if  (res[i]+1) is not res[i+1]:
            writeData.append(res[i])
        
    writeData.append(res[-1])

    dataOut.write(f"{int(int(len(writeData))/2)}\n")
    for i in range(len(writeData)):
        if (i%2):
            dataOut.write(f"{writeData[i]}\n")
        else:
            dataOut.write(f"{writeData[i]} ")


def main():
    beolvas()
    
main()