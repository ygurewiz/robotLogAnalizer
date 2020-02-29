import robotLogKeyWords
import re
import string
import datetime
from pathlib import Path
import sys
import csv
import os
import pandas as pd
from robotLogKeyWords import rDirection

def robotLogAnalizer(argv):

    if(len(argv)<2):
        print("Input file Directory:")
        inputDir = input()
        print("Input file")
        robotile = input()
    else:
        inputDir = argv[1]
        rFile = argv[2]
        
    #open input file
    try:
        rFile = open(inputDir+'\\'+rFile,'r')
    except IOError: 
           print ("Log File: File does not appear to exist.")
           return
    outputfileName = str.replace(rFile.name,'.log','_PARSED.log')
    outputFile = open(outputfileName,'w+')

    lines = rFile.readlines()
    DirectionList = list()

    robotLineAnalizer(lines,DirectionList,outputFile)

    outputFile.write("\n\nPath:\n")
    for d in DirectionList:
        outputFile.write(str(d).strip()+'\n')
    rFile.close()
    outputFile.close()

def robotLineAnalizer(lines,DirectionList,outputFile):
    i=0
    currentDirection = ""
    reverse = False
    for line in lines:
        i+=1
        timeStamp = getTimeStamp(line,i)
        outLine = robotLogLineAnalizer(line,i)
        if(not outLine == ""):
            outputFile.write(str(i)+' '+outLine)
            if(not str.find(outLine,"LOG_MOVEMENT_REVERSE_MOVEMENT_START")==-1):
                reverse=True
        #else:
            #outputFile.write('\n')
            #print(line)
        direction = getRobotHDirection(line,i)
        if(not direction==""):
            currentDirection = direction
        if(not currentDirection==""):
            distance = getRobotDistanceTraveled(line,i)
            if(distance):
                if(reverse):
                    reverse=False
                    go = 'R'
                else:
                    go = 'F'
                RDirection = rDirection(timeStamp,go,currentDirection,float(distance[0])/10,float(distance[1])/10)
                DirectionList.insert(-1,RDirection)
                #DirectionList.insert(-1,str(i) + go+" current direction: "+currentDirection+" Left Encoder: " + distance[0] + " Right Encoder: " + distance[1])
    

def getRobotHDirection(line,i):
    for key in robotLogKeyWords.HorizontalDirection:
        if(not str.find(line,key)==-1):
            return key
    return ""

def getRobotDistanceTraveled(line,i):
    dis=  None
    if(not str.find(line,"(millimeter)")==-1):
        dis = str.split(line,"(millimeter)")
        leftDis = str.split(str.split(dis[1],',')[0],' ')[1].strip()
        rightDis = str.split(str.split(dis[2],'\n')[0],' ')[1].strip()
        return [leftDis,rightDis]
    return dis

def robotLogLineAnalizer(line,i):
    for key in robotLogKeyWords.KeyWords:
        if(not str.find(line,key)==-1):
            return line
    for key in robotLogKeyWords.HorizontalDirection:
        if(not str.find(line,key)==-1):
            return line
    for key in robotLogKeyWords.Rotation:
        if(not str.find(line,key)==-1):
            print(line)
            return line
    return ""

def main():
    robotLogAnalizer(sys.argv)

def getTimeStamp(line,i):
    ############
    #DATE + TIME
    timestamp = str.split(line," ")
    date = str.split(timestamp[0],"-")
    #TIME
    time = str.split(timestamp[1],":")
    microseconds = timestamp[2]
    theTime = datetime.datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]),int(time[1]),int(time[2]),int(microseconds))
    timeStamp = str(theTime.strftime("%b-%d-%Y %H:%M:%S")).strip()
    ##########
    return timeStamp



if __name__=="__main__":
    main()
