def orderFileWriter(items):
  f = open("orders.txt", "wt")    #Opens the file
  for i in range(0, len(items), 8):
    f.write(items[i] + "_")
    f.write(items[i+1] + "_")
    f.write(items[i+2] + "_")
    f.write(items[i+3] + "_")
    f.write(items[i+4] + "_")
    f.write(items[i+5] + "_")
    f.write(items[i+6] + "_")
    f.write(items[i+7] + "_\n")
  f.close()      