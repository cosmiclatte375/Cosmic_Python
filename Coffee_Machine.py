operation=1
milk=1.0 #liter
coffee=1.0 #kg
sugar=1.0 #kg
water=1.0 #liter
price=0
profit=0

print("Welcome to cosmic coffee")
while(operation==1):
    choice= input("What would you like to have(latte/espresso/cappuccino)?").lower()

    #Lattee block
    if(choice=="latte"):
        if water >= 0.2 and milk >= 0.15 and coffee >= 0.024:
            water-=0.2
            milk-=0.15
            coffee-=0.024
            price+=25
            profit+=25
            print(f"Your total bill is {price} please insert coins(5,10,20)")
            coins5=int(input("How many 5 rupee coins you inserted in machine"))
            coins10 = int(input("How many 10 rupee coins you inserted in machine"))
            coins20 = int(input("How many 20 rupee coins you inserted in machine"))
            total=coins5*5+coins10*10+coins20*20
        if(total>price):
            print(f"You have inserted too much money here is your change{total-price} rupees")
            print("Thank you here is your order")
        elif total == price:
            print("Exact amount received.")
            print("Thank you here is your order")
        else:
            print("Not enough resources for Latte.")

    #Espresso block
    elif(choice=="espresso"):
        if(water>=0.05 and coffee>=0.018):
            water-=0.05
            coffee-=0.018
            price+=15
            profit+=15
            print(f"Your total bill is {price} please insert coins(5,10,20)")
            coins5 = int(input("How many 5 rupee coins you inserted in machine"))
            coins10 = int(input("How many 10 rupee coins you inserted in machine"))
            coins20 = int(input("How many 20 rupee coins you inserted in machine"))
            total = coins5 * 5 + coins10 * 10 + coins20 * 20
            if (total > price):
                print(f"You have inserted too much money here is your change{total - price}")
                print("Thank you here is your order")
            elif total == price:
                print("Exact amount received.")
                print("Thank you here is your order")
            else:
                print("Not enough resources for Latte.")

    elif(choice=="cappuccino"):
        if(milk>=0.1 and water>=0.25 and coffee>=0.024):
            water-=0.25
            milk-=0.1
            coffee-=0.024
            price+=30
            profit+=30
            print(f"Your total bill is {price} please insert coins(5,10,20)")
            coins5 = int(input("How many 5 rupee coins you inserted in machine"))
            coins10 = int(input("How many 10 rupee coins you inserted in machine"))
            coins20 = int(input("How many 20 rupee coins you inserted in machine"))
            total = coins5 * 5 + coins10 * 10 + coins20 * 20
            if (total > price):
                print(f"You have inserted too much money here is your change{total - price}")
                print("Thank you here is your order")
            elif total == price:
                print("Exact amount received.")
                print("Thank you here is your order")
            else:
                print("Not enough resources for Latte.")

    elif(choice=="report"):
        print(f"Water={water} litres")
        print(f"Milk={milk} litres")
        print(f"Coffee={coffee} kg")
        print(f"Money={price} rupees")

    elif choice == "off":
        print("Machine shutting down.")
        break

    else:
        print("Invalid choice. Try again.")





