'''
Created on Sep 23, 2022

@author: Brandon Demeritt
'''
menu = {
    "Oil change" : "$35",
    "Tire rotation" : "$19",
    "Car wash" : "$7",
    "Car wax" : "$12",
    "No service chosen" : "$0"
    }
counter = 1
totalPrice = 0
service1 = "-"
service2 = "-"
print("Davy's auto shop services")
for service, price in menu.items():
    print(counter, ")", service, "-->", price,)
    counter = counter + 1
    if counter == 5:
        break

print("\nPlease choose up to two services from the list")
userService1 = input("\nPlease choose your first service(1, 2, 3, 4, or - for none): ")

if userService1 ==  "1":
    totalPrice = totalPrice + 35
    service1 = "Oil change"
elif userService1 == "2":
    totalPrice =  totalPrice + 19
    service1 = "Tire rotation"
elif userService1 == "3":
    totalPrice =  totalPrice + 7
    service1 = "Car wash"
elif userService1 == "4":
    totalPrice =  totalPrice + 12
    service1 = "Car wax"
else:
    service1 = "No service chosen"
    
userService2 = input("Please choose your second service(1, 2, 3, 4, or - for none): ")

if userService2 ==  "1":
    totalPrice += 35
    service2 = "Oil change"
elif userService2 == "2":
    totalPrice +=  19
    service2 = "Tire rotation"
elif userService2 == "3":
    totalPrice +=  7
    service2 = "Car wash"
elif userService2 == "4":
    totalPrice +=  12
    service2 = "Car wax"
else:
    service2 = "No service chosen"

print("\nDavy's auto shop invoice\n\nService 1:", service1, menu[service1], "\nService 2:", service2, menu[service2])
print("\nTotal: $" + str(totalPrice))