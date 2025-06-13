actual_cost = float(input("Please Enter the Actual Product Price: "))
sale_price = float(input("Please Enter the Sales Amount: "))
if (actual_cost < sale_price):
    amount = sale_price - actual_cost
    print("Total Profit = {0}".format(amount))

else:
    print("No Profit!!!")
