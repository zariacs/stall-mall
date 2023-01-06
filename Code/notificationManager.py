# Welcome to the Notification Manager
# This is divided into a few sections for readability. Each section is surrounded
# by the appropriate section comments.
# User Interace, Mailing Lists - Admin and Customer, Support for Mailing Lists,
# Getters of Product Details, Customer Notifications, Stock Alert Notifications,
# Display Notifications

# Associated files
# customerNotifications.txt
# adminNotifications.txt
# customerMailingList.txt

# Other dependencies
# inventory.txt
import productFileReader
import productFileWriter
import userFileReader
from art import *
import os
import customerMenu
import employeeMenu
import userFileReader

# User Interface
def customerNotificationPortal(userID, uname, fname, lname, pnum, nstatus):
    # portal allowing navigation through customer options regarding notifications
    print("Hello and Welcome to\n")
    tprint("Notifications\n\n")
    print("What would you like to do? \n1. View Notifications \n2. Join Mailing List \n3. Return to Main Menu\n\n")
    portalNavSelection = input("Your Selection: ")
    print("\n\n")

    if portalNavSelection == '1':
        if inCustomerMailingList(userID):
            os.system('clear')
            customerNotificationScreen(userID, uname, fname, lname, pnum, nstatus)
        else:
            joinMailingListScreen(userID, uname, fname, lname, pnum, nstatus)
            os.system('clear')
            customerNotificationPortal(userID, uname, fname, lname, pnum, nstatus)
            
    elif portalNavSelection == '2':
        joinMailingListScreen(userID, uname, fname, lname, pnum, nstatus)

    elif portalNavSelection == '3':
        os.system('clear')
        customerMenu.customerMenu(userID, uname, fname, lname, pnum, nstatus)
        
    tprint("----------")
    input("When you're ready to go back to the main menu, press enter...")
    os.system('clear')
    customerMenu.customerMenu
    
def customerNotificationScreen(userID, uname, fname, lname, pnum, nstatus):
    # screen for viewing customer notifications on
    print("Hi, these are your\n")    
    tprint("Notifications\n\n")
    displayCustomerNotifications()
    tprint("----------")
    input("When you're ready to go back to the notifications menu, press enter...")
    os.system('clear')
    customerNotificationPortal(userID, uname, fname, lname, pnum, nstatus)

def adminNotificationScreen():
    # Screen/Portal for admin navigation within Notification Management System
    print("Hello and Welcome to\n")
    tprint("Notifications\n\n")
    notifSelection = input("What would you like to do?\n\n1. View Admin Notifications \n2. View Customer Notifications \n3. Send Out Customer Notification \n4. Add Customer to Mailing List \n5. Add Admin to Mailing List\n\nYour selection: ")
    os.system('clear')

    # Redirection of the user based on their selection
    tprint("Notifications\n\n")
    if notifSelection == '1':
        displayAdminNotifications()        
    elif notifSelection == '2':
        displayCustomerNotifications()
    elif notifSelection == '3':
        os.system('clear')
        broadcastCustomerNotificationScreen()
    elif notifSelection == '4':
        userIDToBeAdded = input("Please enter the user ID of the customer: ")
        print("\n")
        addToCustomerMailingList(userIDToBeAdded)
    elif notifSelection == '5':
        userIDToBeAdded = input("Please enter the user ID of the new admin: ")
        print("\n")
        addToAdminMailingList(userIDToBeAdded)
        
    tprint("----------")    
    print("Menu \n1. Return to Notifications Menu \n2. Return to Main Menu\n")
    exitSelection = input("Your selection: ")
    os.system('clear')

    if exitSelection == '1':
        adminNotificationScreen()
    elif exitSelection == '2':
        employeeMenu.employeeMenu()

def joinMailingListScreen(userID, uname, fname, lname, pnum, nstatus):
    # Menu for joining or not joining customer mailing list
    print("Want to join our mailing list to see our notifications? \n1. Yes \n2. No \n\n")
    joinListChoice = input("Your Selection: ")
    print("\n")
    if joinListChoice == '1':
        addToCustomerMailingList(userID)
    elif joinListChoice == '2':
        print("\nYou can join anytime.")
        
    tprint("----------")    
    input("When you're ready to go back to the notifications menu, press enter...")    
    os.system('clear')
    customerNotificationPortal(userID, uname, fname, lname, pnum, nstatus)
        
