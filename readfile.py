##import qhackclasses
import math
import menu
import qhacks

##mainloop()
class scheduledActivity:

    def __init__(self, name, deadlineDay, deadlineDate, deadlineTime, timeBox, description):
##        self.name = array[0]
##        self.deadline = array[1]
##        self.timeTotal = array[2] #time to be spent on task
##        self.timeLength = array[3] #how long task will be worked on
##        self.description = array[4]
        self.name = name
        self.deadlineDay = deadlineDay
        self.deadlineDate = deadlineDate
        self.deadlineTime = deadlineTime
        self.timeBox = timeBox
##        self.timeTotal = timeTotal #time to be spent on task
##        self.timeLength = timeLength #how long task will be worked on
        self.description = description
        #instiates all the variables availble to class


def clearString(s):
    s = s.replace("\n", "")
    return s

def loadAccountSettings(fileName):
    file = open(fileName, "r")

    #opening a second one so doesn't pass through everything
    f = open(fileName, "r")
    totalLines = sum(1 for line in f)#may need to add a little more depending

    file.readline()#get past days
    file.readline()#get past start time
    file.readline()#get past end time
    #next is info which must be known for event
    

    array = []
    loops = int((totalLines - 3) / 7)

    i = 0
    while i < loops: 
        name = file.readline()
        name = clearString(name); #get rid of \n

    
        #low prioroty for deadline
        deadlineDay = file.readline()
        deadlineDay = clearString(deadlineDay)
        
        deadlineDate = file.readline()
        deadlineDate = clearString(deadlineDate)
        
        deadlineTime = file.readline()
        deadlineTime = clearString(deadlineTime)
        
        timeTotal = file.readline() #in hours
        timeTotal = clearString(timeTotal)

        timeLength = file.readline() #in minutes
        timeLength = clearString(timeLength)

        #for user benefit only
        description = file.readline()
        description = clearString(description)

        #number of each event
        timeBox = (int(timeTotal) * 60) // int(timeLength)
        
        event = scheduledActivity(name, deadlineDay, deadlineDate, deadlineTime, timeBox, description)
        array.append(event)

        i += 1

    file.close()
    return array #returns an array of the events

test = loadAccountSettings("./Users/Tara.txt")
##print(test)
print(test[0].timeBox)
print(test[0].description)

