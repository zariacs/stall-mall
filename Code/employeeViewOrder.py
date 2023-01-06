import orderFileReader
import productFileReader
import os
import completeOrder


def employeeViewOrder():
  items, itemsDict = productFileReader.productFileReader()
  orders, ordersDict = orderFileReader.orderFileReader()
  counter = 0

  for i in range(0, len(orders), 8):
      counter+=1
      index = orders[i+4]
      quant = str(orders[i+5])
      loc = orders[i+6]
      oNum = orders[i+7]
      name = "Item" + index
      tot = int(itemsDict[name]["Price"])*int(quant)

      print("Index - " + str(counter))
      print("Name - " + orders[i+1] + " " + orders[i+2])
      print("Phone Number - (876)" + orders[i+3][:4] + "-" + orders[i+3][3:])
      print("Product Name - " + itemsDict[name]["Name"])
      print("Description - " + itemsDict[name]["Description"])
      print("Location - " + loc)
      print("Quantity - " + quant)
      print("Total - $" + str(tot) + ".00")
      print("Order Number - " + oNum + "\n")
      

  if counter == 0:
    print("There are no current orders!")

  y = True
  while y is True:
    resp = input("Please enter 1 to complete an order or 0 to go back to the Employee Menu: ")
    if resp == "1":
      y = False
      completeOrder.completeOrder()
      os.system('clear')
    elif resp == "0":
      y = False
      os.system('clear')
    else:
      print("\nInvalid input!")
      