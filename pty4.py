items = [("Notebook",80,10,5),("Pen Pack",120,5,12),("Bag",900,1,18)]
subtotal = 0
for name, price, qty, tax_rate in items: subtotal += price * qty
discount = min(subtotal * 0.10, 500) if subtotal >= 2000 else 0
total_tax = 0
for name, price, qty, tax_rate in items:
    line = price * qty
    allocated_discount = discount * line / subtotal if subtotal else 0
    tax = (line - allocated_discount) * tax_rate / 100
    total_tax += tax
    print(name, "Qty:", qty, "Line:", line, "Tax:", round(tax, 2))
print("Subtotal:", subtotal, "Discount:", discount, "Tax:", round(total_tax, 2), "Grand total:", round(subtotal-discount+total_tax, 2))