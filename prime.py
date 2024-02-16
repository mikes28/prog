def PrimSzam(szam: int) -> bool:
    prim = 0
    lista = list(range(1,11))
    lista.append(szam)
    lista=list(set(lista))
    for i in lista:
        if szam % i == 0:
            prim += 1
    return prim == 2

print(PrimSzam(1548654865346532))
