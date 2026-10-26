schedule = [("Python","MON",9.0,10.0,"R101"),("Maths","MON",9.5,10.5,"R102"),("Physics","MON",10.0,11.0,"R101"),("English","TUE",9.0,10.0,"R101")]
conflicts = 0
for i in range(len(schedule)):
    course1, day1, start1, end1, room1 = schedule[i]
    for j in range(i+1, len(schedule)):
        course2, day2, start2, end2, room2 = schedule[j]
        if day1 == day2 and start1 < end2 and start2 < end1:
            print("Time conflict:", course1, "and", course2, "on", day1); conflicts += 1
            if room1 == room2: print("Room conflict:", room1)
if conflicts == 0: print("Timetable is valid.")
else: print("Overlapping pairs:", conflicts)