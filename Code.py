from math import*
import random
global MainDishesDict
global AppetizersDict
global DessrertsDict
global DrinksDict 

global Items 
global Quantity

Quantity = []
Items = {}
global toCart
toCart = {}
#####################
MainDishesDict = {}
AppetizersDict = {}
DessrertsDict = {}
DrinksDict = {}
Total = 0
#####################
def ReadAllFiles(): #DONE
    MainDishesFile = open("MainDishes.txt", "r")
    for line in MainDishesFile:
        key, value = line.strip().split(",")
        MainDishesDict[key] = value
    AppetizersFile = open("Appetizers.txt", "r")
    for line in AppetizersFile:
        key, value = line.strip().split(",")
        AppetizersDict[key] = value
    DrinksFile = open("Drinks.txt", "r")
    for line in DrinksFile:
        key, value = line.strip().split(",")
        DrinksDict[key] = value 
    DessertsFile = open("Desserts.txt", "r")    
    for line in DessertsFile:
        key, value = line.strip().split(",")
        DessrertsDict[key] = value 
def MyMenu(MenuType): #change display into Cart!!! ASAP
    global MainDishesDict
    if MenuType == 1 :
        print("\n"*5,"  *"*6," Main Dishes "," *"*7,"\n","="*60,"\n","|NO.|"," "*2,"|ITEMS|", " "*33, "|PRICE|","\n","="*60)
        i = 1
        for key,value in MainDishesDict.items(): #display Main dishes keys & values, Key -> dish, value -> price
            print("(",i,")",f'{key:<45}{value}KD')
            i += 1
        ChosenDictionary = MainDishesDict
    if MenuType == 2 :
        print("\n"*5,"  *"*6," Appetizers "," *"*7,"\n","="*60,"\n","|NO.|"," "*2,"|ITEMS|", " "*33, "|PRICE|","\n","="*60)
        i = 1
        for key,value in AppetizersDict.items(): #display Main dishes keys & values, Key -> dish, value -> price
            print("(",i,")",f'{key:<45}{value}KD')
            i += 1
        ChosenDictionary = AppetizersDict
    if MenuType == 3 :
        print("\n"*5,"  *"*6," Desserts "," *"*7,"\n","="*60,"\n","|NO.|"," "*2,"|ITEMS|", " "*33, "|PRICE|","\n","="*60)
        i = 1
        for key,value in DessrertsDict.items(): #display Main dishes keys & values, Key -> dish, value -> price
            print("(",i,")",f'{key:<45}{value}KD')
            i += 1
        ChosenDictionary = DessrertsDict
    if MenuType == 4 :
        print("\n"*5,"  *"*6," Drinks  "," *"*7,"\n","="*60,"\n","|NO.|"," "*2,"|ITEMS|", " "*33, "|PRICE|","\n","="*60)
        i = 1
        for key,value in DrinksDict.items(): #display Main dishes keys & values, Key -> dish, value -> price
            print("(",i,")",f'{key:<45}{value}KD')
            i += 1
        ChosenDictionary = DrinksDict

    while True:
         TakeOrder(ChosenDictionary)

         a = int(input('1.Contiue adding     2.Cart       3.Back     4.Exit'))
         if a == 1:
             MyMenu(MenuType)  
         elif a == 2:       
             Cart()
         elif a == 3:
             NewOrder()
         elif a == 4:
             exit()
         else:
            print("*"*5, "INVALID INPUT","*"*5)
def TakeOrder(MyDictonary):
         global Total 

         choise = int(input('\nEnter dish number: '))
         quantity = int(input('Enter how many dishes: '))
        
         item = list(MyDictonary)[choise-1] #extracting the key
         DishPrice = float(MyDictonary[item]) #extracting value

         if item in Items: #checking if the item is already selected 
             Items[item] += quantity   #if yes, update the new quantity + previous quantity
         else:
            Items[item] = quantity
        
         toCart[item] = [Items[item], DishPrice]
         #print(toCart)

         #Calculate Quantity
         Cost = quantity * DishPrice 
         Total += Cost
def NewOrder():#DONE
        print("\n"," "*15,"*"*15,"New Order","*"*15,"\n"," "*15,"*"*41)
        choice = str(input("\nWhat would you like to do?\n\n1.Main Dishes\n2.Appetizers\n3.Desserts\n4.Drinks\n\n(B)Back        (E)Exit \n\nEnter your selection:").upper())
        
        if choice == '1':
                MyMenu(1)
        elif choice == '2':
                MyMenu(2)
        elif choice == '3':
                MyMenu(3)
        elif choice == '4':
                MyMenu(4)
        elif choice == 'B':
                MainMenu()
        elif choice == 'E':
                exit()
        else:
                print("*"*5, "INVALID INPUT","*"*5)
