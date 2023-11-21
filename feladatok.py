def feladat1(szoveg:str):
    print("1. feladat")
    i: int = 0
    szokoz: int = 0
    while i < len(szoveg):
        if " " == szoveg[i]:
            szokoz += 1
        i += 1
    return szokoz

def feladat2(szoveg:str):
    print("2. feladat")
    i:int = 0
    szokoz_nelkul:str = ""
    while i < len(szoveg):
        if not (" " == szoveg[i]):
            szokoz_nelkul += szoveg[i]
        i += 1
    return szokoz_nelkul

def feladat3(szoveg:str):
    print("3. feladat")
    szoveg = szoveg.lower()
    szoveg = szoveg.replace("é", "e")
    szoveg = szoveg.replace("ó", "o")
    szoveg = szoveg.replace("á", "a")
    szoveg = szoveg.replace("ő", "o")
    szoveg = szoveg.replace("ú", "u")
    szoveg = szoveg.replace("ű", "u")
    szoveg = szoveg.replace("í", "i")
    szoveg = szoveg.replace("ö", "o")

    i = len(szoveg) - 1
    while i >= 0:
        print(szoveg[i], end = " ")
        i -= 1


def hazi1():
    print("1. feladat")
    hettel_oszthato: int = 0
    for i in range(1, 1001):
        if i % 7 == 0:
            hettel_oszthato += 1
    return hettel_oszthato

def hazi2():
    print("2. feladat")
    tizenkettovel_oszthato: int = 0
    for i in range(2000, 20001):
        if i % 12 == 0:
            tizenkettovel_oszthato += 1
    return tizenkettovel_oszthato

def hazi3():
    print("3. feladat")
    osszeg: int = 0
    szamok: int = 0
    szam: int = 0
    while szamok < 20:
        if szam % 3 == 0:
            osszeg += szam ** 2
            szamok += 1
        szam += 1
    return osszeg

def hazi4(szam:int):
    print("4. feladat")
    szam_osztok:int = 0
    for i in range(1, szam + 1):
        if szam % i == 0:
            szam_osztok += 1
    return szam_osztok

def hazi5(szam:int):
    print("5. feladat")
    i: int = 0
    while i > 1:
        if szam % i == 0:
            i -= 1
    return szam