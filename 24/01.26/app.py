import random as rand

hit_calc={
    "Ütés": lambda x: x*10,
    "Rúgás": lambda x: x*15,
    "Kardhasítás": lambda x: x*12,
    "Eltűnés": lambda x: x*8
}


def safeNumInp(text:str, max:int, min:int ) -> int:
    while True:
        try:
            a= int(input(text))
            if min <= a <= max:
                return a 
            else:
                raise ValueError
        except ValueError:
            print(f"Kérek {max} és {min} között add meg a számot!")
        


def selectPlayer():
    return(safeNumInp("Kérlek válassz a két karkater közül [1-2]: ", 2, 1))


def intro(chars:dict):
    print(f"""
    A Karakteres Kaland nevű kis játékban egy kitalált világban {len(chars)} karakter:\n
        """)
    for n in range(len(chars)):
        print(f"""
Hősi Herculész [1]: 
                Erő:{chars[n]["power"]}, Sebesség:{chars[n]["speed"]}
                    Képességei:    
                            {", ".join(chars[n]["skills"])}
""")

    print("""    
    Ők vesznek részt egy izgalmas kalandban. Mindkét karakternek vannak saját képességei és eszközei.
    A játék nezhézsége körről körre növekszik.""")
    

def hit(skill, i):
    return hit_calc[skill](i)
    

def challenge(i, curr_char):
    return hit(i, rand.choice(curr_char["skills"]))
    



def main():
    chars = [
        {"name":"Hősi Herculész", "power":10, "speed":5, "skills":["Ütés", "Rúgás"]},
        {"name":"Szuper Szonja", "power":5, "speed":10, "skills":["Kardhasítás", "Eltűnés"]}
    ]


    intro(chars)
    p=selectPlayer()
    curr_char = chars[p]
    curr_char["health"]=rand.randint(10,15)*10
    for i in range(1,6):
        print(challenge(i, curr_char))
       



if __name__ == "__main__":
    main()
