class Auto:
    def __init__(self, marka:str, tipus:str, evjarat:int, szin:str, ar:int):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
        self.szin = szin 
        self.ar = ar
    def __str__(self):
        return f"{self.marka} {self.tipus} {self.evjarat} {self.szin}"
    def anyad(self):
        return self.ar+5

class Telefon:
    def __init__(self, marka:str, tipus:str, evjarat:int, szin:str):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
        self.szin = szin 
    def __str__(self) -> str:
        return f"{self.marka} {self.tipus} {self.evjarat} {self.szin}"
    

auto = Auto("Opel", "Astra", 2005, "feher", 69)
print(auto)
auto.tipus="a"
print(auto)
print(auto.anyad())
tel = Telefon("Samsung", "Galaxy", 2015, "fekete")
print(tel)