#Tithi Raval and Vivienne Qie
#tithi.raval@gatech.edu and qievi@gatech.edu
#We worked on the homework assignment alone, using only this semester's course materials.
import math
def quesoForFishy(x):
    quesoJarsdec = x/2.98
    quesoJarsint = int(quesoJarsdec)
    return quesoJarsint

def mailboxes(x):
    lifeSpan = x*2
    lifeSpan1 = x*6
    print("Because you have run into", x, "mailbox(es), your car's life has been shortened by anywhere from", lifeSpan, "to", lifeSpan1, "months.")

def concertTicket():
    x = input ("Ticket price?")
    y = input ("Hourly rate?")
    hoursOfwork = float(x)/ float(y)
    print ("You need to work {:.2f} hours to buy your ticket.".format(hoursOfwork))

def boringInterlude(r):
    Volume = (4/3) * math.pi * float(r)**3
    volumeCubicFeet = Volume / (12**3)
    return(float(volumeCubicFeet))

def trafficJam(x, y):
    lanes = int(x)
    milesTraffic = float(y)
    feetTraffic = milesTraffic * 5280
    cars = feetTraffic/15
    totalTraffic = cars * lanes
    return (float(totalTraffic))

def timeLeft(x):
    batteryLife = input ("Number of hours the flashlight battery lasts?")
    bLminutes = float (batteryLife)*60
    percentageUsed = (int(x)/ bLminutes) * 100
    percentageRemaining = 100 - float(percentageUsed)
    print(int(percentageRemaining))
    bLRemaining = bLminutes - int (x)
    return (float(bLRemaining))

def daffodils(x, y, z):
    Dozens = math.ceil(int(x) / 12)
    totalCost = Dozens * float(z)
    costRemaining = totalCost - float(y)
    print("You will need to contribute ${:.2f}.". format (costRemaining))