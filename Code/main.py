import login
import createAccount
import os
import sys
import editProduct
import notificationManager

def main():
    
  print("Welcome to")
  print(" _  __     _                     _  ___           _") 
  print("| |/ /    (_)                   | |/ (_)         | |")   
  print("| ' / _ __ _ ___ ___ _   _ ___  | ' / _  ___  ___| | __")
  print("|  < | '__| / __/ __| | | / __| |  < | |/ _ \/ __| |/ /")
  print("| . \| |  | \__ \__ \ |_| \__ \ | . \| | (_) \__ \   < ")
  print("|_|\_\_|  |_|___/___/\__, |___/ |_|\_\_|\___/|___/_|\_\ ")
  print("                      __/ |")             
  print("                     |___/ ")



    
  input("\nPress Enter to continue...")
  os.system('clear')
  
  y = True
  while y is True:
    print("Login Options\n")
    print("1 - Login\n2 - Create Account\n3 - Exit")
    resp = input("\nPlease enter the number that corresponds to the option you would like to go to: ")
    if resp == "1":
      y = False
      os.system('clear')
      login.login()
    elif resp == "2":
      y = False
      os.system('clear')
      createAccount.createAccount()
    elif resp == "3":
      y = False
      os.system('clear')
      print("  _____                 _ _   ")             
      print(" / ____|               | | |  ")            
      print("| |  __  ___   ___   __| | |__  _   _  ___ ") 
      print("| | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ ") 
      print("| |__| | (_) | (_) | (_| | |_) | |_| |  __/ ") 
      print(" \_____|\___/ \___/ \__,_|_.__/ \__, |\___| ") 
      print("                                 __/ |     ") 
      print("                                |___/      ") 
      sys.exit()
      #return
    else:
      print("\nInvalid input! Please try again!")
      input("Press Enter to continue...")
      os.system('clear')
