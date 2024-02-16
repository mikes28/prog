def readDict()->dict:
    dictionary = {}
    with open('morzeabc.txt', 'r') as file:
        file.readline()
        for line in file:
            key, value  = line.split()
            dictionary[key] = value
        
        return dictionary

def inp2morz(inp:chr, dictionary:dict)->str:
    u=inp.upper()
    
    if u in dictionary:
        return(dictionary[u])
    else: 
        print("Nem található a kódtárban ilyen karakter!")
        return

def readSource()->str:
    with open('morze.txt', 'r') as file:
        return file


def Morze2Szöveg(dictionary:dict, morz:str)->str:
    file = readSource()
    for line in file:
        i = line.split(' ').strip()
        print(i)






def main()->int:
    dictionary=readDict()
    inp=input("Kérlek add meg a kerakter, amit at szeretnel:")
    print(inp2morz(inp, dictionary))
    input_file=readSource()
    print(input_file)
    Morze2Szöveg(dictionary, input_file)
    


    





if __name__ == '__main__':
    main()