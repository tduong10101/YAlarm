from datetime import datetime
from time import *
import Tkinter as tk
import ttk
duration = 0

def CalDuration(strDate):
    targetTime = datetime.strptime(strDate, '%d/%m/%Y %H:%M')
    currentDate = datetime.now()
    duration = targetTime - currentDate
    return duration


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
        vHourscmd = (self.register(self.validate),'%d','%P','%W', minVal, maxVal)
        self.hourSB = tk.Spinbox(self, textvariable=self.hourText, from_=minVal, to=maxVal, width=3, validate="all",validatecommand=vHourscmd)
        self.hourSB.grid(row=2, column=0, padx=20)

        minVal = 0
        maxVal = 60
        self.minuteText = tk.StringVar()
        vMinutescmd = (self.register(self.validate),'%d','%P', '%W', minVal, maxVal)
        self.minuteSB = tk.Spinbox(self, textvariable=self.minuteText, from_=minVal, to=maxVal, width=3, validate='all',validatecommand=vMinutescmd)
        self.minuteSB.grid(row=2, column=1, padx=20)

        vTimecmd = (self.register(self.validateTime),'%d','%S', '%W')
        self.timeSB = tk.Spinbox(self, value=("AM", "PM"), width=4, validate='all',validatecommand=vTimecmd)
        self.timeSB.grid(row=2, column=2, padx=20)

    def validate (self,d,P,W,minVal,maxVal):
        spinbox = self.nametowidget(W)
        try:
            if int(d)!= 0:
                if not P:
                    spinbox.after_idle(lambda: spinbox.configure(value=minVal,validate='all'))
                    return False
                elif int(P) > int(maxVal):
                    return False
                else:
                    return True
            else:
                return True
        except ValueError:
            spinbox.after_idle(lambda: spinbox.configure(value=minVal,validate='all'))
            return False

    def validateTime (self,d,S,W):
        spinbox = self.nametowidget(W)
        if int(d) == 1:
            if S.lower() == "a":
                value = ("AM", "PM")
            elif S.lower() == "p":
                value = ("PM", "AM")
            else:
                return False
            spinbox.after_idle(lambda: spinbox.configure(value=value, validate='all'))
            return False
        else:
            return True


def main():
    root=tk.Tk()
    root.geometry("250x150+300+300")
    meh = YAlarm(root)
    root.mainloop()

if __name__ == '__main__':
    main()
