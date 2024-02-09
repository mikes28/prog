def PrimSzam(szam: list[int]):
    prim = 0
    lista = list(range(10)) + szam
    for i in lista:
        for num in szam:
            if num % i == 0:
                prim += 1
                if prim > 2:
                    return True
    return False

print(PrimSzam([50]))
