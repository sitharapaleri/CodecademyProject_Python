'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'
lovely_loveseat_price  = 254.00
stylish_settee_description  = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50
luxurious_lamp_description ="Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15
sales_tax = .088

 
def price_calcilator(item_selected):
  customer_one_total = 0.0 
  customer_one_itemization ="" 
  for position in range(len(item_selected)) :
      
    if item_selected[position] == 'Loveseat' :
        customer_one_itemization += "\n" + lovely_loveseat_description
        customer_one_total += lovely_loveseat_price
    elif item_selected[position] == "Lamp" :
        customer_one_total += luxurious_lamp_price
        customer_one_itemization += "\n" + luxurious_lamp_description 
    elif item_selected[position] == "settee":
        customer_one_total += stylish_settee_price
        customer_one_itemization += "\n" + stylish_settee_description
    customer_one_tax = round(customer_one_total * sales_tax,2)
  print( 'Total price(including sales tax) = ' + str(customer_one_tax) + "     " + '\n'+'Item Description' +customer_one_itemization)
  
price_calculator(['settee','Loveseat','Lamp'])    

  
      

