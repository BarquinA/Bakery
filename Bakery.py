#Initialize variables

overallshoplist = [["Bread", 50, 50], ["Apple Pie", 70, 30], ["Cupcakes", 100, 20]] #Overall list of items
itemfound = 0 #Checks if item is found (option 2/3)

print("Welcome to the Bakery! Here, we have lots of items to check out!")
#Start of program
while True:
    #Asks user for condition
    condition = input("Enter 1 to print a table for all items and their info, enter 2 to print a specific item's price, enter 3 to update a specific item or their price, enter 4 to remove an item, enter 5 to add a new item, or enter 6 to end the program: ")
    #Does something based on condition number
    if condition == "1":
        #Creates table
        print(f"{"Name":<10} {"Price":^5} {"Stock":>10}")
        for itemlist in overallshoplist:
            print(f"{itemlist[0]:<10} {itemlist[1]:^5} {itemlist[2]:>10}")
    elif condition == "2" or condition == "3":
        #Finds item in order to access/update them
        itemvalue = input("Type item you want to access: ")
        for itemlist in overallshoplist:
            if itemlist[0] == itemvalue:
                itemfound = "Found"
                if condition == "2":
                    print(f"Found, Item: {itemlist[0]}, Price: {itemlist[1]}, Stock: {itemlist[2]}")
                if condition == "3":
                    itemlist[0] = input("Enter new item: ")
                    itemlist[1] = int(input("Enter new price: "))
                    itemlist[2] = int(input("Enter new stock: "))
                    print("Item updated.")
                if condition == "4":
                    overallshoplist.remove(itemlist)
        if itemfound != "Found":
            print("Error: Item not found")
    elif condition == "5":
        addeditem = input("Enter the name of the item you want to add: ")
        addedprice = input("Enter the price of the item you want to add: ")
        addedstock = input("Enter the stock of the item you want to add: ")
        overallshoplist.append({addeditem, addedprice, addedstock})
    elif condition == "6":
        #Ends program
        break
    else:
        #Restarts the program if input is different
        print("Invalid input. Type again.")