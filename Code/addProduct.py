import productFileReader
import productFileWriter
import os
import notificationManager


def addProduct():
  name = input("Enter Product name: ")
  while True:
    if "_" in name:
      name = input("Underscores cannot be used in the product name! Please try again: ")
    else:
      break
  if len(name) == 0:
    name = "(No name)"
  
  desc = input("Enter Product description: ")
  while True:
    if "_" in desc:
      desc = input("Underscores cannot be used in the description! Please try again: ")
    else:
      break
  if len(desc) == 0:
    desc = "(No description)"
  
  #price = input("Enter Product price(integer value): ")
  while True:
    try:
      price = int(input("Enter Product price(integer value): "))
    except ValueError:
      print("Error! Price should only contain numbers!")
      continue
    else:
      break
 
  #quant = input("Enter Product quantity(integer value): ")
  while True:
    try:
      quant = int(input("Enter Product quantity(integer value): "))
    except ValueError:
      print("Error! Quantity should only contain numbers!")
      continue
    else:
      break

  while True:
    rp = input("Enter 1 to add this product or 0 to go page to the Product Manager.")
    if rp == "1":
      items, itemsDict = productFileReader.productFileReader() 
      index = len(itemsDict) + 1
      items.append(str(index))
      items.append(name)
      items.append(desc)
      items.append(str(price))
      items.append(str(quant))
      productFileWriter.productFileWriter(items)
      
      

      #Allows Customer Notification re New Product
      print("\nWould you like to send out a notification about this new product?\n\n1. Yes \n2. No\n")
      notifChoice = input("Your Selection: ")              
            
      if notifChoice == '1':
          input(f"\nThis item's product ID is {index}. Press enter to continue to notification manager...")
          os.system('clear')
          notificationManager.adminNotificationScreen()
      break
    elif rp == "0":
      os.system('clear')
      break
    else:
      print("\nInvalid input!\n")
      continue
  