from colorama import init
init()
from colorama import Fore
from colorama import Style
from random import randrange
import time
import sys
waiter_commentary = {
    "Greeting": "Hi and welcome to the most awesome and Fantastic Diner!", #0
    "Menu Selection": "What menu would you like to order from? Breakfast, Lunch, or Dinner? ", #1
    "Menu Response": "Fantastic! Here you are!", #2
    "Failed Menu Selection": "Sorry, I didn't quite catch what you said. Could you say it again?", #3
    "Choose Entree": "You can choose one entree and two sides at the printed price. Anything extra will cost more.", #4
    "Invalid Option": "That's not a valid option!", #5
    "Unlisted Number": "I'm sorry, but I can only take a number that was listed. Please try again", #6
    "Order Side?": "Would you like to order something from the Sides menu, another Entree, or checkout at this time?", #7
    "Checkout": "Thanks for eating at the most awesome and Fantastic Diner today! Have a wonderful day!" #8
}
Breakfast_menu = {
    "  1. Cinnamon Rolls": '4.99',
    "  2. Bagel with Cream Cheese": '3.99', 
    "  3. Biscuits and Gravy": '6.99',
    "  4. Eggs Benedict With Sausage": '5.50',
    "  5. Toasted English Muffin": '4.50',
    "  6. Buttermilk Pancakes and Maple Syrup": '5.99'
}
Breakfast_menu_definitions = [
    "| 3 Large Cinnamon Rolls                                                     |",
    "| Comes with 3 Large Bagels                                                  |",
    "| 2 Large Biscuits covered in Gray                                           |",
    "| 3 Farm Raised Eggs and 4 Premium German Sausages                           |",
    "| 3 Fluffy Toasted English Muffins with a choice of Jam                      |",
    "| 6\" tall Stack of Large Buttermilk Pancakes with Authentic Maple Syrup      |"
]
Lunch_menu = {
    "  1. San Francisco Fish and Chips": "10.50",
    "  2. Deep Fried Shrimp": "10.50",
    "  3. Southern Fried Chicken": "10.50",
    "  4. Chicken Fried Steak": "13.75",
    "  5. Spinach Lasagna": "10.25",
    "  6. Fettuccine Alfredo with Chicken": "11.95"
}
Dinner_menu = {
    "  1. San Francisco Fish and Chips": "15.50",
    "  2. Deep Fried Shrimp": "15.50",
    "  3. Southern Fried Chicken": "15.50",
    "  4. Chicken Fried Steak": "18.75",
    "  5. Spinach Lasagna": "15.25",
    "  6. Fettuccine Alfredo with Chicken": "16.95"
}
Dinner_menu_definitions = [
    "| Golden Rock Cod served with coleslaw, French fries & tartar sauce.         |",
    "| Breaded deep fried shrimp, served with coleslaw, cocktail sauce.           |",
    "| Crispy fried chicken served with coleslaw & French fries.                  |",
    "| Topped with country gravy and served with potatoes and vegetables.         |",
    "| Stuffed with shredded baby spinach, garlic, leeks, and parmesan cheese.    |",
    "| Stuffed with ground beef and mozzarella and parmesan cheese.               |",
    "| Sauteed chicken breast and broccoli florets, tossed with Alfredo sauce.    |"
]
Sides_menu = {
    "  1. Green Salad": "4.25",
    "  2. Asparagus": "1.50",
    "  3. Corn on the cob": "1.50",
    "  4. Baked potato": "1.50",
    "  5. Egg rolls": "2.50",
    "  6. Garlic bread": "3.50"
}
print()

def typing_commentary(waiter_response):
    print(Fore.RED + "Waiter: " + Style.RESET_ALL, end = "", flush = True)
    for char in waiter_response:
        sys.stdout.write(char)
        sys.stdout.flush()
        seconds = "0.0" + str(randrange(50, 100, 40))
        seconds = float(seconds)
        time.sleep(seconds)
    print()
typing_commentary(list(waiter_commentary.values())[0]) #Greeting
def main_menu():
    typing_commentary(list(waiter_commentary.values())[1]) #Menu Selection
    def menu_selection():
        what_menu = input(">>> ") #3
        print()
        if what_menu.lower() == 'breakfast':
            typing_commentary(list(waiter_commentary.values())[2]) #Menu Response
            time.sleep(0.5)
            Breakfast()
        elif what_menu.lower() == 'lunch':
            typing_commentary(list(waiter_commentary.values())[2])
            time.sleep(0.5)
            Lunch()
        elif what_menu.lower() == 'dinner':
            typing_commentary(list(waiter_commentary.values())[2])
            time.sleep(0.5)
            Dinner()
            
        else:
            typing_commentary(list(waiter_commentary.values())[3]) #Failed Menu Selection
            menu_selection()
    menu_selection()
