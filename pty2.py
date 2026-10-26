monthly_units = [80, 120, 190, 280]
previous_bill = None
for month, units in enumerate(monthly_units, 1):
    if units <= 100: energy = units * 1.50
    elif units <= 200: energy = 150 + (units - 100) * 2.50
    else: energy = 150 + 250 + (units - 200) * 4
    bill = energy + 50 + energy * 0.05
    if units < 100: bill -= 30
    print("Month", month, "Units:", units, "Bill: Rs.", round(bill, 2))
    if previous_bill is not None and (bill - previous_bill) / previous_bill * 100 > 30:
        print("Warning: bill increased by more than 30%")
    previous_bill = bill