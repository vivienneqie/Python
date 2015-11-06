#Tithi Raval and Vivienne Qie
#tithi.raval@gatech.edu and qievi@gatech.edu
#We worked on the homework assignment together, using only this semester's course materials.

from Graphics import *
from Myro import *

win = Window("robot", 500, 500)
win.mode = "manual"

f = open("myMovements.txt", "w")
f.close()
def handleKeyRelease(win, event):
    f = open("myMovements.txt", "a")
    sensorValue = getLight("left") / ( getLight("right") + getObstacle("right") )
    if event.key == "Up":
        forward(1,0.1)
        f.write("forward .1" + " " + str(sensorValue) + "\n")
    if event.key == "Down":
        backward(1,0.1)
        f.write("backward .1" + " " + str(sensorValue) + "\n")
    if event.key == "Left":
        turnLeft(1,0.1)
        f.write("turnLeft .1" + " " + str(sensorValue) + "\n")
    if event.key == "Right":
        turnRight(1,0.1)
        f.write("turnRight .1" + " " + str(sensorValue) + "\n")
    if event.key == "b":
        beep(0.1,800)
        f.write("beep .1" + "\n")
    f.close()

onKeyPress(handleKeyRelease)

def collectData(myFile, direction):
    if myFile == "myMovements.txt":
        f = open("myMovements.txt", "r")
        contents = f.read()
        f.close()
    x = sum(1 for line in open('myMovements.txt'))
    y = contents.count("beep")
    if direction == "forward":
        z = contents.count("forward")
    if direction == "backward":
        z = contents.count("backward")
    if direction == "left":
        z = contents.count("turnLeft")
    if direction == "right":
        z = contents.count("turnRight")
    return(print("The robot traveled for", (x-y)*0.1, "seconds total, beeping", y, "times. This robot moved", direction, "a total of", z, "times."))

def replay(fileName):
    f = open(fileName, "r")
    for line in f:
        if "forward" in line:
            forward (1, 0.1)
        if "backward" in line:
            backward(1, 0.1)
        if "turnRight" in line:
            turnRight(1, 0.1)
        if "turnLeft" in line:
            turnLeft(1, 0.1)
        if "beep" in line:
            beep(0.1, 800)
f.close()