import productFileReader
import productFileWriter
import os
import time
import notificationManager

def editProduct():
  items, itemsDict = productFileReader.productFileReader()

  while True:
    print("Please state which product you would like to edit by entering its corresponding index.")
    counter = 0
    for k in range(0, len(items), 5):  #prints the items
      counter+=1
      name = "Item" + str(counter)
      print(str(itemsDict[name]["Index"]) + " - " + itemsDict[name]["Name"] )
    resp = input("Index: ")
    try:
      if int(resp)>counter:
        print("Error! Invalid input!")
        input("Press Enter to continue...")
        os.system('clear')
        continue
      else:
        os.system('clear')
        break
    except ValueError:
      print("Error! Index should be a number!")
      input("Press Enter to continue...")
      os.system('clear')
      continue

  
  resp2 = str(resp)
  name2 = "Item" + resp2

  z = True
  x = True
  while x is True:
    print("Please state which type of edit you would like to make to the product by entering its corresponding index.")
    print("1 - Name - (" + str(itemsDict[name2]["Name"]) + ")\n2 - Description - (" + str(itemsDict[name2]["Description"]) + ")\n3 - Price - ($" + str(itemsDict[name2]["Price"]) + ".00)\n4 - Quantity - (" + str(itemsDict[name2]["Quantity"]) + ")\n0 - Delete Product\n999 - Exit")
    resp2 = input("Index: ")
    rps =["0", "1", "2", "3", "4", "999"]
    if resp2 not in rps:
      print("Invalid input!")
      y = True
      while y is True:
        rp = input("If you would like to try again enter 1 or enter 0 to return to the Product manager: ")
        if rp == "1":
          y = False
        elif rp == "0":
          y = False
          x = False
          z = False
          os.system('clear')
        else:
          print("Invalid Input!")
    else:
      x = False

  if z is True:
    name2 = "Item" + resp
    resp2 = int(resp2)
    if resp2 == 1:
      while True:
        print("The original name is: " + "(" + itemsDict[name2]["Name"] + ")")
        edt = input("Please enter the new name here: ")
        if "_" in edt:
          print("Underscores cannot be used in your product name!")
          input("Press Enter to try again...")
          continue
        else:
          break
        if len(edt) == 0:
          edt = "(No Name)"
      for i in range(0, len(items), 5):
        if items[i] == resp:
          items[i+1] = edt
          productFileWriter.productFileWriter(items)
      os.system('clear')
      print("Item has been successfully updated.")
      time.sleep(3)
      os.system('clear')
        
    elif resp2 == 2:
      while True:
        print("The original description is: " + "(" + itemsDict[name2]["Description"] + ")")
        edt = input("Please enter the new description here: ")
        if "_" in edt:
          print("Underscores cannot be used in your product description!")
          input("Press Enter to try again...")
          continue
        else:
          break
        if len(edt) == 0:
          edt = "(No Description)"
      for i in range(0, len(items), 5):
        if items[i] == resp:
          items[i+2] = edt
          productFileWriter.productFileWriter(items)
      os.system('clear')
      print("Item has been successfully updated.")
      time.sleep(3)
      os.system('clear')
        
    elif resp2 == 3:
      while True:
        try:
          print("The original Price is: " + "($" + itemsDict[name2]["Price"] + ".00)")
          edt = input("Please enter the new price here: ")
          edt2 = int(edt)
        except ValueError:
          print("Error! Prices should only contain numbers!")
          continue
        else:
          break
      for i in range(0, len(items), 5):
        if items[i] == resp:
          items[i+3] = edt
          productFileWriter.productFileWriter(items)
      os.system('clear')
      print("Item has been successfully updated.")
        
      #Allows Customer Notification re Price Change
      notifyChoice = input("\n\nWould you like to send out a notification about this price change? \n1. Yes \n2. No \n\nYour Selection: ")
      if notifyChoice == '1':
          input(f"\n\nThis item's product ID is {itemsDict[name2]['Index']}. Press enter to continue to notification manager...")
          os.system('clear')
          notificationManager.adminNotificationScreen()
      time.sleep(3)
      os.system('clear')

    elif resp2 == 4:
      while True:
        try:
          print("The original Quantity is: " + "(" + str(itemsDict[name2]["Quantity"]) + ")")
          edt = input("Please enter the new quantity here: ")
          edt2 = int(edt)
        except ValueError:
          print("Error! Quantities should only contain numbers!")
          continue
        else:
          break
      for i in range(0, len(items), 5):
        if items[i] == resp:
          items[i+4] = edt
          productFileWriter.productFileWriter(items)
      os.system('clear')
      print("Item has been successfully updated.")

      # Notification Management System
      # Sends an admin alert if we're now running low on the ordered product
      notificationManager.evaluateInventory(resp)
      # End of Notification Management System
      
      time.sleep(3)
      os.system('clear')

    elif resp2 == 0:
      for i in range(0, len(items), 5):
        if items[i] == resp:
          for q in range(5):
            items.pop(i)
          counter = 1
          for j in range(0, len(items), 5):
            items[j] = str(counter)
            counter +=1
          productFileWriter.productFileWriter(items)
          break
      os.system('clear')
      print("Item has been successfully deleted.")
      time.sleep(3)
      os.system('clear')
    elif resp2 == 999:
      os.system('clear')

      
  
    