def MainMenu(): #Just function calls remaining
     choice = str(input("What would you like to do?\n1.New order\n2.Cart\n3.Checkout\n\n(B)Back        (E)Exit \nEnter here:").upper())
     while True: 
        if choice == '1':
                NewOrder()
        elif choice == '2':
                Cart()
        elif choice == '3':
                #open Manger
                print("3")
        elif choice == 'B':
                main() 
        elif choice == 'E':
                exit()
        else:
             print("*"*5, "INVALID INPUT","*"*5)
def main():#Just function calls remaining
    a = int(input("Are you a .. \n1.Customer\n2.Manger\nEnter here:"))
    while True:
        if a == 1:
            MainMenu()
        elif a == 2:
            #open Manger
            print("Manger")
        else:
            print("*"*5, "INVALID INPUT","*"*5)
def Cart():
    '''
    1. Display items in the Cart
    2. adjust order perform deletion
    3. for adding call New Order 
    '''
    k = 1
    print("\n"*5,"*"*80,"\n\t\t\t    Cart\n","*"*80,
          "\n","="*80,"\n","|NO.|"," "*2,"|ITEMS|","         |Quantity|" ," "*33, "|PRICE|","\n","="*80)
    for i,j in toCart.items():
                    print(" (",k,")"," ",f'{i:<23}{j[0]:<43}{j[1]}')
                    k += 1
    print("\n",'='*80,"\n Total price: \t\t\t\t\t\t\t\t",f'{Total:.2f}', "KD\n",
            '='*80,"\n\n (1) Add More     (2) Delete item     (3) Confirm Order   (B) Back    (E) Exit") 
    choice = str(input())
    if choice == '1':
        NewOrder() #D
    elif choice == '2':
        deletion()
    elif choice == '3':
        Confirmation()
    elif choice == 'B':
        NewOrder()
    elif choice == 'E':
        exit()
    else:
        print("*"*5, "INVALID INPUT","*"*5)
def deletion():
    global Total 
    k = 1
    print("\n"*5,"*"*80,"\n\t\t\t    Delete \n","*"*80,
          "\n","="*80,"\n","|NO.|"," "*2,"|ITEMS|","         |Quantity|" ," "*33, "|PRICE|","\n","="*80)
    for i,j in toCart.items():
                    print(" (",k,")"," ",f'{i:<23}{j[0]:<43}{j[1]}')
                    k += 1
    print("\n",'='*80,"\n Total price: \t\t\t\t\t\t\t\t",f'{Total:.2f}', "KD\n") 
    UserInput = int(input("Are you sure you wnat to delete items? 1.Yes 2.Back Main Menu 3.Exit "))

    if UserInput == 1:
        
        take = int(input("What item: "))
        DishPrice2 = list(toCart)[take-1]
        Price = toCart[DishPrice2][1]
        num = toCart[DishPrice2][0]
        #print(Price)
        Total -= (Price*num)
        toCart.pop(DishPrice2)
        again = int(input("Would you like to delete more? 1.Yes     2.Back to Main Menu "))
        if again == 1:
            deletion()
        elif again == 2:
            MainMenu()
        elif UserInput == 3:
            exit()
        else:
            print("*"*5, "INVALID INPUT","*"*5)
def Confirmation():
    k = 1
    global OrderId
    Ids = []
    chars ='abcdefghijklmnopqrstuvwxyz'
    chars += chars.upper()
    nums = str(1234567890)
    chars+=nums
    lenght = 9

    global OrderID
    OrderID ="".join(random.sample(chars,lenght))

    confirm = int(input("\nConfirm your order? \n 1. Yes 2. No "))
    if confirm == 1:
         print("\n"*5,"*"*80,"\n\t\t\t    Receipt  \n","*"*80,
          "\n","="*80,"\n","Order no.", OrderID,"\n","="*80,"\n",
          "|NO.|"," "*2,"|ITEMS|","         |Quantity|" ," "*33, "|PRICE|","\n","="*80)
         for i,j in toCart.items():
                    print(" (",k,")"," ",f'{i:<23}{j[0]:<43}{j[1]}')
                    k += 1
    print("\n",'='*80,"\n Total price: \t\t\t\t\t\t\t\t",f'{Total:.2f}', "KD\n",
            '='*80,"\n\n  (D) Download receipt (B) Back    (E) Exit") 
    choice = str(input())
    
    if choice == 'D':
        print("DOWNLOAD PDF")
    if choice == 'B':
        MainMenu()
    elif choice == 'E':
        exit()
    else:
        print("*"*5, "INVALID INPUT","*"*5)


ReadAllFiles()
main()




