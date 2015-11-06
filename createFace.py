#Vivienne Qie
#qievi@gatech.edu
#I worked on this homework assignment alone, using only this semester's course materials.

from Graphics import *
win = Window()

head = Circle(Point(150, 150), 125)
head.draw(win)
head.setFill(makeColor(255, 235, 205))

eye_1 = Oval(Point(100, 120), 30, 20)
eye_1.draw(win)
eye_1.setFill(makeColor(255, 255, 255))

pupil_1 = Circle(Point(100, 120), 17)
pupil_1.draw(win)
pupil_1.setFill(makeColor(139, 69, 19))

eye_2 = Oval(Point(200, 120), 30, 20)
eye_2.draw(win)
eye_2.setFill(makeColor(255, 255, 255))

pupil_2 = Circle(Point(200, 120), 17)
pupil_2.draw(win)
pupil_2.setFill(makeColor(139, 69, 19))

mouth = Oval(Point(150,210), 50, 15)
mouth.draw(win)
mouth.setFill(makeColor(240, 128, 128))

mouth_line = Line((100,210), (200,210))
mouth_line.draw(win)

nose_1 = Line((160, 140), (140, 180))
nose_1.draw(win)

nose_2 = Line((140, 180), (160, 180))
nose_2.draw(win)

hat_1 = Oval(Point(150, 50), 100, 20)
hat_1.draw(win)
hat_1.setFill(makeColor(184, 134, 11))

hat_2 = Rectangle(Point(70, 1),Point(230, 50))
hat_2.draw(win)
hat_2.setFill(makeColor(184, 134, 11))
hat_2.outline=makeColor(184, 134, 11)

hat_3 = Text(Point(150, 25), "Georgia Tech!")
hat_3.draw(win)
hat_3.setFill(makeColor(0, 0, 128))

name = Text(Point(150, 290), "Vivienne Qie")
name.draw(win)