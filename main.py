from datetime import datetime
from time import *
import Tkinter as tk
import ttk
duration = 0
TEXT_MAXINPUTSIZE = 2
'''
def validateTextInputSize(event):
    """ Method to Validate Entry text input size """
    global TEXT_MAXINPUTSIZE
    if (event.widget.index(tk.END) > TEXT_MAXINPUTSIZE - 1):
        event.widget.delete(TEXT_MAXINPUTSIZE - 1)
def hourValidate(P,self):
    print 123
    print P

    try:
        if int(P) < 0:
            self.after_idle(lambda: self.configure(value="0", validate='focusout'))
            self.focus_set()
            return False
        elif int(P) > 12:
            self.after_idle(lambda: self.configure(value="12", validate='focusout'))
            self.focus_set()
            return False
        else:
            return True
    except ValueError:
        self.after_idle(lambda: self.configure(value="0", validate='focusout'))
        self.focus_set()
        return False

def CalDuration(strDate):
    targetTime = datetime.strptime(strDate, '%d/%m/%Y %H:%M')
    currentDate = datetime.now()
    duration = targetTime - currentDate
    return duration

def main():
    while True:
        strDate = raw_input("Please input date:")
        duration = CalDuration(strDate).total_seconds()
        if duration > 0:
            break
    sleep(int(duration))
    print duration / 3600


'''
class YAlarm(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("YAlarm")
        self.pack(fill=tk.BOTH, expand=1)

        self.hourLabel = tk.Label(self, text="Hour")
        self.hourLabel.grid(row=1,column=0,padx=20)

        self.minuteLabel = tk.Label(self, text="Minute")
        self.minuteLabel.grid(row=1,column=1,padx=20)

        self.hourT = tk.Entry(self)
        #self.hourT.bind("<Key>", validateTextInputSize)
        self.hourT["width"] = 2
        self.hourText = tk.StringVar()
        self.hourText.set("0")
        minVal = 0
        maxVal = 12
        vHourscmd = (self.register(self.validate), '%P', '%W', minVal, maxVal)
        self.hourSB = tk.Spinbox(self, textvariable=self.hourText, from_=minVal, to=maxVal, width=3, validate="focusout",validatecommand=vHourscmd)

        self.hourSB.grid(row=2, column=0, padx=20)

        minVal = 0
        maxVal = 60
        vMinutescmd = (self.register(self.validate), '%P', '%W', minVal, maxVal)
        self.minuteText = tk.StringVar()
        self.minuteSB = tk.Spinbox(self, textvariable=self.minuteText, from_=minVal, to=maxVal, width=3, validate='focusout',validatecommand=vMinutescmd)
        self.minuteSB.grid(row=2, column=1, padx=20)
        vTimecmd = (self.register(self.validateTime),'%P', '%W')
        self.timeSB = tk.Spinbox(self, value=("AM", "PM"), width=4, validate='focusout',validatecommand=vTimecmd)
        self.timeSB.grid(row=2, column=2, padx=20)

    def validate (self, P,W,minVal,maxVal):
        try:
            if int(P) < int(minVal):
                self.nametowidget(W).after_idle(lambda: self.nametowidget(W).configure(value=minVal, validate='focusout'))
                return False
            elif int(P) > int(maxVal):
                print maxVal
                self.nametowidget(W).after_idle(lambda: self.nametowidget(W).configure(value=maxVal, validate='focusout'))
                return False
            else:
                return True
        except ValueError:
            self.nametowidget(W).after_idle(lambda: self.nametowidget(W).configure(value=minVal, validate='focusout'))
            return False

    def validateTime (self, P,W):
        print P
        print P is "PM"
        if (P == "AM") or (P == "PM"):
            return True
        else:
            self.nametowidget(W).after_idle(lambda: self.nametowidget(W).configure(value="AM", validate='focusout'))
            return False


def main():
    root=tk.Tk()
    root.geometry("250x150+300+300")
    meh = YAlarm(root)
    root.mainloop()

if __name__ == '__main__':
    main()
'''
root = Tk()
root.resizable(width=False,height=False)
root.minsize(height=200, width=200)

topFrame = Frame(root)
topFrame.pack(side=TOP)

title = Label( topFrame,text="YAlarm")
title.pack(side=TOP)

midFrame = Frame(root)
midFrame.pack()

hour = Label( midFrame,text="Hour")
hour.grid(row=0,column=0,padx=20)
minute = Label( midFrame,text="Minute")
minute.grid(row=0,column=1,padx=20)
'''
'''
hourT = Entry (midFrame)
hourT.bind("<Key>", validateTextInputSize)
hourT["width"] = 2
hourText = StringVar()
hourText.set("0")
vcmd = (midFrame.register(hourValidate),'%P')
hourSB = Spinbox(midFrame,textvariable=hourText, from_=0, to=12,width=3,validate="focusout",validatecommand=vcmd)
hourSB.grid(row=1,column=0,padx=20)

minuteText = StringVar()
minuteSB = Spinbox(midFrame,textvariable=minuteText, from_=0, to=60,width=3,validate='focusout')
minuteSB.grid(row=1,column=1,padx=20)

timeSB = Spinbox(midFrame, value=("AM","PM"),width=4)
timeSB.grid(row=1,column=2,padx=20)

'''