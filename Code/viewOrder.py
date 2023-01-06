import orderFileReader
import productFileReader
import os


def viewOrder(id):
  items, itemsDict = productFileReader.productFileReader()
  orders, ordersDict = orderFileReader.orderFileReader()
  counter = 0
  tot2 = 0

  lst = []
  iDict = {}
  for i in range(0, len(orders), 8):
    if str(id) == orders[i]:
      counter+=1
      index = orders[i+4]
      quant = str(orders[i+5])
      loc = str(orders[i+6])
      oNum = str(orders[i+7])
      name = "Item" + index
      tot = int(itemsDict[name]["Price"])*int(quant)
      tot2 = tot2 + tot

      print(counter)
      print("Name - " + itemsDict[name]["Name"])
      print("Description - " + itemsDict[name]["Description"])
      print("Location - " + loc)
      print("Quantity - " + quant)
      print("Total - $" + str(tot) + ".00")
      print("Order Number - " + oNum + "\n")

      name2 = "I" + str(counter)
      iDict[name2] = {}
      iDict[name2]["Index1"] = counter
      iDict[name2]["Index2"] = index
      iDict[name2]["Name"] = itemsDict[name]["Name"]
      iDict[name2]["Quantity"] = quant
      iDict[name2]["Location"] = loc
      iDict[name2]["Order Number"] = oNum

      lst.append(str(counter))
      lst.append(str(index))
      lst.append(str(itemsDict[name]["Name"]))
      lst.append(str(quant))
      lst.append(str(loc))
      lst.append(str(oNum))


  if counter == 0:
    print("You have no current orders!")
    return lst, iDict
  
  if tot2 != 0:
    print("Final Total - $" + str(tot2) + ".00")
    return lst, iDict

    

  
      