def broadcastCustomerNotificationScreen():
    # Menu options for admin to send different kinds of notifications
    print("You're at the Best Part of")
    tprint("Notifications\n\n")
    print("What kind of notification would you like to send to your customers?\n")
    print("1. Price Change Notification \n2. New Product Notification \n3. Write my own notification \n4. View Product List \n5. Return to Notifications Menu \n\n Note: If you're sending a notification about a price change or new product, make sure you know the product ID. If you want to view the product list to check a product's ID, enter 4 as your choice for where to go next.\n\n")
    notifTypeSelection = input("Your Selection: ")
    print("\n\n")

    # redirecting the user based on their chosen notification type to create
    # price change notification
    if notifTypeSelection == '1':
        print("Have you changed the price for this product already? \n1. Yes\n2. No\n\n")
        changeCompleted = input("Your selection: ")
        print("\n")
        if changeCompleted == '1':
            prodID = input("Please enter the product ID: ")
            print("\n")
            sendPriceChangeNotification(prodID)
        elif changeCompleted == '2':
            input("You will now be taken to the admin menu so that you can change the price of the product before the notification is sent out. This way your notification will contain the up to date price. Press enter to continue...") 
            os.system('clear')
            employeeMenu.employeeMenu()

    # new product notification        
    elif notifTypeSelection == '2':
        print("Is this new product already in the system or would you like to add it? \n\n1. Already in the System \n2. Add Product Now\n")
        productAdded = input("Your selection: ")
        print("\n\n")
        if productAdded == '1':
            prodID = input("Please enter the product ID: ")
            print("\n")
            sendNewProductNotification(prodID)
        elif productAdded == '2':
            input("You will now be taken to the admin menu so that you can add the product before the notification is sent out. This way your notification will include the new product's details. Press enter to continue...") 
            os.system('clear')
            employeeMenu.employeeMenu()
            
    # self-written notification
    elif notifTypeSelection == '3':
        print("Nice choice. What would you like to say to your customers? \n\n")
        broadcast = input("Your Message: ")
        print("\n")
        sendSpecialNotification(broadcast)

    # redirection to employee menu for user to view product list
    elif notifTypeSelection == '4':
        os.system('clear')
        employeeMenu.employeeMenu()

    # return to notification menu screen
    elif notifTypeSelection == '5':
        os.system('clear')
        adminNotificationScreen()
# End of User Interface

        
# Mailing Lists - Admin and Customer
def addToCustomerMailingList(userID):
    allUsers, userDict = userFileReader.userFileReader()
    userKey = f"User{userID}"
    fname = userDict[userKey]["First Name"]
    
    mailingListFile = open("customerMailingList.txt", "a+")
    mailingListFile.seek(0)
    mailingList = mailingListFile.readlines()
    
    # constructs list of customer IDs for customers in mailing list
    if inCustomerMailingList(userID):
        print(f"Hey {fname}, you're already on our mailing list.")
    else:
        lname = userDict[userKey]["Last Name"]
        contactNumber = userDict[userKey]["Phone Number"]
        mailingListFile.write(f"{userID} {fname} {lname} {contactNumber}\n")
        print(f"{fname}, you've been added to our mailing list! Look out for notifications from us.")    
    
    mailingListFile.close()

def addToAdminMailingList(userID):
    allUsers, userDict = userFileReader.userFileReader()
    userKey = f"User{userID}"
    fname = userDict[userKey]["First Name"]
    
    mailingListFile = open("adminMailingList.txt", "a+")
    mailingListFile.seek(0)
    mailingList = mailingListFile.readlines()
    # constructs list of customer IDs for customers in mailing list
    mailingListIDs = [str(userInfo.split()[0]) for userInfo in mailingList]    

    # checks if current customer already in mailing list
    if str(userID) in mailingListIDs:
        print(f"Hey {fname}, you're already on our admin-only mailing list.")
    # when customer not already in mailing list, proceed with adding them
    else:
        lname = userDict[userKey]["Last Name"]
        contactNumber = userDict[userKey]["Phone Number"]
        mailingListFile.write(f"{userID} {fname} {lname} {contactNumber}\n")
        print(f"{fname}, you've been added to our admin-only mailing list! Look out for notifications from us.")  
