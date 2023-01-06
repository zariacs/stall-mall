def productFileWriter(items):
  f = open("inventory.txt", "wt")    #Opens the file
  for i in range(0, len(items), 5):
    f.write(items[i] + "_")
    f.write(items[i+1] + "_")
    f.write(items[i+2] + "_")
    f.write(items[i+3] + "_")
    f.write(items[i+4] + "_\n")
  f.close()      