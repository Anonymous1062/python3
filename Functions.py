def hello():
    for i in range(10):
        print("Hello there!")

hello()

def x5():
    for i in range(10):
        a = i + 1
        print(a * 5)

x5()

def helloThere(counter):
    for i in range(counter):
        print("Hello there!")

helloThere(12)

def stringPrint(string, getal):
    for i in range(getal):
        print(string)

stringPrint("This is where the fun begins", 13)

def letterArray(letters):
    for i in range(len(letters)):
        b = i + 1
        word = letters[i] * b
        print(word)

array = ["l", "e", "n", "n", "y"]
letterArray(letters)

def max_van_3(r, b, g):
    if (r > b):
        if (r > g):
            return r
    if (b > r):
        if (b > g):
            return b
    if (g > r):
        if (g > b):
            return g

print(max_van_3(420, 66, 69))