# End of Mailing Lists

        
# Suppport Functions for Mailing Lists
def getCustomerMailingListIDs():
    userFile = open("customerMailingList.txt", "r")
    userInfo = userFile.readlines()
    userIDs = None
    if len(userInfo) > 0:
        userIDs = [str(user.split()[0]) for user in userInfo]
    userFile.close()
    return userIDs

def getAdminMailingListIDs():
    userFile = open("adminMailingList.txt", "r")
    userInfo = userFile.readlines()
    userIDs = None
    if len(userInfo) > 0:
        userIDs = [str(user.split()[0]) for user in userInfo]
    userFile.close()
    return userIDs

def inCustomerMailingList(userID):
    mailingList = getCustomerMailingListIDs()
    if not mailingList:
        return False
    if userID in mailingList:
        return True
    else:
        return False
# End of Support Functions for Mailing Lists

        
# Getters of Product Details
def getProductName(productID):
    products, productDict = productFileReader.productFileReader()
    productKey = f"Item{productID}"    
    name = productDict[productKey]["Name"]
    return name

def getProductDescription(productID):
    products, productDict = productFileReader.productFileReader()
    productKey = f"Item{productID}"
    desc = productDict[productKey]["Description"]
    return desc    

def getProductPrice(productID):
    products, productDict = productFileReader.productFileReader()
    productKey = f"Item{productID}"    
    price = productDict[productKey]["Price"]
    return price    

def getProductQuantity(productID):
    products, productDict = productFileReader.productFileReader()
    productKey = f"Item{productID}"    
    quantity = productDict[productKey]["Quantity"]
    return quantity   
# End of Getters for Product Details

    
# Customer Notifications
def sendCustomerNotification(text):
    # is called by all other customer notification functions
    notificationFileWriter("customerNotifications.txt", text)

def sendSpecialNotification(text):                  
    #unique/custom notifications
    sendCustomerNotification(text)

def sendPriceChangeNotification(productID): 
    notif = f"The price of {getProductName(productID)} is now ${getProductPrice(productID)}"
    sendCustomerNotification(notif)

def sendNewProductNotification(productID): 
    notif = f"We now have {getProductName(productID)} on sale for ${getProductPrice(productID)}"
    sendCustomerNotification(notif)
# End of Customer Notifications

    
# Stock Alert Notifications
def sendAdminNotification(text):
    # products running low
    notificationFileWriter("adminNotifications.txt", text)

def sendLowStockAlert(productID):
    notif = f"We're running low on {getProductName(productID)}. Right now we have {getProductQuantity(productID)} in stock."
    sendAdminNotification(notif)

def evaluateInventory(productID):
    # checks if the given product is running low and sends a low stock alert if needed             # otherwise does nothing
    qty = getProductQuantity(productID)
    if int(qty) < 10:
        sendLowStockAlert(productID)
# End of Stock Alert Notifications

        
# Display Notifications
def displayCustomerNotifications(): #
    # prints all notifications that have been sent to customers
    customerNotifs = open("customerNotifications.txt").readlines()
    if len(customerNotifs) == 0:
        print("There haven't been notifications yet. Check back anytime!")
    else:
        for notif in customerNotifs:
            notifID = notif.split()[0]
            notifText = (" ").join(notif.split()[1:])
            print(f"{notifID}\n{notifText}\n\n")
    

def displayAdminNotifications():
    print("---------------------------------ADMIN---------------------------------\n\n")
    adminNotifs = open("adminNotifications.txt").readlines()
    if len(adminNotifs) == 0:
        print("There haven't been any admin notifications yet. Check back anytime!\n\n")
        
    else:
        for notif in adminNotifs:
            notifID = notif.split()[0]
            notifText = (" ").join(notif.split()[1:])
            print(f"{notifID}\n{notifText}\n\n")
# End of Display Notifications


def notificationFileWriter(fileName, text):
    notifsFile = open(fileName, "a+")
    notifsFile.seek(0)
    notifs = notifsFile.readlines()
    notificationID = len(notifs) + 1
    notification = f"{notificationID} {text}"

    notifsFile.write(f"{notification}\n")
    if fileName != "adminNotifications.txt":
        print(f"Notification Sent! - {notification}")

    notifsFile.close()
    