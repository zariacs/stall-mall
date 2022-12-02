import orderFileReader
import orderFileWriter
import os
import time

def completeOrder():
  orders, ordersDict = orderFileReader.orderFileReader()

  x = True
  while x is True:
    print("Please enter the order number of the order you would like to complete.")
    resp = input("Order Number: ")
    for j in range (0, len(orders), 8):
      if resp == orders[j+7]:
        x = False
        for q in range(8):
          orders.pop(j)
        orderFileWriter.orderFileWriter(orders)
        os.system('clear')
        print("Order " + resp + " has been completed!")
        time.sleep(2)
        break
    else:
      print("Order cannot be found!")
      y = True
      while y is True:
        resp2 = input("Enter 1 to try again or 0 to exit: ")
        if resp2 == "1":
          y = False
        elif resp2 == "0":
          y = False
          x = False
        else:
          print("Invalid input!")
      
  