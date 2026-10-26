transactions = [("DEPOSIT",2000),("WITHDRAW",1500),("WITHDRAW",4000),("DEPOSIT",0),("WITHDRAW",1000),("TRANSFER",500)]
balance, deposits, withdrawals, accepted, rejected = 5000, 0, 0, 0, 0
for kind, amount in transactions:
    if amount <= 0:
        print("Rejected:", kind, amount); rejected += 1
    elif kind == "DEPOSIT":
        balance += amount; deposits += amount; accepted += 1
    elif kind == "WITHDRAW" and amount <= 3000 and amount <= balance:
        balance -= amount; withdrawals += amount; accepted += 1
    else:
        print("Rejected transaction:", kind, amount); rejected += 1
print("Accepted:", accepted, "Rejected:", rejected, "Deposits:", deposits, "Withdrawals:", withdrawals, "Closing balance:", balance)