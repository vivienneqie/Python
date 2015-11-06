#Vivienne Qie and Nihar Kandimalla
#qievi@gatech.edu and nkandimalla3@gatech.edu
#We worked on the homework assignment together, using only this semester's course materials.

from Myro import *
init()
setPicSize("small")

def findColor(a):
    pix = getPixels(a)
    redCount = 0
    greenCount = 0
    yellowCount = 0
    whiteCount = 0
    count = 0
    for i in pix:
        r,g,b = getRGB(i)
        if r > b and r > g:
            redCount = redCount + 1
        if g > b and g > r:
            greenCount = greenCount + 1
        if r > b and g > b:
            yellowCount = yellowCount + 1
        if r == b == g or r == b == g == 255:
            whiteCount = whiteCount + 1
    count = count + 1
    redAmount = redCount / count
    greenAmount = greenCount / count
    yellowAmount = yellowCount / count
    whiteAmount = whiteCount / count
    if redAmount > greenAmount and redAmount > yellowAmount and redAmount > whiteAmount:
        return "red"
    if greenAmount > redAmount and greenAmount > yellowAmount and greenAmount > whiteAmount:
        return "green"
    if yellowAmount > redAmount and yellowAmount > greenAmount and yellowAmount > whiteAmount:
        return "yellow"
    if whiteAmount > redAmount and whiteAmount > greenAmount and whiteAmount > yellowAmount:
        return "white"

def turn():
    random = heads()
    if random == True:
        setLED("center", 0)
        setLED("left", 1)
        wait(1)
        setLED("left", 0)
        motors(1,0,1.25)
    if random == False:
        setLED("center", 0)
        setLED("right", 1)
        wait(1)
        setLED("right", 0)
        motors(0,1,1.25)

def stopLight():
    color = findColor(takePicture())
    if color == "green":
        forward(1,2)
        stopLight()
    if color == "yellow":
        forward(0.5,2)
        stopLight()
    if color == "white":
        turn()
        stopLight()
    if color == "red":
        stop()
        beep(1,900)
