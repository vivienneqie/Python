#Tithi Raval and Vivienne Qie
#tithi.raval@gatech.edu and qievi@gatech.edu
#We worked on the homework assignment together, using only this semester's course materials.

from Myro import *
init()

def celebration():
    beep(0.7, 740)
    beep(0.35, 698)
    beep(0.35, 740)
    beep(0.35, 698)
    beep(0.35, 622)
    beep(0.185, 830)
    beep(0.185, 830)
    motors(1,0,4)

def avoidWalls():
    for seconds in timer(60):
        while getIR() == [1,1]:
            backward(1/3)
        while getIR() == [1,0]:
            turnLeft(1/3)
            backward(1/3)
        while getIR() == [0,1]:
            turnRight(1/3)
            backward(1/3)
        while getIR() == [0,0]:
            forward(1/3)
            turnRight(0.5, 1/3)
    stop()
    celebration()
