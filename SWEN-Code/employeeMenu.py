import os
import viewProducts
import employeeViewOrder
import productManager
import main
import notificationManager

def employeeMenu():
  y = True
  while y is True:
    print("Employee Menu\n")
    print("1 - View Orders\n2 - View Products\n3 - Product Manager\n4 - Inventory Manager\n5 - Notifications\n6 - Log out")
    resp = input("\nPlease enter the number that corresponds to the option you would like to go to: ")
    if resp == "1":
      os.system('clear')
      employeeViewOrder.employeeViewOrder()
    elif resp == "2":
      os.system('clear')
      viewProducts.viewProducts()
      q = True
      while q is True:
        resp = input("\nPlease enter the number 1 to go back to the Employee Menu: ")
        if resp == "1":
          q = False
          os.system('clear')
        else:
          print("\nInvalid input!")
    elif resp == "3":
      os.system('clear')
      productManager.productManager()
    elif resp == "4":
      os.system('clear')
      pass
    elif resp == "5":
      os.system('clear')
      notificationManager.adminNotificationScreen()
    elif resp == "6":
      y = False
      os.system('clear')
      main.main()
    else:
      print("\nInvalid input! Please try again!")
      input("Press Enter to continue...")
      os.system('clear')
      

    