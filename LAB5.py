def letterGrade(grade):
    if grade <= 100 and grade >= 90:
        return("You made an A.")
    if grade < 90 and grade >= 80:
        return("You made a B.")
    if grade < 80 and grade >= 70:
        return("You made a C.")
    if grade < 70 and grade >= 80:
        return("You made a D.")
    if grade < 60 and grade >= 0:
        return("You made an F.")

def countLetter(aWord, aLetter):
    aList = []
    for i in aWord:
        aList.append(i)
    return aList.count(aLetter)

def eyeForI(aString):
    aList = []
    newString = ""
    for i in aString:
        aList.append(i)
    for c in aList:
        if c == "i" or c == "I":
            aList[aList.index(c)] = "eye"
    for x in aList:
        newString = newString + x
    print(newString)

def wordMirror(aString):
    reverse = aString[::-1]
    newString = aString + reverse
    return newString

def encryption(aString):
    for i in aString:
        if i == "a":
            aString = aString.replace(i, "@")
        if i == "e":
            aString = aString.replace(i, "()")
        if i == "h":
            aString = aString.replace(i, "#")
        if i == "l":
            aString = aString.replace(i, "1")
        if i == "r":
            aString = aString.replace(i, "+")
        if i == "s":
            aString = aString.replace(i, "$")
        if i == "v":
            aString = aString.replace(i, "^")
        if i == "x":
            aString = aString.replace(i, "*")
    print("The encrypted code is:", aString)

def countDown(startNum, countBy):
    while startNum >= 1:
        print(startNum)
        startNum = startNum - countBy
    print("Blast off!")