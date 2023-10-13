def _20():
    n=int(input("Kérlek add meg a hosszt"))
    m=int(input("Kérlek add meg a magasságot"))
    for i in range(m):
        print(" "*(n-i),"*"*n ) #in c# string str = new string("*", i)

def _21():
    m=int(input("Kérlek add meg a magasságot"))
    for i in range(1,m+1):
        print(" "*(m-i),"*"*(i*2-1), sep="" )

def _22():
    n=int(input("Kérlek add meg a hosszt"))
    m=int(input("Kérlek add meg a magasságot"))
    print("*"*n)
    for i in range(1, m+1):
        print("*"," "*(n-2),"*", sep="")
    print("*"*n)

def _25():
    list=[]
    n=int(input("adj meg egy pozitiv egesz szamot: "))
    for i in range(1,n+1):
        if not n%i:
            print(i)
        
def _29():
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(abc)):
        print(abc[i:len(abc)],abc[:i], sep="") 



""" _20() """
""" _21() """
""" _22()"""
""" _25() """
_29()