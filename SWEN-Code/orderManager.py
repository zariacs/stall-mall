import os
import viewOrder
import placeOrder
import cancelOrder

def orderManager(id, fname, lname, pnum):
  while True:
    print("Order Manager")
    print("\n1 - View Order(s)\n2 - Place Order\n3 - Cancel Order\n4 - Customer Menu")
    rp = input("\nPlease enter the number that corresponds to the option you would like to go to: ")
    if rp == "1":
      os.system('clear')
      lst, iDict = viewOrder.viewOrder(id)
      input("\nPress Enter to continue...")
      os.system('clear')
      continue
    elif rp == "2":
      os.system('clear')
      placeOrder.placeOrder(id, fname, lname, pnum)
      continue
    elif rp == "3":
      os.system('clear')
      cancelOrder.cancelOrder(id)
      continue
    elif rp == "4":
      os.system('clear')
      break
    else:
      print("Invalid input! Please try again!")
      input("Press Enter to continue...")
      os.system('clear')