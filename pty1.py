applicants = [("Asha",91,78,94,250000),("Bala",88,80,92,280000),("Charan",84,82,96,200000),("Divya",91,76,94,240000),("Eshan",90,70,98,180000)]
eligible = []
for name, aggregate, min_subject, attendance, income in applicants:
    if aggregate >= 85 and min_subject >= 75 and attendance >= 90 and income <= 300000:
        eligible.append((name, aggregate, attendance, income))
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))
print("Rank Name Aggregate Attendance Income")
for rank, (name, aggregate, attendance, income) in enumerate(eligible, 1):
    print(rank, name, aggregate, attendance, income)
