from Myro import *

def greenScreen():
    p = makePicture("hcw_clear_glasses.png")
    p2 = makePicture("tower.jpg")
    #getWidth(p2) == 427
    #getHeight(p2) == 266
    getWidth(p2) == 1280
    getHeight(p2) == 1080
    for x in getPixels(p2):
        r = getRed(x)
        g = getGreen(x)
        b = getBlue(x)
    for i in getPixels(p):
        r1 = getRed(i)
        g1 = getGreen(i)
        b1 = getBlue(i)
        if g1 > r1 and g1 > b1:
            setRed(i,r)
            setGreen(i,g)
            setBlue(i,b)
    savePicture(p,"green-screen.jpg")

def crossFade():
    p = makePicture("before-seeing-red.jpg")
    p1 = copyPicture(p)
    p2 = copyPicture(p)
    p3 = copyPicture(p)
    p4 = copyPicture(p)
    p5 = copyPicture(p)
    for i in getPixels(p1):
        setRed(i,getRed(i))
        setBlue(i,getBlue(i)-25)
        setGreen(i,getGreen(i)-25)
    #like fade to black average values
    #green to blue (0,255,0) (0,125,125) (0,0,255)
