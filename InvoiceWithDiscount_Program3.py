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
     total_costDarkEuropean == 0
total_costWhiteChocolate = 10.50 * float(whiteChocolate)
if whiteChocolate < 0 or whiteChocolate == 0:
     total_costWhiteChocolate = 0
total_costEuropeanTruffles = 12.50 * float(europeanTruffles)
if europeanTruffles < 0 or europeanTruffles == 0:
     total_costEuropeanTruffles = 0
     
subtotal = total_costMilkChocolate + total_costDarkEuropean + total_costWhiteChocolate + total_costEuropeanTruffles
salesTax = subtotal * 0.095
print(' ')
print(' ')
print('Invoice for Customer',customerID,':')
print(milkChocolate,'Milk Chocolate @ $8.50 per box        $',str(format(total_costMilkChocolate,'.2f')))
print(darkEuropean,'Dark European @ $9.75 per box         $',str(format(total_costDarkEuropean,'.2f')))
print(whiteChocolate,'White Chocolate @ $10.50 per box     $',str(format(total_costWhiteChocolate,'.2f')))
print(europeanTruffles,'European Truffle @ $12.50 per box    $',str(format(total_costEuropeanTruffles,'.2f')))
print(' ')
print(' ')
print('Subtotal                   $',str(format(subtotal,'.2f')))
if float(subtotal) >= 20.00:
     if float(subtotal) >= 20.00 and float(subtotal) <= 39.99:
          discount = subtotal * 0.1
          netSubtotal = subtotal - discount
          price('Less Discount of 10.0%     $',str(format(discount,'.2f')))
     elif float(subtotal) >= 40.00 and float(subtotal) <= 59.99:
          discount = subtotal * 0.15
          netSubtotal = subtotal - discount
          print('Less Discount of 15.0%     $',str(format(discount,'.2f')))
     elif float(subtotal) >= 60.00 and float(subtotal) <= 79.99:
          discount = subtotal - discount
          netSubtotal = subtotal - discount
          print('Less Discount of 25.0%     $',str(format(discount,'.2f')))
shipping = netSubtotal * 0.1
grandtotal = netSubtotal + shipping
print(' ')
print(' ')
print('Net Subtotal      $',str(format(netSubtotal,'.2f')))
print('Shipping @ 10.0%  $',str(format(shipping,'.2f')))
print(' ')
print(' ')
print('Grand Total       $',str(format(grandtotal,'.2f')))

	

	
