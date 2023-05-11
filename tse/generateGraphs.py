#Generate graphs from CSV inputimport numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import csv
import numpy as np
from PyQt5 import QtCore
import os, sys


#global variables


if hasattr(sys, '_MEIPASS'):
    # PyInstaller creates a temp folder to extract the files.
    # Use the path of the temp folder to locate the pre_data.csv file.
    pre_data_path = os.path.join(sys._MEIPASS, 'tse', 'pre_data.csv')
else:
    # Use the original relative path to locate the pre_data.csv file.
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    pre_data_path = os.path.join(exe_dir, '..', 'tse', 'pre_data.csv')


if hasattr(sys, '_MEIPASS'):
    # PyInstaller creates a temp folder to extract the files.
    # Use the path of the temp folder to locate the pre_data.csv file.
    postDatafile = os.path.join(sys._MEIPASS, 'tse', 'post_data.csv')
else:
    # Use the original relative path to locate the pre_data.csv file.
    exe_dir = os.path.dirname(os.path.abspath(__file__))
    postDatafile = os.path.join(exe_dir, '..', 'tse', 'post_data.csv')





yLKnee = []
yRKnee = []
yLElblow = []
yRElbow = []
yPelvis = []

def setInputFile(file_path):
    global inputFile
    inputFile = file_path

#Knee flexion
def preKneeData ():
    x = []


    
    with open (inputFile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",") 
        header = next(plots)
        right_knee_flexion = header.index("right_knee_flexion_mean")
        left_knee_flexion = header.index("left_knee_flexion_mean")

        ##changes the above lists with CSV values
        for row in plots:
            x.append(row[0])
            yLKnee.append(row[left_knee_flexion])
            yRKnee.append(row[right_knee_flexion])

    

    ##remove the first value from list (non int value)     
    x.remove(x[0])
    yLKnee.remove(yLKnee[0])
    yRKnee.remove(yRKnee[0])
    fig, ax = pt.subplots()

    ##plot graph
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

    ax.plot(xInt,yLKneeInt, color = "red", label = "Left Knee")
    ax.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    ax.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    ax.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line
    ax.set_ylim((min - 5),(max+5))
    ax.set_title("Pre Treatment Knee Flexion")

    ax.plot(xInt, yRKneeInt, color = "blue", label = "Right Knee")
    ax.legend(loc="upper left") ##location of key
    pt.savefig("Pre_Knee_Flexion.png")
    pt.show() ## Show graph
    
    
    

    

def preelbowData():
    x = []
    with open (inputFile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",")
        header = next(plots)
        right_elbow_flexion = header.index("right_elbow_flexion_mean")
        left_elbow_flexion = header.index("left_elbow_flexion_mean")
        for row in plots:
            x.append(row[0])
            yLElblow.append(row[left_elbow_flexion])
            yRElbow.append(row[right_elbow_flexion])

    x.remove(x[0])
    yLElblow.remove(yLElblow[0])
    yRElbow.remove(yRElbow[0])

    ##plot graph
    fig, ax = pt.subplots()
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

    ax.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    ax.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    ax.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line
    ax.set_ylim((min - 5),(max+5))

    ax.set_title("Pre Treatment Elbow Flexion")
    ax.plot(xInt,yLElblowInt, color = "red", label = "Left Elbow")
    ax.plot(xInt, yRElbowInt, color = "blue", label = "Right Elbow")
    ax.legend(loc="upper left")
    pt.savefig("Pre_Elbow_Flexion")
    pt.show()

    ##pelvis flexion graphs
def prepelvisData():
    x = []
    with open (inputFile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",")
        header = next(plots)
        pelvis_flexion = header.index("pelvis_flexion_mean")
        for row in plots:
            x.append(row[0])
            yPelvis.append(row[pelvis_flexion])

    x.remove(x[0])
    yPelvis.remove(yPelvis[0])


    ##plot graph
    fig, ax = pt.subplots()
    xInt = [eval(i) for i in x]
    yPelvisInt = [eval(i) for i in yPelvis]
    ##calculate min mean and max
    min = np.min(yPelvisInt)
    max = np.max(yPelvisInt)
    mean = np.mean(yPelvisInt)
    ax.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    ax.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    ax.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line
    ax.set_ylim((min - 5),(max+5))

    ax.set_title("Pre Treatment Pelvis Flexion")
    ax.plot(xInt,yPelvisInt, color = "red", label = "Pelvis")
    ax.legend(loc="upper left")
    pt.savefig("Pre_Pelvis_Flexion.png")
    pt.show()



    ##pelvis flexion graphs
def PostpelvisData():
    x = []
    with open (postDatafile, "r") as dataSet:
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
    ax.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    ax.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    ax.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line
    ax.set_ylim((min - 5),(max+5))
    ax.set_title("Post Treatment Pelvis Flexion")
    ax.plot(xInt,yPelvisInt, color = "red", label = "Pelvis")
    ax.legend(loc="upper left")
    pt.savefig("Post_Pelvis_Flexion.png")
    pt.show()






