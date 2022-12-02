def productFileReader():
  f = open("inventory.txt", "rt")    #Opens the file
  items = f.read().split('_')        #adds each element to a list
  f.close()                          #Closes the file
  
  for j in range (0, len(items), 5): #Removes \n from list items
    if "\n" in items[j]:
      items[j]= items[j][1:]
  items.remove(items[len(items)-1])  #Removes the last blank element from the list

  itemsDict = {}                     #initializes dictionary
  #We are using a nested dictionary system
  
  for i in range(0, len(items), 5):  #Adds each detail from each product to a label inside of its own nested dictionary. Each product has its own dictionary inside the main dictionary. 
    name = "Item" + items[i]
    itemsDict[name] = {}
    itemsDict[name]["Index"] = int(items[i])
    itemsDict[name]["Name"] = items[i+1]
    itemsDict[name]["Description"] = items[i+2]
    itemsDict[name]["Price"] = items[i+3]
    itemsDict[name]["Quantity"] = int(items[i+4])

  return items, itemsDict