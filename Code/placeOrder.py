import orderFileReader
import orderFileWriter
import productFileReader
import productFileWriter
import viewProducts
import os
import time
import notificationManager

def placeOrder(id, fname, lname, pnum):
  items, itemsDict = productFileReader.productFileReader()
  orders, ordersDict = orderFileReader.orderFileReader()
  
  y = True
  while y is True:
    try:
      viewProducts.viewProducts()
      print("Please enter the number of the item you would like to order.\n")
      resp = input("Index: ")
      resp2 = int(resp)
      for k in range(0, len(items), 5):
        if int(items[k]) == resp2:
          if int(items[k+4]) == 0:
            print("\nItem is out of stock! Please choose a new Item!")
            input("Press Enter to continue...")
            break
      else:
        for k in range(0, len(items), 5):
          if int(items[k]) == resp2:
            y = False
            break
        else:
          print("\nItem is not available! Please choose a new Item!")
          input("Press Enter to continue...")
    except ValueError:
      print("Error! Index should only contain numbers!")
      input("Press Enter to continue...")
      os.system('clear')
      continue

  x = True
  while x is True:
    try:
      print("\nPlease enter the quantity of the item you would like to order or enter 0 in order to return to the order manager.\n")
      resp3 = input("Quantity: ")
      resp4 = int(resp3)

      if resp4 == 0:
        x = False
        os.system('clear')
        break
      else:
        for k in range(0, len(items), 5):
          if int(items[k]) == resp2:
            if resp4 > int(items[k+4]):
              print("There are only " + items[k+4] + " items left in stock! Please enter a valid quantity!")
              break
        else:
          for k in range(0, len(items), 5):
            if int(items[k]) == resp2:
              prodname = items[k+1]
              price = items[k+3]
              price = int(price)
              items[k+4] = str(int(items[k+4]) - resp4)
          print("Please enter your location.")
          rp = input("Location: ")
          if "_" in rp:
            items[k+4] = str(int(items[k+4]) + resp4)
            print("Location cannot contain underscores!")
            continue
          else:
            x = False
            if len(orders) == 0:
              oNum = 3500
            else:
              oNum = int(orders[-1]) + 1
            orders.append(str(id))
            orders.append(str(fname))
            orders.append(str(lname))
            orders.append(str(pnum))
            orders.append(resp)
            orders.append(resp3)
            orders.append(rp)
            orders.append(str(oNum))
            orderFileWriter.orderFileWriter(orders)
            productFileWriter.productFileWriter(items)
            tot = price * resp4

            os.system('clear')
            print("Your order of " + resp3 + " " + prodname + "(s) has been placed successfully. Your total is $" + str(tot) + ".00. and your order number is " + str(oNum) + ".")

            # Notification Management System
            # Sends an admin alert if we're now running low on the ordered product
            notificationManager.evaluateInventory(resp)
            # End of Notification Management System
            
            input("Press Enter to continue...")
            os.system('clear')
    except ValueError:
      print("\nError! Quantity should only contain numbers!")
      print("Please try again!\n")
      continue

  