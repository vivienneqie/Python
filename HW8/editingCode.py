#Vivienne Qie, Amy Liu, and Nathan Cheek
#qievi@gatech.edu, aliu66@gatech.edu, and ncheek@gatech.edu
#We worked on the homework assignment together, using only this semester's course materials.

from Myro import *

"""
masterList is a list of all the frames and it is used to output the final frame list (or gif).
If a picture is modified, append the picture object to the list
Otherwise just append the filename as a string and it will be taken care of (instead of having it in memory throughout the program)
"""
masterList = []
currentFrameNum = 1 #Set the frame counter to 1

def framePush(imgIn, numFrames, backgroundRGB = (0,0,0)):
  global currentFrameNum

  if type(imgIn) == type(""): #This part allows it to accept a string filename or a picture object
      pic = makePicture(imgIn)
  else:
      pic = copyPicture(imgIn)
  returnList = []
  picSize = (getWidth(pic), getHeight(pic))

  returnList.append(pic)#Makes first frame same as pic
  numFrames += -1

  for i in range(numFrames):
    print("Creating frame", currentFrameNum, "(using framePush)")
    currentFrameNum += 1
    newPic = makePicture(picSize[0], picSize[1], makeColor(backgroundRGB[0],backgroundRGB[1],backgroundRGB[2]))
    offset = (((i+1)*picSize[0]/numFrames),0)
    print("Offset is",offset)
    pixelLocationsNew = []
    for j in range(picSize[0]):
      for k in range(picSize[1]):
        newPixel = (j+offset[0],k+offset[1]) #New background picture to be filled with part of imgIn
        if (newPixel[0] >= 0 and newPixel[0] < picSize[0]) and (newPixel[1] >= 0 and newPixel[1] < picSize[1]): #If it's within the picture
          pixel1 = getPixel(newPic, newPixel[0], newPixel[1])
          pixel2 = getPixel(pic, j, k)
          pix2R, pix2G, pix2B = getRGB(pixel2) #Get rgb values from pixel2 and overwrite pixel1
          setRed(pixel1, pix2R)
          setGreen(pixel1, pix2G)
          setBlue(pixel1, pix2B)
    returnList.append(newPic)
  return returnList


def screenShake(imgFilename, numFrames, backgroundRGB = (0,0,0)): #Parameters: image, number of frames to return, optional background color as rgb tuple
  global currentFrameNum

  if type(imgFilename) != type(""): #Make sure imgFilename is a string
    print("Error! imgFilename must be a string")
    return

  imgIn = makePicture(imgFilename)
  picSize = (getWidth(imgIn), getHeight(imgIn))
  pixelLocations = []
  for j in range(picSize[0]):
    for k in range(picSize[1]):
      pixelLocations.append((j,k))
  i = numFrames
  returnList = []
  if i > 0: #Makes first frame same as imgIn
    returnList.append(imgIn)
    i += -1
  while i > 0:
    print("Creating frame", currentFrameNum, "(using screenShake)")
    currentFrameNum += 1
    newPic = makePicture(picSize[0], picSize[1], makeColor(backgroundRGB[0],backgroundRGB[1],backgroundRGB[2]))
    offset = (randint(int(-picSize[0]/12),int(picSize[0]/12)), randint(int(-picSize[1]/12),int(picSize[1]/12)))
    print("Offset is",offset)
    pixelLocationsNew = []
    for j in range(picSize[0]):
      for k in range(picSize[1]):
        newPixel = (j+offset[0],k+offset[1]) #New background picture to be filled with part of imgIn
        if (newPixel[0] >= 0 and newPixel[0] < picSize[0]) and (newPixel[1] >= 0 and newPixel[1] < picSize[1]): #If it's within the picture
          pixel1 = getPixel(newPic, newPixel[0], newPixel[1])
          pixel2 = getPixel(imgIn, j, k)
          pix2R, pix2G, pix2B = getRGB(pixel2) #Get rgb values from pixel2 and overwrite pixel1
          setRed(pixel1, pix2R)
          setGreen(pixel1, pix2G)
          setBlue(pixel1, pix2B)
    returnList.append(newPic)
    i += -1
  print("Done screen shake")
  return returnList

def seeingRed(a,dontCount = 0):
    global currentFrameNum
    p = makePicture(a)
    p1 = copyPicture(p)
    print("Creating frame", currentFrameNum, "(using seeingRed)")
    if dontCount == 0: #Default increment frame counter (don't when combining with another effect)
        currentFrameNum += 1
    for i in getPixels(p):
        r = getRed(i)
        b = getBlue(i)
        g = getGreen(i)
        setRed(i, r+40)
        setBlue(i, b-40)
        setGreen(i, g-40)
    return p

def splitScreen(pic1, pic2):
    global currentFrameNum
    pic1 = makePicture(pic1)
    pic2 = makePicture(pic2)
    height1 = getHeight(pic1)
    height2 = getHeight(pic2)
    width1 = getWidth(pic1)
    width2 = getWidth(pic2)
    print("Creating frame", currentFrameNum, "(using splitScreen)")
    currentFrameNum += 1
    for y in range(int(height1/2),height1):
        for x in range(0,width1):
            pixels1 = getPixel(pic1,x,y)
            pixels2 = getPixel(pic2,x,y-height1/2)
            setRed(pixels1,getRed(pixels2))
            setGreen(pixels1,getGreen(pixels2))
            setBlue(pixels1,getBlue(pixels2))
    return pic1

