# Create grocery_item dictionary and grocery_history list
grocery_item = {}
grocery_history = []

#Variable used to check if the while loop condition is met
stop = 'go'

while stop != 'q' :

#Accept input of the item name, quantity, and cost
  item_name = input('Item Name: ')
  item_quant = int(input('Item Quantity: '))
  item_cost = float(input('Cost of item: '))
#Take the user input and enter it into our grocery_item dictionary
  grocery_item['name'] = item_name
  grocery_item['number'] = int(item_quant)
  grocery_item['price'] = float(item_cost)
#Add the grocery_item to the grocery_history list using the append function
  grocery_history.append(grocery_item.copy())
#Ask the user if they are done adding to the list/dictionary
  stop = input("Would you like to enter another item? \nType 'c' for continue or 'q' for quit: ")

  
# Define variable to hold grand total called 'grand_total'
grand_total = 0

# This for loop will do the math for us, totaling up our costs.
for index,item in enumerate(grocery_history):
  item_total = item['number'] * item['price']
  grand_total += item_total
  #Output the information for the grocery item
  print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))
  item_total = 0

#Print the grand total
print('Grand Total: $%.2f' % grand_total)
