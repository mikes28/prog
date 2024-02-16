class Food:
    def __init__(self, name:str, amount:int, cal:int, allergies:list[str]):
        self.name = name
        self.amount = amount
        self.cal = cal
        self.allergies = allergies
    def isAllergic(self, knownAllergies: list[str]):
        return knownAllergies in self.allergies
    def howManyCals(self):
        return self.cal*self.amount
    def __str__(self) -> str:
        return f" Name : {self.name} \n Amount : {self.amount}g \n Cal : {self.cal}cal/100g \n Allergy : {str(self.allergies)}"


def elso():
    food_list=[]
    food_list.append(Food("alma", 10, 1000, ["none"]))
    food_list.append(Food("korte", 10, 1000, ["none"]))
    food_list.append(Food("pizza", 10, 7000, ["liszt", "tej"]))


    for i in food_list:
        if i.isAllergic("liszt"):
            print(f"igen, {i.name}-ban/ben van liszt")
        else:
            print(f"nem, {i.name}-ban/ben nincs liszt")
        print(f"{i.name} has {i.howManyCals()} cals")
        print(i)
        print('*' * 35)

""" masodik feladat """


class Product:
    def __init__(self, name: str, price: int, pieces: int):
        self.name = name 
        self.price=price
        self.pieces = pieces
    def toBePaid(self):
        return self.price*self.pieces
    def __str__(self)->str:
        return f" Name : {self.name} \n Pieces : {self.pieces}g \n Price : {self.price}"


def masodik():
    print("MÁSODIK FELADAT")    
    print('*'*35)

    prod_list = []
    prod_list.append(Product("alma", 200, 50))
    prod_list.append(Product("korte", 156, 42))
    prod_list.append(Product("barack", 100, 68))


    for i in prod_list:
        print(i)
        print(f" Full Price: {i.toBePaid()}")
        print('*' * 35)


if __name__ == "__main__":
    elso()
    masodik()