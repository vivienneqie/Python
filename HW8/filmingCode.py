#Vivienne Qie, Amy Liu, and Nathan Cheek
#qievi@gatech.edu, aliu66@gatech.edu, and ncheek@gatech.edu
#We worked on the homework assignment together, using only this semester's course materials.

from Myro import *
init()

def sceneOne():
    for i in range(1,26):
        p = takePicture()
        savePicture(p, "scene_one_pic" + str(i) + ".jpg")

def sceneTwo():
    for i in range(1,21):
        p = takePicture()
        savePicture(p, "scene_two_pic" + str(i) + ".jpg")

def sceneThree():
    for i in range(1,15):
        p = takePicture()
        savePicture(p, "scene_three_pic" + str(i) + ".jpg")

def sceneFour():
    for i in range(1,17):
        p = takePicture()
        savePicture(p, "scene_four_pic" + str(i) + ".jpg")

def sceneFive():
    for i in range(1,17):
        p = takePicture()
        savePicture(p, "scene_five_pic" + str(i) + ".jpg")