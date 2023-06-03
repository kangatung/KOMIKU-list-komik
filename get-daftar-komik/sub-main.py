with open("../daftar-komik.txt",'r') as file:
    data = file.readlines()

myReadyList = []
myWaitList = []
for a in data:
    try:
        firstPosition = a.index('Chapter')
        secondPosition = a.index('new=Chapter')
        oldChapter = int(a[firstPosition+8:firstPosition+11])
        newChapter = int(a[secondPosition+12:secondPosition+15].strip())
        if (newChapter-oldChapter) >= 10:
            myReadyList.append(a)

        else:
            waitKomik = a[:a.index("|")].strip() + "\n"
            myWaitList.append(waitKomik)
    except:
        pass

with open("ready.txt","w") as file:
    strReady = "".join(myReadyList)
    file.write(strReady)

with open("wait.txt","w") as file:
    strWait = "".join(myWaitList)
    file.write(strWait)

    