#pw= KKSadmin#1
#un= admin1
#cpw= enter123
#zpw= password
import stdiomask
import base64
import userFileReader
import customerMenu
import employeeMenu
import time
import os
import main

def login():
  info, usersDict = userFileReader.userFileReader()
  str_enc = None

  y = True
  while y is True:
    un = input("Please enter your username: ")
    for i in range(1, len(info), 7):
      if un == info[i]:
        y = False
        pwd = stdiomask.getpass(prompt="Please enter your password: ", mask="*")
        str_enc = base64.b64encode(pwd.encode("utf-8"))
        break
    else:
      print("\nUser (" + un + ") does not exist!")
      x = True
      while x is True:
        rpy = input("If you would like to try again enter 1 or enter 0 to exit the Home page: ")
        if rpy == "0":
          x = False
          os.system('clear')
          main.main()
        elif rpy == "1":
          x = False
          os.system('clear')
        else:
          print("\nInvalid input! Please try again!")
          input("Press Enter to continue...")
          os.system('clear')

    
  if info[i+1]==str(str_enc) and info[i-1]=="1001":
    os.system('clear')
    print("Login Successful!")
    print("\nWelcome Krissy!")
    time.sleep(1)
    os.system('clear')
    employeeMenu.employeeMenu()
  elif info[i+1]==str(str_enc):
    id = info[i-1] 
    uname = info[i] 
    fname = info[i+2] 
    lname = info[i+3] 
    pnum = info[i+4]
    nstatus = info[i+5]
    os.system('clear')
    print("Login Successful!")
    print("\nWelcome " + fname + "!")
    time.sleep(1)
    os.system('clear')
    customerMenu.customerMenu(id, uname, fname, lname, pnum, nstatus)
  else:
    print("\nInvalid Password!")
    x = True
    while x is True:
      rpy = input("If you would like to try again enter 1 or enter 0 to exit the login page: ")
      if rpy == "0":
        x = False
        os.system('clear')
        main.main()
      elif rpy == "1":
        x = False
        os.system('clear')
        login()
      else:
        print("\nInvalid input! Please try again!")
        input("Press Enter to continue...")
        os.system('clear')
