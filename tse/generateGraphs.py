#Generate graphs from CSV inputimport numpy as np
import math
import pandas as pd
import matplotlib.pyplot as pt
import csv
import numpy as np
from PyQt5 import QtCore
##TKINTER
import tkinter as tk

#global variables
inputFile = "tse/scan_data.csv"


yLKnee = []
yRKnee = []
yLElblow = []
yRElbow = []
yPelvis = []

def setInputFile(file_path):
    global inputFile
    inputFile = file_path

#Knee flexion
def KneeData ():
    x = []
    with open (inputFile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",") 

        ##changes the above lists with CSV values
        for row in plots:
            x.append(row[0])
            yLKnee.append(row[1])
            yRKnee.append(row[4])
    

    ##remove the first value from list (non int value)     
    x.remove(x[0])
    yLKnee.remove(yLKnee[0])
    yRKnee.remove(yRKnee[0])
    
    ##plot graph
    pt.axis([0, 200, 0, 70])
    xInt = [eval(i) for i in x]
    yLKneeInt = [eval(i) for i in yLKnee]
    yRKneeInt = [eval(i) for i in yRKnee]
    
    ##calculate mean, min and max of knee flexion 
    if (np.min(yLKneeInt))<(np.min(yRKneeInt)):
        min = np.min(yLKneeInt)
    else:
        min = np.min(yRKneeInt)
    
    if (np.max(yLKneeInt))>(np.max(yRKneeInt)):
        max = np.max(yLKneeInt)
    else:
        max = np.max(yRKneeInt)
    mean = np.mean(yLKneeInt)

    pt.plot(xInt,yLKneeInt, color = "red", label = "Left Knee")
    pt.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    pt.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    pt.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line
    pt.plot(xInt, yRKneeInt, color = "blue", label = "Right Knee")
    pt.legend(loc="upper left") ##location of key
    pt.savefig("Knee_Flexion.png")
    #pt.show() ## Show graph
    
    
    

    

def elbowData():
    x = []
    with open (inputFile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",")
        for row in plots:
            x.append(row[0])
            yLElblow.append(row[13])
            yRElbow.append(row[16])

    x.remove(x[0])
    yLElblow.remove(yLElblow[0])
    yRElbow.remove(yRElbow[0])

    ##plot graph
    fig, ax = pt.subplots()
    pt.axis([0, 200, 0, 200])
    xInt = [eval(i) for i in x]
    yLElblowInt = [eval(i) for i in yLElblow]
    yRElbowInt = [eval(i) for i in yRElbow]
    ##calculate min mean and max
    if (np.min(yLElblowInt))<(np.min(yRElbowInt)):
        min = np.min(yLElblowInt)
    else:
        min = np.min(yRElbowInt)
    
    if (np.max(yLElblowInt))>(np.max(yRElbowInt)):
        max = np.max(yLElblowInt)
    else:
        max = np.max(yRElbowInt)
    mean = np.mean(yLElblowInt)

    pt.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    pt.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    pt.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line


    pt.plot(xInt,yLElblowInt, color = "red", label = "Left Elbow")
    pt.plot(xInt, yRElbowInt, color = "blue", label = "Right Elbow")
    pt.legend(loc="upper left")
    pt.savefig("Elbow_Flexion")
    #pt.show()

    ##pelvis flexion graphs
def pelvisData():
    x = []
    with open (inputFile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",")
        for row in plots:
            x.append(row[0])
            yPelvis.append(row[36])

    x.remove(x[0])
    yPelvis.remove(yPelvis[0])


    ##plot graph
    fig, ax = pt.subplots()
    pt.axis([0, 200, 0, 15])
    xInt = [eval(i) for i in x]
    yPelvisInt = [eval(i) for i in yPelvis]
    ##calculate min mean and max
    min = np.min(yPelvisInt)
    max = np.max(yPelvisInt)
    mean = np.mean(yPelvisInt)
    pt.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    pt.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    pt.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line

    pt.title("Pelvis Flexion")
    pt.plot(xInt,yPelvisInt, color = "red", label = "Pelvis")
    pt.legend(loc="upper left")
    pt.savefig("Pelvis_Flexion.png")
    #pt.show()





    


KneeData()


elbowData()
#pelvisData()