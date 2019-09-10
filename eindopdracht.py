def readfile():
    with open('hellothere.txt') as f:
      bestandsdata = f.read().split('\n')

    dictionary = {}

    for item in bestandsdata:
        if not item == '':
            woord1, woord2 = item.split("=")
            dictionary[woord1] = woord2
    return dictionary

def addtofile(newkey, newvalue):
    with open('hellothere.txt', 'a') as f:
        f.write(newkey + "=" + newvalue + "\n")


'''
def removefromfile(removedkey):
    dictionary = readfile()
    for i in range(len(dictionary)):
        if removedkey == dictionary[i]:
            print(dictionary[i])
    with open("memes.txt", "a") as b:
        regel = int(input("Welke regel wilt u verwijderen? : "))
        regel = regel - 1
        del line[regel]
removefromfile("Sheev Palpatine")

'''
