#Aaron Oviedo #1990958

def validate(date):
    valtemp = 0
    newval = ""

    if date.find(",") != -1:
        monthVal, year = date.split(',')
        if monthVal.find(" ") != -1:
            month, day = monthVal.split(" ")
            valtemp = 1

            day = day.strip()
            month = month.strip()
            year = year.strip()

            if month == "January":
                newval = "1" + "/"
            elif month == "February":
                newval = "2" + "/"
            elif month == "March":
                newval = "3" + "/"
            elif month == "April":
                newval = "4" + "/"
            elif month == "May":
                newval = "5" + "/"
            elif month == "June":
                newval = "6" + "/"
            elif month == "July":
                newval = "7" + "/"
            elif month == "August":
                newval = "8" + "/"
            elif month == "September":
                newval = "9" + "/"
            elif month == "October":
                newval = "10" + "/"
            elif month == "November":
                newval = "11" + "/"
            elif month == "December":
                newval = "12" + "/"
            else:
                valtemp = 0

            newval += day + "/"
            newval += year

    if valtemp == 1:
        return newval
    else:
        return ""



userdate = input()

while (userdate != "-1"):
    valDate = validate(userdate)
    if valDate != "":
        print(valDate)
    print()
    userdate = input()

