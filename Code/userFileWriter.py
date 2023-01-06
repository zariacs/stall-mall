def userFileWriter(info):
  f = open("users.txt", "wt")    #Opens the file
  for i in range(0, len(info), 7):
    f.write(info[i] + "_")
    f.write(info[i+1] + "_")
    f.write(info[i+2] + "_")
    f.write(info[i+3] + "_")
    f.write(info[i+4] + "_")
    f.write(info[i+5] + "_")
    f.write(info[i+6] + "_\n")
  f.close()      