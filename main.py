from datetime import datetime
duration = 0

def CalDate(strDate):
    targetTime = datetime.strptime(strDate, '%d/%m/%Y %H:%M')
    currentDate = datetime.now()
    duration = targetTime - currentDate
    return duration

duration = CalDate("03/05/2017 15:00")
print duration.total_seconds()/3600

duration = CalDate("03/05/2017 7:00")
print duration.total_seconds()/3600