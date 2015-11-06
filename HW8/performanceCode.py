#Vivienne Qie, Amy Liu, and Nathan Cheek
#qievi@gatech.edu, aliu66@gatech.edu, and ncheek@gatech.edu
#We worked on the homework assignment together, using only this semester's course materials.

from Myro import *

print("Playing movie.. enjoy!")
for i in range(1,200):
    show(makePicture("output_video_pic_"+str(i)+".jpg"))
    wait(.2)
print("Done!")