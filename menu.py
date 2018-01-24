from tkinter import *
import os

class requirementTaken: #forth window
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.geometry('250x80')
        top.grab_set() #gives the window a forced focus
        
        Label(top, text="UserName already taken", font=(None, 15)).grid(row=1)
        
        b = Button(top, text="ok", command=self.ok, font=(None, 15), height = 1, width = 10)
        b.grid(row=2)
    def ok(self):
        self.top.grab_release()
        self.top.destroy()
        
class requirementFailed: #third window
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.geometry('200x80')
        top.grab_set() #gives the window a forced focus
        
        Label(top, text="Invalid Username", font=(None, 15)).grid(row=1)
        
        b = Button(top, text="ok", command=self.ok, font=(None, 15), height = 1, width = 10)
        b.grid(row=2)
    def ok(self):
        self.top.grab_release()
        self.top.destroy()
        
class createNewTitle: #second window
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.parent = parent #REMEMBERS PARENT, THATS SO HELPFUL REMEMBER THIS SHIT
        top.geometry('500x170')
        top.grab_set() #gives the window a forced focus

        #username input slot
        Label(top, text="Username", font=(None, 15)).grid(row=0, column=0)
        self.userName = Entry(top,width=50)
        self.userName.grid(row=0, column=1)

        #days input slot
        Label(top, text="Days", font=(None, 15)).grid(row=1, column=0)
        self.deadline = Entry(top,width=50)
        self.deadline.grid(row=1, column=1)

        #days input slot
        Label(top, text="Day start(E.g. 8:30):", font=(None, 15)).grid(row=2, column=0)
        self.startTime = Entry(top,width=50)
        self.startTime.grid(row=2, column=1)

        #days input slot
        Label(top, text="Day End(E.g. 22:30):", font=(None, 15)).grid(row=3, column=0)
        self.endTime = Entry(top,width=50)
        self.endTime.grid(row=3, column=1)

        b = Button(top, text="confirm", command=self.confirm, font=(None, 15), width = 5)
        b.grid(row=4,column=0)

        b = Button(top, text="cancel", command=self.cancel, font=(None, 15), width = 5)
        b.grid(row=4,column=1)

    def confirm(self):
        #file does not exist, popup error
        if os.path.isfile(self.userName.get()+".txt"):
            emptyInput = requirementTaken(self.top)

        elif self.userName.get() == "":
            emptyInput = requirementFailed(self.top)
            
        else:
            if not os.path.exists("./Users"):
                os.makedirs("./Users")
            f = open("./Users/" + self.userName.get() + ".txt","w+") # writes a new user file
            #f.write(self.userName.get()+"\n")  
            f.write(self.deadline.get()+"\n") 
            f.write(self.startTime.get()+"\n") 
            f.write(self.endTime.get()+"\n") 
            f.close()    

            f = open("userNames.txt","a") #adds new user into the list of users
            f.write(self.userName.get() + "\n")  
            f.close()
            
            f = open ("userNameChosen.txt","w+") #becomes the new focus file
            f.write (self.userName.get()+"\n")
            f.close()
            
            self.top.grab_release() #releases forced focus
            self.top.parent.destroy()
            #self.top.destroy() #closes the child window
    def cancel(self):
        print ("canceled")
        self.top.grab_release()
        #self.top.parent.destroy()
        self.top.destroy()
        
class scheduleMenu: #first window
#label.config(font=("Courier", 44))
    def __init__(self, parent):

        top = self.top = Toplevel(parent)
        top.parent = parent
        top.geometry('300x300')
        top.grab_set() #gives the window a forced focus

        #self.readTitles()
        scheduleSelect = Listbox(top, font=(None, 15))
        if not(os.path.isfile("userNames.txt")):
            q = open("userNames.txt","w+")
            q.close()
        f = open("userNames.txt","r")
        for line in f:
            scheduleSelect.insert(END, line)
        f.close()

        scheduleSelect.bind("<Double-Button-1>", self.OnDouble)
        scheduleSelect.pack()
        
##        action_with_arg = partial(action, arg)
##button = Tk.Button(master=frame, text='press', command=action_with_arg)
        
        #action_with_arg = partial(self.addTitles, userNewTitle)
        Button(top, text = "New User", command=self.newSchedule).pack()

    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        try:
            value = widget.get(selection[0])
            print ("selection:", selection, ": '%s'" % value)
            f = open ("userNameChosen.txt","w+")
            f.write (value+"\n")
            f.close()
            self.top.destroy()
            #self.readTitles()
        except:
            pass
    def newSchedule(self): #makes a popup and takes user input,
                                    #it then adds it to the text file                                    
        self.inputNewTitle = createNewTitle(self.top)
        
##    def readTitles(self): #reads the titles
##        scheduleSelect = Listbox(self.top, font=(None, 15))
##        
##        f = open("titles.txt","r")
##        for line in f:
##            scheduleSelect.insert(END, line) #creates a list of thingys
##        f.close()
##        scheduleSelect.pack()
##    def closething(self):
##        self.top.destroy()


def create_menu():
    window = scheduleMenu(mainScreen)    

mainScreen = Tk()
mainScreen.geometry('500x100')
new = Button(mainScreen, text = "Hello!", command=create_menu)
new.pack()
mainloop()
