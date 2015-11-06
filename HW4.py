#Vivienne Qie
#qievi@gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials.

from Myro import *
init()

def fetch():
    forward(1,4)
    turnLeft(0.5,2.7)
    forward(1,4)

def tailWag():
    turnLeft(1,0.2)
    turnRight(1,0.2)
    turnLeft(1,0.2)
    turnRight(1,0.2)

def figureEight():
    motors(1,0,4)
    motors(0,1,4)

def square():
    forward(0.75, 3)
    turnRight(0.5, 1.35)
    forward(0.75, 3)
    turnRight(0.5, 1.35)
    forward(0.75, 3)
    turnRight(0.5, 1.35)
    forward(0.75, 3)
    turnRight(0.5,1.35)

def tune():
    beep(0.25,660)
    beep(0.25,587)
    beep(0.25,523)
    beep(0.25,587)
    beep(0.25,660)
    beep(0.25,660)
    beep(0.5,660)
    beep(0.25,587)
    beep(0.25,587)
    beep(0.5,587)
    beep(0.25,660)
    beep(0.25,784)
    beep(0.5,784)
    beep(0.25,660)
    beep(0.25,587)
    beep(0.25,523)
    beep(0.25,587)
    beep(0.25,660)
    beep(0.25,660)
    beep(0.25,660)
    beep(0.25,660)
    beep(0.25,587)
    beep(0.25,587)
    beep(0.25,660)
    beep(0.25,587)
    beep(1,523)

def morningRoutine(n):
    if n < 1:
        None
    if n == 1:
        fetch()
    if n == 2:
        fetch()
        tailWag()
    if n == 3:
        fetch()
        tailWag()
        figureEight()
    if n == 4:
        fetch()
        tailWag()
        figureEight()
        square()
    if n >= 5:
        fetch()
        tailWag()
        figureEight()
        square()
        tune()

def harryPotter():
    beep(0.5,493)
    beep(0.75,659)
    beep(0.25,784)
    beep(0.5,740)
    beep(1,659)
    beep(0.5,987)
    beep(1.5,880)
    beep(1.5,740)
    beep(0.75,659)
    beep(0.25,784)
    beep(0.5,740)
    beep(1.25,587)
    beep(0.5,699)
    beep(2.5,493)

def starWars():
    beep(0.5,523)
    beep(0.5,784)
    beep(0.125,699)
    beep(0.125,659)
    beep(0.125,587)
    beep(0.5,1047)
    beep(0.25,784)
    beep(0.125,699)
    beep(0.125,659)
    beep(0.125,587)
    beep(0.5,1047)
    beep(0.25,784)
    beep(0.125,699)
    beep(0.125,659)
    beep(0.125,699)
    beep(0.5,587)

def greetMenu():
    n = askQuestion("Pick a treat:", ["Tiny Treats", "OK Treats", "Jumbo Treats", "Exit"])
    if n == "Tiny Treats":
        fetch()
        tailWag()
        harryPotter()
    if n == "OK Treats":
        fetch()
        tailWag()
        figureEight()
        tune()
    if n == "Jumbo Treats":
        fetch()
        tailWag()
        figureEight()
        square()
        starWars()
    if n == "Exit":
        print("Bye, bye! Have a good day!")