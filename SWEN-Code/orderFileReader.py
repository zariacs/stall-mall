def orderFileReader():
  f = open("orders.txt", "rt")    #Opens the file
  orders = f.read().split('_')        #adds each element to a list
  f.close()                          #Closes the file
  
  for j in range (0, len(orders), 8): #Removes \n from list items
    if "\n" in orders[j]:
      orders[j]= orders[j][1:]
  orders.remove(orders[len(orders)-1])  #Removes the last blank element from the list

  ordersDict = {}                     #initializes dictionary
  #We are using a nested dictionary system
  
  for i in range(0, len(orders), 8):  #adds each detail from each product to a label inside of its own nested dictionary. each product has its own dictionary inside the main dictionary. 
    name = "Order" + orders[i]
    ordersDict[name] = {}
    ordersDict[name]["ID"] = int(orders[i])
    ordersDict[name]["First Name"] = orders[i+1]
    ordersDict[name]["Last Name"] = orders[i+2]
    ordersDict[name]["Phone Number"] = orders[i+3]
    ordersDict[name]["Index"] = int(orders[i+4])
    ordersDict[name]["Quantity"] = int(orders[i+5])
    ordersDict[name]["Location"] = orders[i+6]
    ordersDict[name]["Order Number"] = int(orders[i+7])

  return orders, ordersDict