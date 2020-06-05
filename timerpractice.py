import time

starttime = time.time()
seconds = 5

while True:
    currenttime = time.time()
    elapsedtime = currenttime - starttime

    if elapsedtime > seconds :
        print("Zavrseno u " + str(int(elapsedtime)) + "sekundi")
        break