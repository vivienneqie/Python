#Vivienne Qie
#qievi@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.

def machToFPS(m):             #Enter speed in mach
    FPS = m * 1116.4370079
    print(FPS, "feet/second")

def sqPyramidVolume(b, h):    #Enter length (in inches) of one side of the base, enter the height (in inches) of the square pyramid
    volume = (b * b * h) / 3
    print("Volume of the square pyramid is", int(volume), "inches-cubed")

def makeChange(c):            #Enter number of cents as an integer
    dollar = c // 100
    quarter = (c % 100) // 25
    dime = ((c % 100) % 25) // 10
    nickel = ((c % 100) % 25 % 10) // 5
    penny = ((c % 100) % 25 % 10 % 5) // 1
    print(dollar, "dollar(s),", quarter, "quarter(s),", dime, "dime(s),", nickel, "nickel(s) and", penny, "pennies")

def PPIIndex(w, h):           #Enter your weight in pounds, enter your height in inches
    PPI = (w / h) * 1.125
    PPI_round = round(PPI,1)
    print ("Your corrected PPI is {}.".format(PPI_round))