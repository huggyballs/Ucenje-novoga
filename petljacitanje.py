import nfc
import time

clf = nfc.ContactlessFrontend()
clf.open('ttyAMA0')

def main():
    try:
        while True:
            unos = ''
            print("Zelite pokusati citati? 1 - DA 3 - NE")
            
            while unos != 1 and unos != 3:

                unos = input()

                if unos == 1:
                    print("citanje")
                    starttime = time.time()
                    userID = ''

                    while True:
                        currenttime = time.time()
                        elapsedtime = currenttime - starttime

                        userID = clf.connect(rdwr={'on-connect': lambda tag: False})

                        if elapsedtime > 5 :
                            print("Neuspjesno citanje!")
                            break
                        elif userID != '' :
                            print("Uspjesno citanje!")
                            print(userID)
                            break
                        pass

                    break
                elif unos == 3:
                    print("nema citanja")
                    break
                else:
                    print("neispravan unos!")
                    pass
                pass
            pass
        pass
    except KeyboardInterrupt:
        print("Kraj rograma!")
        clf.close()
        pass

if __name__ == '__main__':
    main()