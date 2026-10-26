attended, total, target = 42, 60, 75
if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance data.")
else:
    future = 0
    while (attended + future) / (total + future) * 100 < target:
        future += 1
    print("Current attendance:", round(attended/total*100, 2), "%")
    print("Additional classes required:", future)
    print("Projected attendance:", round((attended+future)/(total+future)*100, 2), "%")