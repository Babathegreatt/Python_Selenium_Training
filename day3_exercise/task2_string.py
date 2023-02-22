# Mary Smith wants to purchase a Shirt

custName = 'Mary Smith'
itemDesc = ['Shirt', 'bag', 'toy', 'mobile']

outOfStock = False

price = 50.50
quantity = 10
tax = (price * quantity * 10) / 100
total = None

print('Customer can purchase', len(itemDesc), 'items')

if quantity > 1:
    message = custName + 'wants to purchase ' + str(quantity) + str(itemDesc[3]) + 's'
else:
    message = custName + 'wants to purchase ' + str(quantity) + str(itemDesc[3])
    total = (price * quantity) + tax

if outOfStock:
    print('item is unavailable.')
else:
    print(message)
    print("total cost with tax is :", total)
