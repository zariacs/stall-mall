import os
import viewProducts
import main
import businessinfo
import orderManager
import notificationManager

def customerMenu(id, uname, fname, lname, pnum, nstatus):
  y = True
  while y is True:
    print("Customer Menu\n")
    print("1 - View Products\n2 - Orders\n3 - Notifications\n4 - Business Information\n5 - Log out")
    resp = input("\nPlease enter the number the corresponds to the option you would like to go to: ")
    if resp == "1":
      os.system('clear')
      viewProducts.viewProducts()
      input("Press Enter to continue...")
      os.system('clear')
    elif resp == "2":
      os.system('clear')
      orderManager.orderManager(id, fname, lname, pnum)
    elif resp == "3":
      os.system('clear')
      notificationManager.customerNotificationPortal(id, uname, fname, lname, pnum, nstatus)
    elif resp == "4":
      os.system('clear')
      businessinfo.businessinfo()
      input("Press Enter to continue...")
      os.system('clear')
    elif resp == "5":
      y = False
      os.system('clear')
      main.main()
    else:
      print("\nInvalid input! Please try again!")
      input("Press Enter to continue...")
      os.system('clear')

    #q = True
    #while q is True:
      #resp = input("\nPlease enter the number 1 to go back to the Customer Menu: ")
      #if resp == "1":
        #q = False
        #os.system('clear')
      #else:
        #print("\nInvalid input!")


  
