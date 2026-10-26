basic, allowances, overtime, incentive = 22000, 5000, 1800, 1200
gross = basic + allowances + overtime + incentive
if gross <= 15000: deduction = 0
elif gross <= 25000: deduction = (gross - 15000) * 0.05
else: deduction = 10000 * 0.05 + (gross - 25000) * 0.10
print("Basic pay:", basic, "Allowances:", allowances, "Overtime:", overtime, "Incentive:", incentive)
print("Gross salary:", gross, "Deduction:", round(deduction, 2), "Net salary:", round(gross - deduction, 2))