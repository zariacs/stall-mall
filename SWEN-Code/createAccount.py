import stdiomask
import base64
import userFileReader
import userFileWriter
import main
import os
import time

def createAccount():
  info, usersDict = userFileReader.userFileReader()

  fname = input("Enter your first name: ")
  while True:
    if "_" in fname:
      fname = input("Underscores cannot be used in your name! Please try again: ")
    else:
      break
  if len(fname) == 0:
    fname = "Anonymous"

  lname = input("Enter your last name: ")
  while True:
    if "_" in lname:
      lname = input("Underscores cannot be used in your name! Please try again: ")
    else:
      break
  if len(lname) == 0:
    lname = "Anonymous"

  pnum = None
  while True:
    while True:
      try:
        pnum = int(input("Enter your phone number name(7 digits without the 876): "))
      except ValueError:
        print("Error. Phone numbers should only contain numbers!")
        continue
      else:
        break
    if len(str(pnum)) != 7:
      print("Error. Phone numbers must be 7 digits long!")
    else:
      break
      

  x = True
  while x is True:
    uname = input("Enter your username: ")
    for i in range(0, len(info), 7):
      if uname == info[i+1]:
        print("Username already in use!")
        q = True
        while q is True:
          rpy = input("If you would like to try again enter 1 or enter 0 to exit the Home page: ")
          if rpy == "0":
            q = False
            os.system('clear')
            main.main()
          elif rpy == "1":
            q = False
          else:
            print("\nInvalid input! Please try again!")
            input("Press Enter to continue...")
        break
      elif "_" in uname:
        print("Error! Underscores cannot be used in usernames!")
        q = True
        while q is True:
          rpy = input("If you would like to try again enter 1 or enter 0 to exit the Home page: ")
          if rpy == "0":
            q = False
            os.system('clear')
            main.main()
          elif rpy == "1":
            q = False
          else:
            print("\nInvalid input! Please try again!")
            input("Press Enter to continue...")
        break
    else:
      x = False
      y = True
      while y is True:
        pwd = stdiomask.getpass(prompt="Please enter your password: ", mask="*")
        pwd2 = stdiomask.getpass(prompt="Please confirm your password: ", mask="*")
        if pwd != pwd2:
          print("Passwords do not match!")
        else:
          y = False
          str_enc = base64.b64encode(pwd.encode("utf-8"))
          index = int(info[-7])+1
          info.append(str(index))
          info.append(str(uname))
          info.append(str(str_enc))
          info.append(str(fname))
          info.append(str(lname))
          info.append(str(pnum))
          info.append("N")
          userFileWriter.userFileWriter(info)
          os.system('clear')
          print("Account creation successful!")
          time.sleep(1)
          os.system('clear')
          main.main()
          
          
    
    
  