def Invoice():
	customerID = str(input('Enter Customer ID: '))
	milkChocolate = int(input('Number of box of Milk Chocolate @ $8.50: '))
	darkEuropean = int(input('Number of box of Dark European @ $9.75: '))
	whiteChocolate = int(input('Number of box of White Chocolate @ $10.50: '))
	europeanTruffles = int(input('Number of box of European Truffles @ $12.50: '))

	total_costMilkChocolate = 8.50 * float(milkChocolate)
	if milkChocolate < 0 or milkChocolate == 0:
		total_costMilkChocolate = 0
	total_costDarkEuropean = 9.75 * float(darkEuropean)
	if darkEuropean < 0 or darkEuropean == 0:
		total_costDarkEuropean = 0
	total_costWhiteChocolate = 10.50 * float(whiteChocolate)
	if whiteChocolate < 0 or whiteChocolate == 0:
		total_costWhiteChocolate = 0
	total_costEuropeanTruffles = 12.50 * float(europeanTruffles)
	if europeanTruffles < 0 or europeanTruffles == 0:
		total_costEuropeanTruffles = 0

	subtotal = total_costMilkChocolate + total_costDarkEuropean + total_costWhiteChocolate + total_costEuropeanTruffles
	salesTax = subtotal * 0.095
	shipping = subtotal * .1

	grandtotal = subtotal + salesTax + shipping

	print('Invoice for Customer AF101:',customerID)
	print(milkChocolate,'Milk Chocolate @ $8.50 is $' + str(round(total_costMilkChocolate,2)))
	print(darkEuropean,'Dark European @ $9.75 is $' + str(round(total_costDarkEuropean,2)))
	print(whiteChocolate,'White Chocolate @ $10.50 is $' + str(round(total_costWhiteChocolate,2)))
	print(europeanTruffles,'European Truffles @ $12.50 is $' + str(round(total_costEuropeanTruffles,2)))

	print('Subtotal             $' + str(round(subtotal,2)))
	print('Sales Tax @ 9.5%     $' + str(round(salesTax,2)))
	print('Shipping @ 10.0%     $' + str(round(shipping,2)))
	print('Grand Total          $' + str(round(grandtotal,2)))

	