def Breakfast():
    menu_item = 0
    border_length = 76
    print("+" + "-"*(border_length) + "+")
    print("|                               Breakfast Menu                               |")
    for entree, price in Breakfast_menu.items():
        print(f'{entree} - ${price}')
        print(list(Breakfast_menu_definitions)[menu_item])
        print("|                                                                            |")
        menu_item += 1
        time.sleep(0.05)
    print("+" + "-"*(border_length) + "+")
    typing_commentary(list(waiter_commentary.values())[4]) #Choose Entree
    add_to_total("entree", Breakfast_menu, Breakfast)
def Lunch():
    menu_item = 0
    border_length = 76
    print("+" + "-"*(border_length) + "+")
    print("|                                 Lunch Menu                                 |")
    for entree, price in Lunch_menu.items():
        print(f'{entree} - ${price}')
        print(list(Dinner_menu_definitions)[menu_item])
        print("|                                                                            |")
        menu_item += 1
        time.sleep(0.05)
    print("+" + "-"*(border_length) + "+")
    typing_commentary(list(waiter_commentary.values())[4]) #Choose Entree
    add_to_total("entree", Lunch_menu, Lunch)
def Dinner():
    menu_item = 0
    border_length = 76
    print("+" + "-"*(border_length) + "+")
    print("|                                Dinner Menu                                 |")
    for entree, price in Dinner_menu.items():
        print(f'{entree} - ${price}')
        print(list(Dinner_menu_definitions)[menu_item])
        print("|                                                                            |")
        menu_item += 1
        time.sleep(0.05)
    print("+" + "-"*(border_length) + "+")
    typing_commentary(list(waiter_commentary.values())[4]) #Choose Entree
    add_to_total("entree", Dinner_menu, Dinner)
def Sides(repeat_menu):
    menu_item = 0
    border_length = 76
    print("+" + "-"*(border_length) + "+")
    print("|                                 Sides Menu                                 |")
    for entree, price in Sides_menu.items():
        print(f'{entree} - ${price}')
        print("|                                                                            |")
        menu_item += 1
        time.sleep(0.05)
    print("+" + "-"*(border_length) + "+")
    typing_commentary(list(waiter_commentary.values())[4]) #Choose Entree
    add_to_total("side", Sides_menu, repeat_menu)
def Order_side(dish, what_menu, repeat_menu, total_cost):
    typing_commentary(list(waiter_commentary.values())[7]) #Order Side?
    print("Please type \"Side\", \"Entree\", or \"Checkout\"")
    side_entree_checkout = input(">>> ")
    print()
    if side_entree_checkout.lower() == "side":
        typing_commentary(list(waiter_commentary.values())[2]) #Menu Response
        time.sleep(0.5)
        Sides(repeat_menu)
    elif side_entree_checkout.lower() == "entree":
        typing_commentary(list(waiter_commentary.values())[2]) #Menu Response
        time.sleep(0.5)
        backtrack_to_entree = repeat_menu()
        backtrack_to_entree
    elif side_entree_checkout.lower() == "checkout":
        typing_commentary(list(waiter_commentary.values())[8]) #Checkout
        print(f'Your total is: ${total_cost}')
        print()
        print()
    else:
        typing_commentary(list(waiter_commentary.values())[5]) #Invalid Option
        Order_side(dish, what_menu, repeat_menu, total_cost)
total_cost = 0
def add_to_total(dish, what_menu, repeat_menu):
    global total_cost
    while True:
        try:
            selected_entree = int(input(f'(Please select the number that corresponds to the desired {dish}): '))
            break
        except:
            typing_commentary(list(waiter_commentary.values())[5]) #Invalid Option
    if selected_entree in range(1, 7):
        total_cost += float(list(what_menu.values())[selected_entree - 1])
        print(f'Current Total: ${total_cost}')
        print()
        Order_side(dish, what_menu, repeat_menu, total_cost) #If else statement to redirect to desired menu
    else:
        typing_commentary(list(waiter_commentary.values())[6]) #Unlisted Number
        add_to_total("entree", what_menu, repeat_menu)
main_menu()
input("Press [Enter] to exit...")