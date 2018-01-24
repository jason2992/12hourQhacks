import math

class scheduleStructure:
    def __init__(self, startTime, endTime, lengthOfHour, days):
        self.startTime = startTime
        self.endTime = endTime
        self.lengthOfHour = lengthOfHour
        self.days = days

def loadCalenderSizes(fileName):
    file = open(fileName, "r")
    
    #data given for calender structure
    days = file.readline()
    startTime = file.readline()
    endTime = file.readline()

    #data to be given
    sTime = startTime.replace("\n", "")
    sTime = sTime.split(":")
    sTime = (int(sTime[0]) * 60) + int(sTime[1])
    eTime = endTime.replace("\n", "")
    eTime = eTime.split(":")
    eTime = (int(eTime[0]) * 60) + int(eTime[1])
    

    dayTime = eTime - sTime
    hour = math.ceil(dayTime / 60)
    lengthOfHour = math.ceil(530 / hour)

    data = scheduleStructure(startTime, endTime, lengthOfHour, days)

    return data

##x = loadCalenderSizes("text")
##print(x.startTime)
##print(x.lengthOfHour)
