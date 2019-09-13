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


def removefromfile(removedkey):
    dictionary = readfile()
    if removedkey in dictionary:
        del dictionary[removedkey]
        with open('hellothere.txt', 'w') as f:
            for item in dictionary:
                f.write(item + "=" + dictionary[item] + "\n")
        return "Successfully deleted"
    else:
        return "Impossible. Perhaps the archives are incomplete"

def menu():
    print('''
If you want to see the contents of the file, say read
If you want to add something to the file, say write
If you want to delete something from the file, say remove
If you want to stop the program, say cancel\n''')
    choice = input("Pick one of the options: ")
    if choice == "read":
        print(readfile())
        menu()
    elif choice == "write":
        addkey = input("What will the new key be? ")
        addvalue = input("What will the new value be? ")
        addtofile(addkey, addvalue)
        print("Adding to file complete")
        menu()
    elif choice == "remove":
        delkey = input("Which key do you want to remove from the file? ")
        print(removefromfile(delkey))
        menu()
    elif choice == "cancel":
        print("Program terminated")
    else:
        menu()
print("Hello there!")
menu()
