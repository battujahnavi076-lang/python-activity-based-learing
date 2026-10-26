products = [("P101",50.0,25),("P102",120.0,4),("P103",75.0,0),("",40.0,8),("P105",-10.0,12)]
inventory_value = 0
for product_id, price, stock in products:
    if product_id == "" or price < 0 or stock < 0:
        print("Invalid record:", product_id, price, stock)
    else:
        value = price * stock; inventory_value += value
        print(product_id, "Stock:", stock, "Value:", round(value, 2))
        if stock < 10: print("Replenish", 10-stock, "units")
print("Total valid inventory value:", round(inventory_value, 2))