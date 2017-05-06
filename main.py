from datetime import *
from time import *
import thread
import Tkinter as tk
import ttk
duration = 0

class YAlarm(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("YAlarm")
        self.pack(fill=tk.BOTH, expand=1)

        #set hour spinbox and label
        self.hourLabel = tk.Label(self, text="Hour")
        self.hourLabel.grid(row=1, column=0, padx=20)

        self.hourT = tk.Entry(self)
        self.hourT["width"] = 2
        self.hourText = tk.StringVar()
        self.hourText.set("0")
        minVal = 0
        maxVal = 12
        vHourscmd = (self.register(self.validate),'%d','%P','%W', minVal, maxVal)
        self.hourSB = tk.Spinbox(self, textvariable=self.hourText, from_=minVal, to=maxVal, width=3, validate="all",validatecommand=vHourscmd)
        self.hourSB.grid(row=2, column=0, padx=20)

        #set minute spinbox and label
        self.minuteLabel = tk.Label(self, text="Minute")
        self.minuteLabel.grid(row=1, column=1, padx=20)
        minVal = 0
        maxVal = 59
        self.minuteText = tk.StringVar()
        self.vMinutescmd = (self.register(self.validate),'%d','%P', '%W', minVal, maxVal)
        self.minuteSB = tk.Spinbox(self, textvariable=self.minuteText, from_=minVal, to=maxVal, width=3, validate='all',validatecommand=self.vMinutescmd)
        self.minuteSB.grid(row=2, column=1, padx=20)

        #set time spinbox (AM/PM)
        self.vTimecmd = (self.register(self.validateTime),'%d','%S', '%W')
        self.timeSB = tk.Spinbox(self, value=("AM", "PM"), width=4, validate='all',validatecommand=self.vTimecmd)
        self.timeSB.grid(row=2, column=2, padx=20)

        #Add set button
        self.setButton = tk.Button(self, text='Set',command=self.setButton,width=8)
        self.setButton.grid(row=3, column=2,pady=5)
    def setButton(self):
        hour = int(self.hourText.get())
        minute = int(self.minuteText.get())
        time = self.timeSB.get()
        duration = self.getDuration(hour,minute,time)
        thread.start_new_thread(self.setAlarm, (duration,hour,minute,time))
        print duration
        return True

    def setAlarm(self,duration,hour,minute,time):
        sleep(int(duration))
        print "Wake up time!!!!!!!!!!! it's {0}:{1} {2}".format(hour,minute,time)

    def getDuration(self,hour,minute,time):
        if time == "PM":
            newhour = int(hour)+12
        else:
            newhour = int(hour)
        targetTime = datetime.now()
        targetTime = targetTime.replace(hour=newhour, minute=int(minute),second=0)
        currentDate = datetime.now()
        print targetTime
        print currentDate
        print targetTime < currentDate
        if targetTime < currentDate:
            targetTime += timedelta(days=1)
        duration = targetTime - currentDate


        return duration.total_seconds()

    def validate (self,d,P,W,minVal,maxVal):
        spinbox = self.nametowidget(W)
        try:
            if int(d)!= 0:
                if not P:
                    spinbox.after_idle(lambda: spinbox.configure(value=minVal,validate='all'))
                    return False
                elif (int(P) > int(maxVal)) or len(P) > 2:
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
