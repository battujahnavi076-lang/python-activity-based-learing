students = ["Asha","Bala","Charan","Divya"]
subjects = ["Python","Maths","Physics"]
marks = [[88,76,81],[67,72,58],[45,49,52],[91,85,89]]
totals = []
for i in range(len(marks)):
    total = sum(marks[i]); totals.append(total)
    print(students[i], "Total:", total, "Average:", round(total/len(subjects), 2))
top = totals.index(max(totals))
print("Top performer:", students[top], "Total:", totals[top])
for j, subject in enumerate(subjects):
    average = sum(marks[i][j] for i in range(len(marks))) / len(marks)
    print(subject, "average:", round(average, 2))
    if average < 50: print("Warning: low class average")