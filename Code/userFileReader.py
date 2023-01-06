def userFileReader():
  f = open("users.txt", "rt")    #Opens the file
  info = f.read().split('_')        #adds each element to a list
  f.close()                          #Closes the file
  
  for j in range (0, len(info), 7): #Removes \n from list items
    if "\n" in info[j]:
      info[j]= info[j][1:]
  info.remove(info[len(info)-1])  #Removes the last blank element from the list

  usersDict = {}                     #initializes dictionary
  #We are using a nested dictionary system
  
  for i in range(0, len(info), 7):  #adds each detail from each product to a label inside of its own nested dictionary. each product has it's own dictionary inside the main dictionary. 
    name = "User" + info[i]
    usersDict[name] = {}
    usersDict[name]["ID"] = int(info[i])
    usersDict[name]["Username"] = info[i+1]
    usersDict[name]["Password"] = info[i+2]
    usersDict[name]["First Name"] = info[i+3]
    usersDict[name]["Last Name"] = info[i+4]
    usersDict[name]["Phone Number"] = info[i+5]
    usersDict[name]["nSatus"] = info[i+6]

  return info, usersDict