#Knee flexion
def PostKneeData ():
    x = []
    with open (postDatafile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",") 
        header = next(plots)
        right_knee_flexion = header.index("right_knee_flexion_mean")
        left_knee_flexion = header.index("left_knee_flexion_mean")

        ##changes the above lists with CSV values
        for row in plots:
            x.append(row[0])
            yLKnee.append(row[left_knee_flexion])
            yRKnee.append(row[right_knee_flexion])
    

    ##remove the first value from list (non int value)     
    x.remove(x[0])
    yLKnee.remove(yLKnee[0])
    yRKnee.remove(yRKnee[0])
    fig, ax = pt.subplots()

    
    ##plot graph
    
    xInt = [eval(i) for i in x]
    yLKneeInt = [eval(i) for i in yLKnee]
    yRKneeInt = [eval(i) for i in yRKnee]
    
    x = range(len(yLKneeInt))
    yLKneeInt = yLKneeInt[:len(x)]


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


    ax.plot(xInt,yLKneeInt, color = "red", label = "Left Knee")
    ax.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    ax.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    ax.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line
    ax.set_ylim((min - 5),(max+5))
    ax.set_title("Post Treatment Knee Flexion")
    ax.plot(xInt, yRKneeInt, color = "blue", label = "Right Knee")
    ax.legend(loc="upper left") ##location of key
    pt.savefig("Post_Knee_Flexion.png")
    pt.show() ## Show graph








def PostElbowData():
    x = []
    with open (postDatafile, "r") as dataSet:
        plots = csv.reader(dataSet, delimiter=",")
        header = next(plots)
        right_elbow_flexion = header.index("right_elbow_flexion_mean")
        left_elbow_flexion = header.index("left_elbow_flexion_mean")
        for row in plots:
            x.append(row[0])
            yLElblow.append(row[left_elbow_flexion])
            yRElbow.append(row[right_elbow_flexion])

    x.remove(x[0])
    yLElblow.remove(yLElblow[0])
    yRElbow.remove(yRElbow[0])

    ##plot graph
    fig, ax = pt.subplots()
    
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

    ax.axhline(mean, color='green', linestyle='--', label='Mean')  ## add mean line
    ax.axhline(min, color='black', linestyle='--', label='Minimum')  ## add minimum line
    ax.axhline(max, color='purple', linestyle='--', label='Maximum')  ## add maximum line
    ax.set_ylim((min - 5),(max+5))
    ax.set_title("Post Treatment Elbow Flexion")

    ax.plot(xInt,yLElblowInt, color = "red", label = "Left Elbow")
    ax.plot(xInt, yRElbowInt, color = "blue", label = "Right Elbow")
    ax.legend(loc="upper left")
    pt.savefig("Post_Elbow_Flexion")
    pt.show()




def compareData():
     pre_data = pd.read_csv(pre_data_path)
     post_data = pd.read_csv(postDatafile)
     
     #Lknee Diff
     pre_Lknee_flexion = pre_data["left_knee_flexion_mean"]
     post_Lknee_flexion = post_data["left_knee_flexion_mean"]

     #Rknee Diff
     pre_Rknee_flexion = pre_data["right_knee_flexion_mean"]
     post_Rknee_flexion = post_data["right_knee_flexion_mean"]

     #LElbow Diff
     pre_LElbow_flexion = pre_data["left_elbow_flexion_mean"]
     post_LElbow_flexion = post_data["left_elbow_flexion_mean"]

     #RElbow Diff
     pre_RElbow_flexion = pre_data["right_elbow_flexion_mean"]
     post_RElbow_flexion = post_data["right_elbow_flexion_mean"]

     #Pelvis Diff
     pre_Pelvis_flexion = pre_data["pelvis_flexion_mean"]
     post_Pelvis_flexion = post_data["pelvis_flexion_mean"]


     LKneediff = abs((pre_Lknee_flexion.mean() - post_Lknee_flexion.mean()) / pre_Lknee_flexion.mean()) * 100
     RKneediff = abs((pre_Rknee_flexion.mean() - post_Rknee_flexion.mean()) / pre_Rknee_flexion.mean()) * 100

     LElbowdiff = abs((pre_LElbow_flexion.mean() - post_LElbow_flexion.mean()) / pre_LElbow_flexion.mean()) * 100
     RElbowdiff = abs((pre_RElbow_flexion.mean() - post_RElbow_flexion.mean()) / pre_RElbow_flexion.mean()) * 100

     Pelvisdiff = abs((pre_Pelvis_flexion.mean() - post_Pelvis_flexion.mean()) / pre_Pelvis_flexion.mean()) * 100

     print ("Left Knee Difference: "+ str(LKneediff))
     print ("Right Knee Difference: "+ str(RKneediff))
     print("Right Elbow diff: "+ str(RElbowdiff))
     print("Left Elbow diff: "+ str(LElbowdiff))
     print("Pelvis diff: "+ str(Pelvisdiff))


    

     return pre_data, post_data, pre_Lknee_flexion.mean(), post_Lknee_flexion.mean(), pre_Rknee_flexion.mean(), post_Rknee_flexion.mean(), pre_LElbow_flexion.mean(), post_LElbow_flexion.mean(), pre_RElbow_flexion.mean(), post_RElbow_flexion.mean(), pre_Pelvis_flexion.mean(), post_Pelvis_flexion.mean(), LKneediff, RKneediff, LElbowdiff, RElbowdiff, Pelvisdiff


compareData()



