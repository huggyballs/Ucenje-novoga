dodavanje = ''

print("unosenje broja")
dodavanje = input()

if dodavanje is not '' :
    print("Uspjeh!")
else:
    print("Neuspjeh!")

print("unosenje drugog broja")
dodavanje = input()

if dodavanje != '' :
    print("Uspjeh 2!")
else:
    print("Neuspjeh 2!")

def Petlja():
    while True:
        odgovor = int(input("Unesi jedan ili dva"))
        if odgovor == 1:
            print("Unesena jedinica")
            return False
        elif odgovor == 2:
            print("Unesena dvojka")
            return False
        else:
            print("Nepravilan unos!")
            pass
        pass

Petlja()
print("Zavrsena petlja!")