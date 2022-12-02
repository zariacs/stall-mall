import viewOrder
import orderFileReader
import orderFileWriter
import productFileReader
import productFileWriter
import time
import os

def cancelOrder(id):
  orders, ordersDict = orderFileReader.orderFileReader()
  items, itemsDict = productFileReader.productFileReader()

  y=True
  while y is True:
    lst, iDict = viewOrder.viewOrder(id)
    quant = None
    index = None
  
    if iDict == {}:
      input("\nPress Enter to continue...")
      y = False
      os.system('clear')
    else:
      try:
        print("\nPlease enter the order number of the order you would like to cancel or enter 0 to return to the order Manager.")
        resp = int(input("Order Number: "))
      except ValueError:
        print("\nError! Order numbers should only contain numbers!")
        input("Press Enter to continue...")
        os.system('clear')
        continue
      #y = False
      for i in range(5, len(lst), 6):
          if resp == int(lst[i]):
            index = lst[i-4]
            quant = lst[i-2]
            for k in range(0, len(orders), 8):
              if resp == int(orders[k+7]):
                for q in range(8):
                  orders.pop(k)
                orderFileWriter.orderFileWriter(orders)
                print(index)
                for j in range(0, len(items), 5):
                  if int(items[j]) == int(index):
                    np = int(items[j+4]) + int(quant)
                    items[j+4] = str(np)
                    productFileWriter.productFileWriter(items)
                    break
                break
            os.system('clear')
            print("Order " + str(resp) + " has been cancelled!")
            time.sleep(2)
            os.system('clear')
            break    
            #y = False
        
      else:
        if resp == 0:
          y = False
          os.system('clear')
        else:
          x = True
          print("That order does not exist!")
          while x is True:
            rp = input("Enter 1 to try again or 0 to return to the order manager.")
            if rp == "1":
              x = False
              os.system('clear')
            elif rp == "0":
              x = False
              y = False
              os.system('clear')
            else:
              print("Invalid Input! Please try again!\n")
      
    
              
          
    