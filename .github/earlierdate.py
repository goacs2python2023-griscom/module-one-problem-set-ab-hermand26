def date(month1, day1, year1, month2, day2, year2):
    if year1 < year2:
        return "Before"
    elif month1 == month2 and day1 == day2 and year1 == year2:
        return "Same"
    elif year1 <= year2 and month1 < month2:
        return "Before"
    elif year1<= year2 and month1 <= month2 and day1 < day2:
        return "Before"
    else:
        return "After"

print(date(2, 20, 24, 6, 25, 23))