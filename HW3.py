#Vivienne Qie
#qievi@gatech.edu
#I worked on this homework assignment alone, using only this semester's materials.

def tallEnough(h):
    heightInches = int(h) / 0.39370
    if heightInches > 120 and heightInches < 190:
        return True
    else:
        return False

def whereIsWaldo(Int1, Int2):
    x = input("Guess Waldo's x-coordinate")
    y = input("Guess Waldo's y-coordinate")
    if int(Int1) == int(x) and int(Int2) == int(y):
        return("You found Waldo")
    else:
        return("Couldn't find Waldo. Better luck next time.")

import string
def allLetters(userString):
    newStr = ""
    for i in userString:
        if i in string.ascii_letters:
            newStr = newStr + i
        else:
            newStr = newStr + ""
    return(newStr)

def replaceLetter(aString, aLetter):
    anotherLetter = input("Input a letter")
    while anotherLetter not in str(aString):
        anotherLetter = input("Letter not in string. Input a letter")
    aString = aString.replace(str(anotherLetter), str(aLetter))
    print(aString)

def countUp(start, end, increment):
    while start < end + 1:
        print(start)
        start = start + increment
    print("Done!")

def numMountainRange(x):
    for i in range (1, x+1):
        aNum = i
        aNumStringForm = str(aNum)
        print(aNumStringForm * i + str(" ")*(x*2-i*2) + aNumStringForm * i)

def printTimestable():
    print("Times:", end = "\t")
    for i in range(1, 10):
        print(i, end = "\t")
    print()
    for row in range(1, 10):
        print(row, end = "\t")
        for column in range(1, 10):
            product = row * column
            print(product, end = "\t")
        print()

def printTimes(n):
    print("Times:", end = "\t")
    for x in range(1, (n+1)):
        print(x, end = "\t")
    print()
    for row in range(1, (n + 1)):
        print(row, end = "\t")
        for column in range(1, (n + 1)):
            product = row * column
            print(product, end = "\t")
        print()