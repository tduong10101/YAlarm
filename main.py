from datetime import datetime
from time import *
from Tkinter import *
from ttk import *
duration = 0
TEXT_MAXINPUTSIZE = 2

def validateTextInputSize(event):
    """ Method to Validate Entry text input size """
    global TEXT_MAXINPUTSIZE
    if (event.widget.index(END) > TEXT_MAXINPUTSIZE - 1):
        event.widget.delete(TEXT_MAXINPUTSIZE - 1)


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

def hourValidate (P):
    print 123
    print P

    try:
        if int(P) < 0:
            hourSB.after_idle(lambda: hourSB.configure(value="0",validate='focusout'))
            hourSB.focus_set()
            return False
        elif int(P) > 12:
            hourSB.after_idle(lambda: hourSB.configure(value="12", validate='focusout'))
            hourSB.focus_set()
            return False
        else:
            return True
    except ValueError:
        hourSB.after_idle(lambda: hourSB.configure(value="0", validate='focusout'))
        hourSB.focus_set()
        return False



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
hourT = Entry (midFrame)
hourT.bind("<Key>", validateTextInputSize)
hourT["width"] = 2
'''
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
countryvar = StringVar()
country = Combobox(midFrame, textvariable=countryvar)
country.bind('<<ComboboxSelected>>')
country['values'] = ('USA', 'Canada', 'Australia')
country.grid(row=1,column=0,padx=20)
'''
root.mainloop()

'''
-need to use class for frame
-add validation for minutes and AM/PM text
-start on set button
'''