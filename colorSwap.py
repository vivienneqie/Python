from Myro import *

def colorSwap():
    p = makePicture("RA_colorswap_source.jpg")
    for i in getPixels(p):
        r = getRed(i)
        g = getGreen(i)
        b = getBlue(i)
        if r > g and r > b:
            setGreen(i, 255)
            setRed(i, 0)
            setBlue(i, 0)
        elif g > r and g > b:
            setBlue(i, 255)
            setGreen(i, 0)
            setRed(i, 0)
        elif b > r and b > g:
            setRed(i, 255)
            setGreen(i, 0)
            setBlue(i, 0)
        elif r == 255 and g == 255 and b == 255:
            setRed(i,255)
            setGreen(i, 255)
            setBlue(i, 255)
        elif r < g < b:
            setRed(i,r)
            setGreen(i,g)
            setBlue(i,b)
    show(p)
    savePicture(p, "RA_colorswap_source.jpg")
