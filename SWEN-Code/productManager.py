import addProduct
import editProduct
import os

def productManager():
  y = True
  while y is True:
    print("Product Manager\n")
    print("1 - Add Product\n2 - Edit Product\n3 - Employee Menu")
    resp = input("\nPlease enter the number that corresponds to the option you would like to go to.")
    if resp == "1":
      os.system('clear')
      addProduct.addProduct()
    elif resp == "2":
      os.system('clear')
      editProduct.editProduct()
    elif resp == "3":
      y = False
      os.system('clear')
    else:
      print("\nInvalid input! Please try again!")
      input("Press Enter to continue...")
      os.system('clear')
    