def fade(picture):
    global currentFrameNum
    if type(picture) == type(""): #This part allows it to accept a string filename or a picture object
        pic = makePicture(picture)
    else:
        pic = copyPicture(picture)
    picList = []
    for i in range(10):
        print("Creating frame", currentFrameNum, "(using fade)")
        currentFrameNum += 1
        for pixel in getPixels(pic):
            r, g, b = getRGB(pixel)
            if r >= 0:
                setRed(pixel, (r - i*5))
            else:
                setRed(pixel, 0)
            if g >= 0:
                setGreen(pixel, (g - i*5))
            else:
                setGreen(pixel, 0)
            if b >= 0:
                setBlue(pixel, (b - i*5))
            else:
                setBlue(pixel, 0)
        picList.append(pic)
        pic = copyPicture(pic)
    return picList


def listPicNames(prefix,numPics):#Returns a list of picture names
    nameList = []
    for i in range(1,numPics+1):
        nameList.append(prefix+str(i)+".jpg")
    return nameList

#Scene one
print("Creating Scene 1")
#Load filenames into list
scene1Names = listPicNames("scene_one_pic",25)
#Fade in
tempList = fade(scene1Names[0])
tempList.reverse()#Reverse to fade IN
masterList += tempList
#Loop through the rest
for i in scene1Names[1:-1]:
    print("Appending frame", currentFrameNum, "(no change)")
    currentFrameNum += 1
    masterList.append(i)
#Fade out
masterList += fade(scene1Names[-1])

#Scene two
print("Creating Scene 2")
#Load filenames into list
scene2Names = listPicNames("scene_two_pic",20)
tempList = fade(scene2Names[0])
tempList.reverse()#Reverse to fade IN
masterList += tempList
#Loop till frame 17
for i in scene2Names[1:16]:
    print("Appending frame", currentFrameNum, "(no change)")
    currentFrameNum += 1
    masterList.append(i)
#Do 17th frame
masterList += screenShake(scene2Names[16],12)
#Loop through the rest
for i in scene2Names[17:]:
    print("Appending frame", currentFrameNum, "(no change)")
    currentFrameNum += 1
    masterList.append(i)
#Fade out
masterList += fade(scene2Names[-1])

#Scene three
print("Creating Scene 3")
#Load filenames into list
scene3Names = listPicNames("scene_three_pic",14)
tempList = fade(seeingRed(scene3Names[0],1))
tempList.reverse()#Reverse to fade IN
masterList += tempList
#Loop through the rest
for i in scene3Names:
    masterList.append(seeingRed(i))
#Fade out
masterList += fade(seeingRed(scene3Names[-1],1))

#Scene four
print("Creating Scene 4")
#Load filenames into list
scene4Names = listPicNames("scene_four_pic",16)
tempList = fade(seeingRed(scene4Names[0]))
tempList.reverse()#Reverse to fade IN
masterList += tempList
#Loop through the rest
for i in scene4Names:
    masterList.append(seeingRed(i))
#Fade out
masterList += fade(seeingRed(scene4Names[-1],1))

#Scene five
print("Creating Scene 5")
#Load filenames into list
scene5Names = listPicNames("scene_five_pic",16)
tempList = fade(seeingRed(scene5Names[0]))
tempList.reverse()#Reverse to fade IN
masterList += tempList
#Loop through the rest
for i in scene5Names:
    masterList.append(seeingRed(i))
#Fade out
masterList += framePush(seeingRed(scene5Names[-1],1),10)

"""
Here we give two options: does the user want to save each frame as a jpg or a create a single gif?
"""
def createFrames():
    #Almost done!
    #go through masterList and save new set of images
    masterListLen = len(masterList) #Setting it here for quicker reusability
    for i in range(masterListLen):
        percent = str((i*100)/masterListLen)#For printing progress
        item = masterList[i]
        filename = "output_video_pic_"+str(i+1)+".jpg"
        if type(item) == type(""):#If its a string copy the original picture
            tempPic = makePicture(item)
            print("Saving",filename,"- total progress:",percent+"%")
            savePicture(tempPic,filename)
        else:#If its a picture object save it to disk
            print("Saving",filename,"- total progress:",percent+"%")
            savePicture(item,filename)
    print("Done! - total progress: 100%")

def createGif():
    #Almost done!
    #go through masterList and save new set of images
    masterListLen = len(masterList) #Setting it here for quicker reusability
    gifList = []
    for i in range(masterListLen):
        percent = str((i*100)/masterListLen)#For printing progress
        item = masterList[i]
        if type(item) == type(""):
            print("Loading frame",str(i+1),"- total progress:",percent+"%")
            gifList.append(makePicture(item))
        else:
            print("Loading frame",str(i+1),"- total progress:",percent+"%")
            gifList.append(item)
    print("Saving to file")
    savePicture(gifList,"output_video.gif")
    print("Done! - total progress: 100%")

#Ask the user what kind of output they want
outputValid = False
while outputValid == False:
    outputType = input("What type of output would you like? (enter number)\n1. JPG of each frame\n2. GIF of entire film (note this will be take much longer):")
    if outputType == "1":
        outputValid = True
        createFrames()
    elif outputType == "2":
        outputValid = True
        createGif()
print("Program is complete")
