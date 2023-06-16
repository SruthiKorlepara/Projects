print("---------------------------------------------Welcome to Supermart------------------------------------------------------------------")

name=input("Enter your name : ")
address=input("Enter your address : ")

list_of_items = '''
Rice     Rs.50/kg
Dal      Rs.70/kg
Wheat    Rs.60/kg
Oil      Rs.100/kg
Sugar    Rs.50/kg
Salt     Rs.25/kg
Coffee   Rs.90/kg
Tea      Rs.150/kg
Paneer   Rs.300/kg'''

# Declaration 
price = 0
total_price = 0
final_price = 0
plist = []
items_list = []
quantity_list = []
price_list = []

# Rate of items
items = {'Rice':50,'Dal':70,'Wheat':60,'Oil':110,'Sugar':50,'Salt':25,'Coffee':80,'Tea':150,'Paneer':300}
option = int(input("For List of items Press 1: "))
if (option == 1):
    print(list_of_items)
for i in range(len(items)):
    inp1 = int(input("If you want to buy press 1 or press 2 for exit: "))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your item name : ")
        quantity = int(input("Required quantity : "))
        if item in items.keys():
            price = quantity * (items[item])
            plist.append((item,quantity,items,price))
            total_price += price
            items_list.append(item)
            quantity_list.append(quantity)
            price_list.append(price)
            gst = (total_price * 5)/100
            final_price = gst + total_price
        else:
            print("Your item is Unavailable")
    else:
            print("You entered wrong number")

final_input = input("Can I bill the items? yes or no: ")
if final_input == "yes":
    pass
    if final_price!=0:
        print(25 * "*","Supermart",30 * "*")
        print(28 * " ","")
        print("Name:",name,30 * " ")
        print(75* "-")
        print("S.No",8 * " ","Item",8 * " ","Quantity",4 * " ","Price")
        print(75* "-")
        for i in range(len(plist)):
            print(i,10 * " ",list_of_items[i],10 * " ",quantity_list[i],5 * " ",price_list[i])
        print(75 * "-")
        print(50 * " ","Total Amount:","Rs.",total_price)
        print(50 * " ","Gst Amount:","Rs.",gst)
        print(75 * "-")
        print(50 * " ",'Final Amount:','Rs.',final_price)
        print(75* "-")
        print(50 * " ","Thanks for Visiting")
        print(75 * "-")
else:
    print("Try again after Some time")







































































