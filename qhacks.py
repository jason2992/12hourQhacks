from tkinter import *


class requirementFailed:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        top.geometry('280x80')
        top.grab_set() #gives the window a forced focus
        
        Label(top, text="please fill in the required fields", font=(None, 15)).grid(row=1)
        
        b = Button(top, text="ok", command=self.ok, font=(None, 15), height = 1, width = 10)
        b.grid(row=2)
    def ok(self):
        self.top.grab_release()
        self.top.destroy()
  
class addEvent:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)
        top.geometry('620x200')
        top.grab_set() #gives the window a forced focus
        
        
        Label(top, text="eventName", font=(None, 15)).grid(row=1, column=0)
        self.eventName = Entry(top,width=60)
        self.eventName.grid(row=1, column=1,columnspan=3)
        
        Label(top, text="deadline(Monday,25,19:30)", font=(None, 15)).grid(row=2, column=0)
        self.deadlineA = Entry(top,width=15)
        self.deadlineA.grid(row=2, column=1)
        self.deadlineB = Entry(top,width=15)
        self.deadlineB.grid(row=2, column=2)
        self.deadlineC = Entry(top,width=15)
        self.deadlineC.grid(row=2, column=3)
        
        Label(top, text="timeTotal(Hrs)", font=(None, 15)).grid(row=3, column=0)
        self.timeTotal = Entry(top,width=60)
        self.timeTotal.grid(row=3, column=1,columnspan=3)
        
        Label(top, text="timeLength(20,30,60)", font=(None, 15)).grid(row=4, column=0)
        self.timeLength = Entry(top,width=60)
        self.timeLength.grid(row=4, column=1,columnspan=3)
        
        Label(top, text="description", font=(None, 15)).grid(row=5, column=0)
        self.description = Entry(top,width=60)
        self.description.grid(row=5, column=1,columnspan=3)

        b = Button(top, text="confirm", command=self.confirm, font=(None, 15), width = 5)
        b.grid(row=6,column=0)

        b = Button(top, text="cancel", command=self.cancel, font=(None, 15), width = 5)
        b.grid(row=6,column=2)

    def confirm(self):
        #what fields are required?
        if self.eventName.get() != "" and self.timeTotal.get() != "" and (self.timeLength.get() != 20 or self.timeLength.get() != 30 or self.timeLength.get() != 20):
            #testing = "helo"            
            #f = open(testing+".txt","a+")
            k = open("userNameChosen.txt","r")
            self.userName = k.readline()
            k.close()
            self.userName = self.userName.replace("\n", "")
            f = open("./Users/" + self.userName + ".txt","a+") 
            #print ("event stored!", self.value.get())
            f.write(self.eventName.get() + "\n")
            f.write(self.deadlineA.get() + "\n")
            f.write(self.deadlineB.get() + "\n")
            f.write(self.deadlineC.get() + "\n")
            f.write(self.timeTotal.get() + "\n")
            f.write(self.timeLength.get() + "\n")
            f.write(self.description.get() + "\n")
            #f.write("\n")
            f.close()
            self.top.grab_release() #releases forced focus
            self.top.destroy() #closes the child window
        else:
            emptyInput = requirementFailed(self.top)
    def cancel(self):
        print ("canceled")
        self.top.grab_release()
        self.top.destroy()
             
        
def create_window():
##    window = Toplevel(mainScreen)
##    Label(window, text="name").grid(row=0)
##    Label(window, text="age").grid(row=1)
##    userName = Entry(window)
##    userAge = Entry(window)
##
##    userName.grid(row=0, column=1)
##    userAge.grid(row=1,column=1)
    window = addEvent(mainScreen)
#    mainScreen.wait_window(window.top)

def checker():
    print("Hello!")

    
mainScreen = Tk()
mainScreen.geometry('500x100')
##userView = Canvas(mainScreen, width=200, height=200)
##userView.config(bg='yellow')
##userView.create_oval(90,90,110,110, width = 0, fill = "ivory3")
##Button(mainScreen, text = "Hello", command=create_window).grid(row=1, column=0, sticky=W, pady=4)
##Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
##userView.pack()
new = Button(mainScreen, text = "Hello!", command=create_window)
#new = Button(mainScreen, text = "Hello!", command=checker)
new.pack()
mainloop()

##mainScreen.wait_window(window.top)

mainScreen = Tk()
create_menu()
create_window()
