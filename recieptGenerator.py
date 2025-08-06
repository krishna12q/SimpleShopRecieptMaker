store_name = input("Your Store Name: ")
gstPercent = int(input("How Much GST Does Your Shop Take"))

items_bought = {}
totalCost = 0

def take_item_val():
    item = input("Enter Item Name: ")
    price = int(input("Item Price: "))

    items_bought.update([(item, price)])

    option = input("Do you want to add more [Y] [N]")

    if(option == "Y"):
        take_item_val()
    else:
        print("_________________________________________________________________________")
        print(store_name)
        print("_________________________________________________________________________")
        print("Shop Reciept")
        print("_________________________________________________________________________")
        print(items_bought)
        print("_________________________________________________________________________")

        for item in items_bought:
            global totalCost
            totalCost = totalCost + items_bought.get(item)

        print(f"Total Cost: {totalCost}")
        Gst = (gstPercent / 100) * totalCost
        afterGst = totalCost + Gst
        print(f"{gstPercent}% GST")
        print(f"Total Cost is {afterGst}")
        print("_________________________________________________________________________")
        print("Thank You")
        print("_________________________________________________________________________")

take_item_val()