import datetime
from datetime import date

def friday_13(month, year):
    fri = datetime.date(year, month, 13)
    return fri.strftime("%A") == "Friday"

mon = int(input("Enter the month: "))
yr = int(input("Enter the year: "))
print()
print("Does 13th come as Friday for month ",mon,"year ",yr,"? ",friday_13(mon,yr))

