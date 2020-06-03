cost_price = float(input("enter the cost price : "))
selling_price = float(input("enter the selling price : "))
profit = 0
if selling_price > cost_price :
    profit = selling_price - cost_price

print(" the profit =",profit)

new_sell_price = selling_price + (0.05*cost_price)

print("new selling price for which the profit will increase by 5% =",new_sell_price)
