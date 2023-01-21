def busses(NumberOfStudents):
    if NumberOfStudents % 52 == 0:
        return int(NumberOfStudents / 52)
    else:
        return int(NumberOfStudents / 52) + 1

print(busses(360), 'busses.')

