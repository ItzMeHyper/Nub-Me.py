import calendar

year = 2023
cal = calendar.TextCalendar(calendar.SUNDAY)
i = 1
while i <= 12:
    cal.prmonth(2024,i) #Of the year given
    i+=1