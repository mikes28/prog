def PrimSzam(szam: int) -> bool:
    prim = 0
    lista = list(range(1,11))
    lista.append(szam)
    lista=list(set(lista))
    for i in lista:
        if szam % i == 0:
            prim += 1
    return prim == 2

# Test cases
test_cases = [
    # Prime numbers
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (19, True),
    (23, True),
    (29, True),
    # Composite numbers
    (4, False),
    (6, False),
    (8, False),
    (9, False),
    (10, False),
    (12, False),
    (14, False),
    (15, False),
    (16, False),
    (18, False),
    # Large prime numbers
    (15485863, True),
    (32452843, True),
    (49979687, True),
    (67867967, True),
    (86028121, True),
    (104395301, True),
    (122949823, True),
    (141650939, True),
    (160481183, True),
    (179424673, True),
    # Large composite numbers
    (15485862, False),
    (32452842, False),
    (49979686, False),
    (67867966, False),
    (86028120, False),
    (104395300, False),
    (122949822, False),
    (141650938, False),
    (160481182, False),
    (179424672, False),
    # Other numbers
    (21, False),
    (25, False),
    (27, False),
    (30, False),
    (35, False),
    (40, False),
    (45, False),
    (50, False),
    (55, False),
    (60, False),
]

# Run the tests
for i, (num, expected) in enumerate(test_cases):
    result = PrimSzam(num)
    assert result == expected, f"Test case {i+1} failed: {num} -> {result}"
    print(f"Test case {i+1} passed")