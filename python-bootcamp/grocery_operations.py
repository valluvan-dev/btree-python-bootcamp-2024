
grocery_list = {}



def Add_items(name,price):

    grocery_list[name] = price

    print(f"{name} has been added with a price of ${price}")



def Remove_items(name):

    if name in grocery_list:

        del grocery_list[name]

        print(f"{name} has been removed from the list")

    else:

        print(f"{name} not in the grocery list. ")



def Display_items():

    print("Current Grocery List :")

    for item,price in grocery_list.items():

        print(f"{item} - ${price}")


def Total_cost():

    total = sum(grocery_list.values())
    
    print(f"Total cost of the grocery list is ${total}")