
def openFile(source:str):
    with open(file=f"{source}.txt") as file:
        _LINESIZE = len(file.readline().strip().split())
        listx =[]
        custom_inputs=[]
        file.seek(0,0)
        for line in file:
            temp_list = line.strip().split()
            if len(temp_list) == _LINESIZE:
                listx.append(temp_list)
            elif len(temp_list)==3:
                custom_inputs.append(temp_list)
            else:
                print("Noticed some errors while reading the file")

        print(listx, sep="")
        print(listx[1][5])
        print(custom_inputs)
            



def main():
    openFile(input("Válassz nehézségi szintet. (könnyű, közepes, nehéz): "))

if __name__ == "__main__":
    main()