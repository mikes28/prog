import random


def questionAsk(ques):
    ques, ans = ques
    inp = input(ques)
    if inp == ans:
        return True
    else:
        return False


def torpe(questions, inventory):
    input(f'''Üdvözöllek Kalandor! Én vagyok a törpe, ha 3 találós kérdésből akár egyre is jól válaszolsz, akkor adok neked Élelmet \n 
    (A továbblépésekhez ezentúl bármikor nyomd meg az Entert)''')
    while questionAsk(random.choice(questions)) is False:
         i+=1
         print('''Rossz válasz!''')      
         if  i is 3:
            print("A manó felnégyelt")
            return False
    else: 
        print("Ügyes vagy, ezért kapsz élelmet!")
        inventory.extend("élelem")
        return True

def pok(inventory):
    a= random.randint(0, 500)
    b= random.randint(0, 500)
    c = a+b
    inp = int(input(f"Megláttál egy pókot, hogy továbbmenj, el kell slisszannod mellette. {a} + {b} = "))
    if (inp == c):
        print("Ügyes vagy, megkapod a sziget vízkészletét")
        inventory.extend("víz")
        return True
    else: return False


def palindrome(palindromes, inventory, items):
    inp= input("kérlek adj meg egy palindrome szót. ")
    if inp in palindromes:
        print('''Ügyes vagy, ezért kapsz: alma, futópad, 
        gépfegyver, kiskés, gránát, olló, kanál''')
        inventory.extend(items)
        return True
    else: 
        return False

def titkos(inventory):
    input("Nyomd meg az entert a dobáshoz! ")
    a = random.randint(1, 6)
    print(f"A dobásod {a}")
    if a == 6:
        return
    else :
        print("Sajnos belesétáltál egy csapdába, és beleszorültál.")
        if "kés" in inventory:
            print("Szerencséd volt, és a késeddel kivágtad magad a hálóból.")
            return True
        else: return False

def endGame(inventory):
    input("Ügyes voltál, eljutottál a játék végéhez, de még ne lélkegezz fel, mert még a végső kihívás rád vár. le kell győzd a főgonoszt!")
    if "gépfegyver" in inventory: 
        print("Ügyes voltál, sikeresen legyőzted a főgonoszt a gépfegyvereddel.")
    else: 
        a=random.randint(1, 25)
        b=random.randint(1, 25)
        while a == b:
            b=random.randint(1, 25)

        print("mivel nincs nálad gépfegyver, kockáznod kell, dobj négyszer, és dobj nagybbat mint a szörny.")
        print(f"dobásaid összege: {a}")
        print(f"A szörny dobása {b}")
        if b>a:
            print("Sajnos a szörny nagyobbat dobott mint te.")
            return False
        else: return True



def app():

    palindromes = ["ama", "apa", "ara", "arra", "bab", "dagad", "eme", "epe", "erre", "geg", "icipici", "jaj", "kajak", "kerek", "konok", "legel", "lehel", "lel", "lepel", "lohol", "pap", "radar", "sas", "sebes", "soros", "tehet", "temet", "tettet", "uccu", "uhu"]
    inventory = []
    items = ["alma", "futópad", "gépfegyver", "kiskés", "gránát", "olló", "kanál"]
    questions=[
    ("Éjjel-nappal mindig jár, mégis egyhelyben áll. Mi az?", "föld")
    ]
    good_ans= False
    i=0




    print('''Ahhoz, hogy túléld, megfelelő tárgyakat kell gyűjtened.
    - élelem
    - víz
    - fegyver
    A játék során különböző helyszínekre fogsz utazni, ahhol akadályok várnak rád. Ezek legyőzésével tudsz tárgyakt gyűjteni.
    Az "I" betű beírásával bármikor lekérdezheted a hátizyákod tartalmát!''')
    input("A játék elkezdéséhez nyomd meg az Entert")
    if torpe(questions, inventory) is False:
        print("Sajnálom, de nem jó a válaszod")
        exit(0)
    if pok(inventory) is False:
        print("Sajnálom, de meglátott a pók, és ezért el kellett futnod.")
    if palindrome(palindromes, inventory, items) is False:
        print("Ez nem volt mefelelő szó, sajnálom,")
    if titkos(inventory) is False:
        exit(0)
    if endGame(inventory) is False:
        print("Sajnálom, de a szörny megevett téged. Ha szeretnéd, kezd újra a játékot.")
    else:
        print("Gratulálok, sikerult legyőznöd az összes kihívást.")




if __name__=="__main__":
   app()