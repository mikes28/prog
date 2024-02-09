class Auto:
    def __init__(self, marka, tipus, evjarat, szin):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
        self.szin = szin 
    def __str__(self):
        return f"{self.marka} {self.tipus} {self.evjarat} {self.szin}"

class Telefon:
    def __init__(self, marka, tipus, evjarat, szin):
        self.marka = marka
        self.tipus = tipus
        self.evjarat = evjarat
        self.szin = szin 
    def __str__(self):
        return f"{self.marka} {self.tipus} {self.evjarat} {self.szin}"
    


auto = Auto("Opel", "Astra", 2005, "feher")
print(auto)