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


