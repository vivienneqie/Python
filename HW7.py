#Vivienne Qie and Nihar Kandimalla
#qievi@gatech.edu and nkandimalla3@gatech.edu
#We worked on the homework assignment together, using only this semester's course materials.

from Myro import *
setPicSize("small")

def seeingRed(): #15
    p = takePicture()
    p1 = copyPicture(p)
    for i in getPixels(p):
        r = getRed(i)
        b = getBlue(i)
        g = getGreen(i)
        setRed(i, r+40)
        setBlue(i, b-40)
        setGreen(i, g-40)
    savePicture(p, "seeing-red.jpg")
    savePicture(p1, "before.jpg")

def fade(): #35
    pic1 = takePicture()
    pic2 = takePicture()
    pic3 = takePicture()
    pic4 = takePicture()
    pic5 = takePicture()
    pic6 = takePicture()
    pic7 = takePicture()
    pic8 = takePicture()
    pic9 = takePicture()
    pic10 = takePicture()
    pic11 = takePicture()
    pic12 = takePicture()
    for i in getPixels(pic2):
        setRed(i,getRed(i)-25)
        setBlue(i,getBlue(i)-25)
        setGreen(i,getGreen(i)-25)
    for i in getPixels(pic3):
        setRed(i,getRed(i)-50)
        setBlue(i,getBlue(i)-50)
        setGreen(i,getGreen(i)-50)
    for i in getPixels(pic4):
        setRed(i,getRed(i)-75)
        setBlue(i,getBlue(i)-75)
        setGreen(i,getGreen(i)-75)
    for i in getPixels(pic5):
        setRed(i,getRed(i)-100)
        setBlue(i,getBlue(i)-100)
        setGreen(i,getGreen(i)-100)
    for i in getPixels(pic6):
        setRed(i,getRed(i)-125)
        setBlue(i,getBlue(i)-125)
        setGreen(i,getGreen(i)-125)
    for i in getPixels(pic7):
        setRed(i,getRed(i)-150)
        setBlue(i,getBlue(i)-150)
        setGreen(i,getGreen(i)-150)
    for i in getPixels(pic8):
        setRed(i,getRed(i)-175)
        setBlue(i,getBlue(i)-175)
        setGreen(i,getGreen(i)-175)
    for i in getPixels(pic9):
        setRed(i,getRed(i)-200)
        setBlue(i,getBlue(i)-200)
        setGreen(i,getGreen(i)-200)
    for i in getPixels(pic10):
        setRed(i,0)
        setBlue(i,0)
        setGreen(i,0)
    for i in getPixels(pic11):
        setRed(i,0)
        setBlue(i,0)
        setGreen(i,0)
    for i in getPixels(pic12):
        setRed(i,0)
        setBlue(i,0)
        setGreen(i,0)
    savePicture([pic1,pic2,pic3,pic4,pic5,pic6,pic7,pic8,pic9,pic10,pic11,pic12], "fade.gif")

def overlay(): #35
    p = takePicture()
    h = getHeight(p)
    w = getWidth(p)
    for x in range(50,100):
        for y in range(100,120):
            pix = getPixel(p,x,y)
            setRed(pix,255)
            setGreen(pix,0)
            setBlue(pix,255)
    for x in range(65,85):
        for y in range(120,180):
            pix = getPixel(p,x,y)
            setRed(pix,255)
            setGreen(pix,0)
            setBlue(pix,255)
    savePicture(p, "overlay.jpg")

def splitScreen(): #40
    pic1 = takePicture()
    turnRight(1,1)
    pic2 = takePicture()
    height1 = getHeight(pic1)
    height2 = getHeight(pic2)
    width1 = getWidth(pic1)
    width2 = getWidth(pic2)
    for y in range(int(height1/2),height1):
        for x in range(0,width1):
            pixels1 = getPixel(pic1,x,y)
            pixels2 = getPixel(pic2,x,y)
            setRed(pixels1,getRed(pixels2))
            setGreen(pixels1,getRed(pixels2))
            setBlue(pixels1,getBlue(pixels2))
    savePicture(pic1,"SplitScreen.jpg")

def lensFlare(): #20
    b = takePicture()
    pix = getPixels(b)
    for i in pix:
        x = getX(i)
        y = getY(i)
        if 150 < x < 200 and  100 < y < 150:
            setRGB(i,255,255,255)
    savePicture(b,"lens-flare.jpg")

def greenScreen(): #50
    pic1 = makePicture("foreground.jpg")
    pic2 = makePicture("background.jpg")
    pix1 = getPixels(pic1)
    for i in pix1:
        r,g,b = getRGB(i)
        if g > r and g > b:
            x = getX(i)
            y = getY(i)
            pix2 = getPixel(pic2,x,y)
            setRed(i,getRed(pix2))
            setGreen(i,getGreen(pix2))
            setBlue(i,getBlue(pix2))
    savePicture(pic1,"GreenScreen.jpg")