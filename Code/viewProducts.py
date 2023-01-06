import productFileReader
import customerMenu

def viewProducts():
  items, itemsDict = productFileReader.productFileReader() 
  counter = 1
  for k in range(0, len(items), 5):  #prints the items
    name2 = "Item" + str(counter)
    print(itemsDict[name2]["Index"])
    print("Product Name: " + itemsDict[name2]["Name"])
    print("Description: " + itemsDict[name2]["Description"])
    print("Price: " + "$" + itemsDict[name2]["Price"] + ".00")
    if itemsDict[name2]["Quantity"]>10:
      print("In stock")
    elif itemsDict[name2]["Quantity"] == 0:
      print("Out of stock")
    else:
      print("Only " + str(itemsDict[name2]["Quantity"]) + " left. Order Now!")
    print("")
    counter+=1

  #print(len(itemsDict))

  #res = sorted(itemsDict.items(), key = lambda x:x[1]["Price"])

  #print(res)
  #print(res[0][1][1])
    
    